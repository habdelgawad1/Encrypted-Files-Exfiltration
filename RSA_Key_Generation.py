import random
import math

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

def write_rsa_keys(e, d, n, filename="rsa_keys.txt"):
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
            
            return (e, d, n)
            
e,d,n = generate_keys()
print(f"Generated Keys: {e}, {d}, {n}")
write_rsa_keys(e, d, n)
