def rsa_decrypt_bytes(encrypted, d, n):
    decrypted = pow(encrypted, d, n)
    decrypted = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, byteorder='big')
    return decrypted

def load_encrypted_aes_keys(filename):
    with open(filename, 'rb') as f:
        encrypted_data = f.read()
        
    encrypted_keys = []
    for i in range(0, len(encrypted_data), 4):
        encrypted_int = int.from_bytes(encrypted_data[i:i+4], byteorder='big')
        encrypted_keys.append(encrypted_int)
    return encrypted_keys

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
encrypted_key = load_encrypted_aes_keys('aes_key.bin')
decrypted_key = b''.join(rsa_decrypt_bytes(key, d, n) for key in encrypted_key)
print("RSA Decryption Done Successfully")
