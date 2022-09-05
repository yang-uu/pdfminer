import unittest
from pdfminer.runlength import rldecode
from pdfminer.psparser import KWD, LIT, PSEOF, PSBaseParser, PSStackParser
from pdfminer.ccitt import CCITTG4Parser
from ..pdfminer.utils import url



class TestRunLength(unittest.TestCase):

    def test_rldecode(self):
        input = b'\x05123456\xfa7\x04abcde\x80junk'
        result = rldecode(input)
        expected = b'1234567777777abcde'
        self.assertEqual(result, expected)


class TestPSBaseParser(unittest.TestCase):
    TESTDATA = br'''%!PS
begin end
 "  @ #
/a/BCD /Some_Name /foo#5f#xbaa
0 +1 -2 .5 1.234
(abc) () (abc ( def ) ghi)
(def\040\0\0404ghi) (bach\\slask) (foo\nbaa)
(this % is not a comment.)
(foo
baa)
(foo\
baa)
<> <20> < 40 4020 >
<abcd00
12345>
func/a/b{(c)do*}def
[ 1 (z) ! ]
<< /foo (bar) >>
'''

    TOKENS = [
        (5, KWD(b'begin')), (11, KWD(b'end')),
        (16, KWD(b'"')), (19, KWD(b'@')),
        (21, KWD(b'#')), (23, LIT('a')),
        (25, LIT('BCD')), (30, LIT('Some_Name')),
        (41, LIT('foo_xbaa')),
        (54, 0), (56, 1), (59, -2), (62, 0.5),
        (65, 1.234), (71, b'abc'), (77, b''), (80, b'abc ( def ) ghi'),
        (98, b'def \x00 4ghi'), (118, b'bach\\slask'), (132, b'foo\nbaa'),
        (143, b'this % is not a comment.'),
        (170, b'foo\nbaa'), (180, b'foobaa'),
        (191, b''), (194, b' '), (199, b'@@ '),
        (211, b'\xab\xcd\x00\x124\x05'),
        (226, KWD(b'func')), (230, LIT('a')), (232, LIT('b')),
        (234, KWD(b'{')), (235, b'c'), (238, KWD(b'do*')), (241, KWD(b'}')),
        (242, KWD(b'def')), (246, KWD(b'[')),
        (248, 1), (250, b'z'), (254, KWD(b'!')),
        (256, KWD(b']')), (258, KWD(b'<<')), (261, LIT('foo')), (266, b'bar'),
        (272, KWD(b'>>'))
    ]

    OBJS = [
        (23, LIT('a')), (25, LIT('BCD')), (30, LIT('Some_Name')),
        (41, LIT('foo_xbaa')), (54, 0), (56, 1), (59, -2), (62, 0.5),
        (65, 1.234), (71, b'abc'), (77, b''), (80, b'abc ( def ) ghi'),
        (98, b'def \x00 4ghi'), (118, b'bach\\slask'), (132, b'foo\nbaa'),
        (143, b'this % is not a comment.'),
        (170, b'foo\nbaa'), (180, b'foobaa'),
        (191, b''), (194, b' '), (199, b'@@ '),
        (211, b'\xab\xcd\x00\x124\x05'),
        (230, LIT('a')), (232, LIT('b')), (234, [b'c']), (246, [1, b'z']),
        (258, {'foo': b'bar'}),
    ]

    def get_tokens(self, s):
        from io import BytesIO

        class MyParser(PSBaseParser):
            def flush(self):
                self.add_results(*self.popall())

        parser = MyParser(BytesIO(s))
        r = []
        try:
            while 1:
                r.append(parser.nexttoken())
        except PSEOF:
            pass
        return r

    def get_objects(self, s):
        from io import BytesIO

        class MyParser(PSStackParser):
            def flush(self):
                self.add_results(*self.popall())

        parser = MyParser(BytesIO(s))
        r = []
        try:
            while 1:
                r.append(parser.nextobject())
        except PSEOF:
            pass
        return r

    def test_1(self):
        tokens = self.get_tokens(self.TESTDATA)
        print(tokens)
        self.assertEqual(tokens, self.TOKENS)
        return

    def test_2(self):
        objs = self.get_objects(self.TESTDATA)
        print(objs)
        self.assertEqual(objs, self.OBJS)
        return


