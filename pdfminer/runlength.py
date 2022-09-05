#!/usr/bin/env python
#
# RunLength decoder (Adobe version) implementation based on PDF Reference
# version 1.4 section 3.3.4.
#
#  * public domain *
#

def rldecode(data):
    decoded = b''
    i = 0
    while i < len(data):
        # print('data[%d]=:%d:' % (i,ord(data[i])))
        length = data[i]
        if length == 128:
            break
        if length >= 0 and length < 128:
            run = data[i + 1:(i + 1) + (length + 1)]
            # print('length=%d, run=%s' % (length+1,run))
            decoded += run
            i = (i + 1) + (length + 1)
        if length > 128:
            run = data[i + 1:i + 2] * (257 - length)
            # print('length=%d, run=%s' % (257-length,run))
            decoded += run
            i = (i + 1) + 1
    return decoded
