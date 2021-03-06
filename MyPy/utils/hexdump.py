"""
Hexdump for Packets

Snippets from http://code.activestate.com/recipes/142812-hex-dumper/
"""

FILTER=''.join([(len(repr(chr(x)))==3) and chr(x) or '.' for x in range(256)])

def hexdump(src, length=0x10):
    N = 0; result = ''
    while src:
        s, src = src[:length], src[length:]
        hexa = ' '.join(["%02X" % ord(x) for x in s])
        s = s.translate(FILTER)
        result += "%08X   %-*s   |%s|\n" % (N, length*3, hexa, s)
        N += length
    return result