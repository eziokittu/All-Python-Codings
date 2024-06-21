import time

# Additive / Shift Cypher Emcryption
def encrypt(message, key):
    cipherText = ""
    for i in message:
        # charIsUpper = 0
        # if (i.isupper()):
        #     i = i.lower()
        #     charIsUpper = 1
        cipherText += (( (ascii(i)-ascii('a')) + key ) % 26 ) + ascii('a')
    return cipherText

def decrypt(cipherText, key):
    message = ""
    for i in cipherText:
        x = ( (ascii(i)-ascii('a')) - key )
        if (x<0):
            x = 26+x
        message += x + ascii('a')
    return message

print(encrypt("hello", 1))