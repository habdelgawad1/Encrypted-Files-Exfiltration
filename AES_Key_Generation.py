import os

def generate_key_and_iv(key_size=32, iv_size=16):
    # Generate a random key and IV
    key = os.urandom(key_size)
    iv = os.urandom(iv_size)
    return key, iv

def write_key_and_iv_to_file(key, iv, file_path):
    with open(file_path, "w") as f:
        f.write(f"AES Key: {key.hex()}\n")
        f.write(f"AES IV: {iv.hex()}\n")

def load_key_and_iv(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()
        key = bytes.fromhex(lines[0].strip().split(": ")[1])
        iv = bytes.fromhex(lines[1].strip().split(": ")[1])
        return key, iv


key, iv = generate_key_and_iv()
write_key_and_iv_to_file(key, iv, r"/home/hgawad/Desktop/coursework/aes_key.txt")