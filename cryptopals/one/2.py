import binascii
import codecs

def xor(b1, b2):
    d1 = binascii.unhexlify(b1)
    d2 = binascii.unhexlify(b2)
    o = ''
    for i in range(len(d1)):
        o += chr(d1[i] ^ d2[i])
    # o = ''.join([chr(d1[i] ^ d2[i]) for i in range(len(d1))])
    return codecs.encode(o.encode(), 'hex')

b1 = '1c0111001f010100061a024b53535009181c'
b2 = '686974207468652062756c6c277320657965'
expected = '746865206b696420646f6e277420706c6179'
res = xor(b1, b2)

print(res, expected)

if res != expected:
    raise Exception(res + ' != ' + expected)
