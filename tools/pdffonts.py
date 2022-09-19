import sys
from typing import List, Set, Tuple

from pdfminer.converter import FontExtractor
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage


def usage(command: str = "pdffonts"):
    print(f"usage: {command} input.pdf ...")


def get_fontnames(filenames: List[str]) -> Set[Tuple[str, str]]:
    fontnames = set()
    for fname in filenames:
        with open(fname, 'rb') as fp:
            rsrcmgr = PDFResourceManager()
            device = FontExtractor(rsrcmgr)
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.get_pages(fp):
                interpreter.process_page(page)
                fontnames.update(device.get_fontnames())
        device.close()
    return fontnames


def print_fontnames(fontnames: Set[Tuple[str, str]]):
    table: List[Tuple[str, str]] = [
        ('Font', 'Type'),
        ('----------------------', '----------------------')
        ]
    table = table + list(fontnames)
    for row in table:
        print("{:<40} {:<20}".format(*row))


def main(argv: List[str]):
    if len(argv) <= 1:
        usage(argv[0])
    else:
        fontnames = get_fontnames(argv[1:])
        print_fontnames(fontnames)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
