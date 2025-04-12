from RSA_Key_Generation import load_rsa_keys

def rsa_encrypt_bytes(byte_data, e, n):
    data=int.from_bytes(byte_data, byteorder='big')
    encrypted_data=pow(data, e, n)
    return [encrypted_data]

def load_aes_key(aes_key_file):
    with open(aes_key_file, "rb") as f:
        aes_key = f.read(16)
    return aes_key

def write_encrypted_aes_key(aes_key, e, n):
    encrypted_key = rsa_encrypt_bytes(aes_key, e, n)
    with open("aes_key.bin", "w") as f:
        for value in encrypted_key:
            f.write(str(value) + "\n")

e, d, n = load_rsa_keys()
print(f"Public key (e, n): ({e}, {n})")
print(f"Private key (d, n): ({d}, {n})")

