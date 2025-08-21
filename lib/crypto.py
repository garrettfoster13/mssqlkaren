from Crypto.Cipher import AES,DES3
from hashlib import *
import binascii  
import math

def aes_des_key_derivation(password):
    
    key_sha1 = sha1(password).digest()
    
    b0 = b""
    for x in key_sha1:
        b0 += bytes((x ^ 0x36,))
        
    b1 = b""
    for x in key_sha1:
        b1 += bytes((x ^ 0x5c,))

    b0 += b"\x36"*(64 - len(b0))
    b1 += b"\x5c"*(64 - len(b1))
        
    b0_sha1 = sha1(b0).digest()
    b1_sha1 = sha1(b1).digest()
    
    return b0_sha1 + b1_sha1 
    
def _3des_decrypt(data,key):

    _3des = DES3.new(key, DES3.MODE_CBC, b"\x00"*8)
    decrypted = _3des.decrypt(data)
    return decrypted.decode("utf-16-le")
    
def deobfuscate_credential_string(credential_string):
    key_data = binascii.unhexlify(credential_string[8:88])
    encrypted_data = binascii.unhexlify(credential_string[128:])

    key = aes_des_key_derivation(key_data)
    last_16 = math.floor(len(encrypted_data)/8)*8
    return _3des_decrypt(encrypted_data[:last_16],key[:24])