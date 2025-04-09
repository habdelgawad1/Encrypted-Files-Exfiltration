from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

def generate_key_and_iv(key_size=32, iv_size=16):
    # Generate a random key and IV
    key = os.urandom(key_size)
    iv = os.urandom(iv_size)
    return key, iv

def encrypt_file(file_path, key, iv):
    # Create a cipher object using the key and IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Read the plaintext from the file
    with open(file_path, 'rb') as f:
        plaintext = f.read()

    # Pad the plaintext to be a multiple of the block size
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    # Encrypt the padded data
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Write the ciphertext to a new file
    with open(file_path + '.enc', 'wb') as f:
        f.write(ciphertext)

def encrypt_files_from_list(file_list_path,key,iv):
    with open(file_list_path, "r") as f:
        files = [line.strip() for line in f if line.strip()]
        
    for file_path in files:
            encrypt_file(file_path, key, iv)
            
    print(f"Encryption completed for files listed in {file_list_path}")

def write_key_and_iv_to_file(key, iv, file_path):
    # Write the key and IV to a text file
    with open(file_path, "w") as f:
        f.write(f"AES Key: {key.hex()}\n")
        f.write(f"AES IV: {iv.hex()}\n")

key, iv = generate_key_and_iv()
print(f"AES Key: {key.hex()}")
print(f"AES IV: {iv.hex()}")
write_key_and_iv_to_file(key, iv, r"/home/hgawad/Desktop/coursework/AES_key.txt")
encrypt_files_from_list(r"/home/hgawad/Desktop/coursework/files.log", key, iv)

        