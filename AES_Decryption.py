import base64

def unpad(padded_data):
    padding_len = padded_data[-1]
    return padded_data[:-padding_len]

def decrypt_block(block, key):
    decrypted = bytearray(len(block))
    for i in range(len(block)):
        decrypted[i] = block[i] ^ key[i % len(key)]
    return decrypted

def decrypt_file(key, input_file, output_file):
    with open(input_file, "rb") as f:
        ciphertext = f.read()
    
    plaintext = bytearray()
    for i in range(0, len(ciphertext), 16):
        block = ciphertext[i:i + 16]
        decrypted_block = decrypt_block(block, key)
        plaintext.extend(decrypted_block)
    
    plaintext = unpad(plaintext)
    
    with open(output_file, "wb") as f:
        f.write(plaintext)

def load_aes_key(filename="/home/hgawad/Desktop/coursework/aes_key.txt"):
    with open(filename, "r") as key_file:
        key = key_file.read().strip()
    return key

encrypted_files_log = r"/home/hgawad/Desktop/coursework/encrypted_files.log"
key = base64.b64decode(load_aes_key())

with open(encrypted_files_log, "r") as log:
    for line in log:
        encrypted_file_path = line.strip()
        original_extension_start = encrypted_file_path[:-4].rfind(".")
        original_extension = encrypted_file_path[original_extension_start+1:-4]
        decrypted_file_path = encrypted_file_path[:-4] + "." + original_extension
        decrypt_file(key, encrypted_file_path, decrypted_file_path)
        
print("AES Decryption Done Successfully")

