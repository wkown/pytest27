# -*- coding:utf-8 -*-
from Crypto.Cipher import AES

__author__ = 'walkskyer'

# pad unpad
BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]


# Encryption
encryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
cipher_text = encryption_suite.encrypt(pad("A really secret message. Not for prying eyes."))
print cipher_text
print cipher_text.encode('hex')

# Decryption
decryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
plain_text = decryption_suite.decrypt(cipher_text)
print plain_text
print unpad(plain_text)