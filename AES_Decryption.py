from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from AES_Key_Generation import load_key_and_iv
import os

def decrypt_file(file_path, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    with open(file_path, 'rb') as f:
        ciphertext = f.read()

    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    output_path = file_path.replace(".enc", ".dec")
    with open(output_path, 'wb') as f:
        f.write(plaintext)

def decrypt_files_from_list(file_list_path, key, iv):
    with open(file_list_path, "r") as f:
        files = [line.strip() for line in f if line.strip()]
        
    for file_path in files:
        enc_file = file_path + ".enc"
        decrypt_file(enc_file, key, iv)

key, iv = load_key_and_iv(r"/home/hgawad/Desktop/coursework/aes_key.txt")
decrypt_files_from_list(r"/home/hgawad/Desktop/coursework/files.log", key, iv)
    