class TestCCITTG4Parser(unittest.TestCase):

    def get_parser(self, bits):
        parser = CCITTG4Parser(len(bits))
        parser._curline = [int(c) for c in bits]
        parser._reset_line()
        return parser

    def test_b1(self):
        parser = self.get_parser('00000')
        parser._do_vertical(0)
        self.assertEqual(parser._curpos, 0)
        return

    def test_b2(self):
        parser = self.get_parser('10000')
        parser._do_vertical(-1)
        self.assertEqual(parser._curpos, 0)
        return

    def test_b3(self):
        parser = self.get_parser('000111')
        parser._do_pass()
        self.assertEqual(parser._curpos, 3)
        self.assertEqual(parser._get_bits(), '111')
        return

    def test_b4(self):
        parser = self.get_parser('00000')
        parser._do_vertical(+2)
        self.assertEqual(parser._curpos, 2)
        self.assertEqual(parser._get_bits(), '11')
        return

    def test_b5(self):
        parser = self.get_parser('11111111100')
        parser._do_horizontal(0, 3)
        self.assertEqual(parser._curpos, 3)
        parser._do_vertical(1)
        self.assertEqual(parser._curpos, 10)
        self.assertEqual(parser._get_bits(), '0001111111')
        return

    def test_e1(self):
        parser = self.get_parser('10000')
        parser._do_vertical(0)
        self.assertEqual(parser._curpos, 1)
        parser._do_vertical(0)
        self.assertEqual(parser._curpos, 5)
        self.assertEqual(parser._get_bits(), '10000')
        return

    def test_e2(self):
        parser = self.get_parser('10011')
        parser._do_vertical(0)
        self.assertEqual(parser._curpos, 1)
        parser._do_vertical(2)
        self.assertEqual(parser._curpos, 5)
        self.assertEqual(parser._get_bits(), '10000')
        return

    def test_e3(self):
        parser = self.get_parser('011111')
        parser._color = 0
        parser._do_vertical(0)
        self.assertEqual(parser._color, 1)
        self.assertEqual(parser._curpos, 1)
        parser._do_vertical(-2)
        self.assertEqual(parser._color, 0)
        self.assertEqual(parser._curpos, 4)
        parser._do_vertical(0)
        self.assertEqual(parser._curpos, 6)
        self.assertEqual(parser._get_bits(), '011100')
        return

    def test_e4(self):
        parser = self.get_parser('10000')
        parser._do_vertical(0)
        self.assertEqual(parser._curpos, 1)
        parser._do_vertical(-2)
        self.assertEqual(parser._curpos, 3)
        parser._do_vertical(0)
        self.assertEqual(parser._curpos, 5)
        self.assertEqual(parser._get_bits(), '10011')
        return

    def test_e5(self):
        parser = self.get_parser('011000')
        parser._color = 0
        parser._do_vertical(0)
        self.assertEqual(parser._curpos, 1)
        parser._do_vertical(3)
        self.assertEqual(parser._curpos, 6)
        self.assertEqual(parser._get_bits(), '011111')
        return

    def test_e6(self):
        parser = self.get_parser('11001')
        parser._do_pass()
        self.assertEqual(parser._curpos, 4)
        parser._do_vertical(0)
        self.assertEqual(parser._curpos, 5)
        self.assertEqual(parser._get_bits(), '11111')
        return

    def test_e7(self):
        parser = self.get_parser('0000000000')
        parser._curpos = 2
        parser._color = 1
        parser._do_horizontal(2, 6)
        self.assertEqual(parser._curpos, 10)
        self.assertEqual(parser._get_bits(), '1111000000')
        return

    def test_e8(self):
        parser = self.get_parser('001100000')
        parser._curpos = 1
        parser._color = 0
        parser._do_vertical(0)
        self.assertEqual(parser._curpos, 2)
        parser._do_horizontal(7, 0)
        self.assertEqual(parser._curpos, 9)
        self.assertEqual(parser._get_bits(), '101111111')
        return

    def test_m1(self):
        parser = self.get_parser('10101')
        parser._do_pass()
        self.assertEqual(parser._curpos, 2)
        parser._do_pass()
        self.assertEqual(parser._curpos, 4)
        self.assertEqual(parser._get_bits(), '1111')
        return

    def test_m2(self):
        parser = self.get_parser('101011')
        parser._do_vertical(-1)
        parser._do_vertical(-1)
        parser._do_vertical(1)
        parser._do_horizontal(1, 1)
        self.assertEqual(parser._get_bits(), '011101')
        return

    def test_m3(self):
        parser = self.get_parser('10111011')
        parser._do_vertical(-1)
        parser._do_pass()
        parser._do_vertical(1)
        parser._do_vertical(1)
        self.assertEqual(parser._get_bits(), '00000001')
        return

class TestUtilities(unittest.TestCase):

    def test_url_basic(self):
        test_url = url("testsite.com/search?", name="John", lastname="Doe", age="25")
        self.assertEqual(test_url, "testsite.com/search?name=John&lastname=Doe&age=25")

    def test_url_special_characters(self):
        test_url = url("testsite.com/search?", name="Äööl_&==??!!  ")
        self.assertEqual(True, False)

if __name__ == '__main__':
    unittest.main()
