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


def aes256_decrypt(data,key,iv=b"\x00"*16):

    aes256 = AES.new(key, AES.MODE_CBC, iv)
    decrypted = aes256.decrypt(data)
    return decrypted.decode("utf-16-le")


    #thx @blurbdust https://github.com/blurbdust/PXEThief/blob/6d21293465959796c629e0a3517f1bb1655289b0/media_variable_file_cryptography.py#L80
def credential_string_algo(credential_string):
    hash_type = ""
    algo_bytes = credential_string[112:116]
    if algo_bytes == "1066":
        hash_type = "aes256"
    elif algo_bytes == "0366":
        hash_type = "3des"
    return hash_type
    
def deobfuscate_credential_string(credential_string):
    
    algo = credential_string_algo(credential_string)
    
    key_data = binascii.unhexlify(credential_string[8:88])
    encrypted_data = binascii.unhexlify(credential_string[128:])

    key = aes_des_key_derivation(key_data)
    last_16 = math.floor(len(encrypted_data)/8)*8

    if algo == "3des":
        last_16 = math.floor(len(encrypted_data)/8)*8
        return _3des_decrypt(encrypted_data[:last_16], key[:24])
    elif algo == "aes256":
        last_16 = math.floor(len(encrypted_data)/16)*16 
        return aes256_decrypt(encrypted_data[:last_16], key[:32])




