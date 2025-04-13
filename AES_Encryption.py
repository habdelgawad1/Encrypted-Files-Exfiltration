import base64

def pad(data, block_size=16):
    padding_len = block_size - (len(data) % block_size)
    return data + bytes([padding_len] * padding_len)

def encrypt_block(block, key):
    encrypted = bytearray(len(block))
    for i in range(len(block)):
        encrypted[i] = block[i] ^ key[i % len(key)]  
    return encrypted

def encrypt_file(key, input_file, output_file):
    with open(input_file, "rb") as f:
        plaintext = f.read()
    padded_plaintext = pad(plaintext)
    ciphertext = bytearray()
    for i in range(0, len(padded_plaintext), 16):
        block = padded_plaintext[i:i + 16]
        encrypted_block = encrypt_block(block, key)
        ciphertext.extend(encrypted_block)
    with open(output_file, "wb") as f:
        f.write(ciphertext)

def load_aes_key(filename="/home/hgawad/Desktop/coursework/aes_key.txt"):
    with open(filename, "r") as key_file:
        key = key_file.read().strip()
    return key
    
files_log = r"/home/hgawad/Desktop/coursework/files.log"
encrypted_files_log = r"/home/hgawad/Desktop/coursework/encrypted_files.log"
key = base64.b64decode(load_aes_key())  

with open(encrypted_files_log, "w") as encrypted_log:
    with open(files_log, "r") as log:
        for line in log:
            file_path = line.strip()
            encrypted_file_path = file_path + ".enc"
            encrypt_file(key, file_path, encrypted_file_path)
            encrypted_log.write(encrypted_file_path + "\n")
            
print("AES Encryption Done Successfully")
