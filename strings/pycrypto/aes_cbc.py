# -*- coding:utf-8 -*-
from Crypto.Cipher import AES
import base64

__author__ = 'walkskyer'

# pad unpad
BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]

key = 'This is a key123'
iv = 'This is an IV456'

data = 'A really secret message. Not for prying eyes.'


# Encryption
encryption_suite = AES.new(key, AES.MODE_CBC, iv)
cipher_text = encryption_suite.encrypt(pad(data))
print cipher_text
print base64.b64encode(cipher_text)

# Decryption
decryption_suite = AES.new(key, AES.MODE_CBC, iv)
plain_text = decryption_suite.decrypt(cipher_text)
print plain_text
print unpad(plain_text)