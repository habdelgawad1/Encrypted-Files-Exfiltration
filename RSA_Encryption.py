def rsa_encrypt_bytes(byte_data, e, n):
    data = int.from_bytes(byte_data, byteorder='big')
    encrypted_data = pow(data, e, n)
    return [encrypted_data]

def load_aes_key(aes_key_file):
    with open(aes_key_file, "rb") as f:
        aes_key = f.read(16)
    return aes_key

def write_encrypted_aes_key(aes_key, e, n):
    encrypted_key = rsa_encrypt_bytes(aes_key, e, n)
    
    with open("aes_key.bin", "wb") as f:
        for value in encrypted_key:
            f.write(value.to_bytes((value.bit_length() + 7) // 8, byteorder='big'))

def load_rsa_keys(filename="rsa_keys.txt"):
    """Loads RSA keys (e, d, n) from a file."""
    with open(filename, "r") as f:
            lines = f.readlines()
            public_key_line = lines[0].strip()
            e_str, n_str = public_key_line.split(":")[1].split(",")
            e = int(e_str.strip())
            n = int(n_str.strip())
            
            # Extract private key (d, n)
            private_key_line = lines[1].strip()
            d_str, n_str = private_key_line.split(":")[1].split(",")
            d = int(d_str.strip())
            
            return (e, d, n)
            
e, d, n = load_rsa_keys()
aes_key = load_aes_key("aes_key.txt")
write_encrypted_aes_key(aes_key, e, n)
print("RSA Encryption Done Successfully")

