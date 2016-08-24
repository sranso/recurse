import base64
import binascii

def hex_to_base64(s):
    decoded = binascii.unhexlify(s)
    return base64.b64encode(decoded)

hex_val = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
expected = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
res = hex_to_base64(hex_val)

print(res, expected)

if res != expected:
    raise Exception(res + ' != ' + expected)
