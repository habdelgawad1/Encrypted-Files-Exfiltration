from RSA_Key_Generation import load_rsa_keys

def rsa_decrypt_bytes(encrypted,d,n):
    decrypted = pow(encrypted, d, n)
    decrypted = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, byteorder='big')
    return decrypted

def load_encrypted_aes_keys(filename):
    with open(filename, 'rb') as f:
        encrypted_aes_key = f.read()
    return encrypted_aes_key

e,d,n= load_rsa_keys('rsa_keys.txt')
encrypted_key= load_encrypted_aes_keys('aes_key.bin')
decrypted_key= rsa_decrypt_bytes(encrypted_key,d,n)
