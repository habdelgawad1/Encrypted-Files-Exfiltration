import random
import math
import os

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def eed(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 % m0

def generate_keys():
    p = random.randint(1000, 5000)
    while not is_prime(p):
        p = random.randint(1000, 10000)

    q = random.randint(1000, 5000)
    while not is_prime(q) or q == p:
        q = random.randint(1000, 10000)

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 65537
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2

    d = eed(e, phi)
    return (e, d, n)

def write_keys(e, d, n, filename="rsa_keys.txt"):
    """Saves RSA keys to a file for later use."""
    with open(filename, "w") as f:
        f.write(f"Public Key (e, n): {e}, {n}\n")
        f.write(f"Private Key (d, n): {d}, {n}\n")

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
            n_priv = int(n_str.strip())
            
            return (e, d, n)
   

def rsa_encrypt_bytes(byte_data, e, n):
    """Encrypts each byte of data using RSA"""
    return [(b ** e) % n for b in byte_data]

def rsa_decrypt_bytes(encrypted_data, d, n):
    return bytes([(c ** d) % n for c in encrypted_data])

# Step 1: Generate RSA key pair
e, d, n = generate_keys()
print(f"Public key (e, n): ({e}, {n})")
print(f"Private key (d, n): ({d}, {n})")


# Step 2: Read 16 bytes from AES.txt
aes_key_file = "AES.txt"
with open(aes_key_file, "rb") as f:
    aes_key = f.read(16)

if len(aes_key) != 16:
    raise ValueError("File must contain exactly 16 bytes for AES-128 key.")

print(f"\nOriginal AES Key (hex): {aes_key.hex()}")

# Step 3: Encrypt AES key using RSA
encrypted_key = rsa_encrypt_bytes(aes_key, e, n)

# Step 4: Save encrypted key to AES_key.txt.enc
with open("AES_key.txt.enc", "w") as f:
    for value in encrypted_key:
        f.write(str(value) + "\n")

print("\n🔐 AES key encrypted and saved to AES_key.txt.enc")
