# -*- coding:utf-8 -*-
__author__ = 'walkskyer'

from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64

# 伪随机数生成器
random_generator = Random.new().read
# rsa算法生成实例
rsa = RSA.generate(1024, random_generator)

# master的秘钥对的生成
private_pem = rsa.exportKey()

with open('master-private.pem', 'w') as f:
    f.write(private_pem)

public_pem = rsa.publickey().exportKey()
with open('master-public.pem', 'w') as f:
    f.write(public_pem)

# ghost的秘钥对的生成
private_pem = rsa.exportKey()
with open('ghost-private.pem', 'w') as f:
    f.write(private_pem)

public_pem = rsa.publickey().exportKey()
with open('ghost-public.pem', 'w') as f:
    f.write(public_pem)


# Master使用Ghost的公钥对内容进行rsa 加密

message = 'hello ghost, this is a plian text'
with open('ghost-public.pem') as f:
      key = f.read()
      rsakey = RSA.importKey(key)
      cipher = Cipher_pkcs1_v1_5.new(rsakey)
      encrypt_text = base64.b64encode(cipher.encrypt(message))
      print 'encrypt_text:', encrypt_text

# Ghost使用自己的私钥对内容进行rsa 解密

with open('ghost-private.pem') as f:
     key = f.read()
     rsakey = RSA.importKey(key)
     cipher = Cipher_pkcs1_v1_5.new(rsakey)
     text = cipher.decrypt(base64.b64decode(encrypt_text), random_generator)

print 'text:', text

# Master 使用自己的私钥对内容进行签名
with open('master-private.pem') as f:
     key = f.read()
     rsakey = RSA.importKey(key)
     signer = Signature_pkcs1_v1_5.new(rsakey)
     digest = SHA.new()
     digest.update(message)
     sign = signer.sign(digest)
     signature = base64.b64encode(sign)
print 'signature:', signature

#验签
with open('master-public.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    verifier = Signature_pkcs1_v1_5.new(rsakey)
    digest = SHA.new()
    # Assumes the data is base64 encoded to begin with
    digest.update(message)
    is_verify = verifier.verify(digest, base64.b64decode(signature))
    print 'is_verify:', is_verify


if __name__ == "__main__":
    pass