import random
import base64

def generate_key():
    key = bytearray(random.getrandbits(8) for _ in range(32))
    return base64.b64encode(key).decode()

def write_aes_key(key, filename="aes_key.txt"):
    with open(filename, "w") as key_file:
        key_file.write(key)
    
key = generate_key()
write_aes_key(key)
print(f"Generated Key: {key}")