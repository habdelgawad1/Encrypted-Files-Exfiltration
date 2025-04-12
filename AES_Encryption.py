from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from AES_Key_Generation import load_key_and_iv

def encrypt_file(file_path, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    with open(file_path, 'rb') as f:
        plaintext = f.read()

    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(plaintext) + padder.finalize()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    with open(r"/home/hgawad/Desktop/coursework/encrypted_files.log", 'wb') as f:
        f.write(ciphertext + ".enc")

def encrypt_files_from_list(file_list_path,key,iv):
    with open(file_list_path, "r") as f:
        files = [line.strip() for line in f if line.strip()]
        
    for file_path in files:
            encrypt_file(file_path, key, iv)
            
    print(f"Encryption completed for files listed in {file_list_path}")

key, iv = load_key_and_iv(r"/home/hgawad/Desktop/coursework/aes_key.txt")
encrypt_files_from_list(r"/home/hgawad/Desktop/coursework/files.log", key, iv)