import random as r
import math as m
import base64 as b

def a(x):
    if x < 2:
        return False
    for i in range(2, int(m.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def b1(x, y):
    while y:
        x, y = y, x % y
    return x

def c1(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0
    return x1 % m0

def d1():
    p = r.randint(1000, 5000)
    while not a(p):
        p = r.randint(1000, 10000)

    q = r.randint(1000, 5000)
    while not a(q) or q == p:
        q = r.randint(1000, 10000)

    n = p * q
    ph = (p - 1) * (q - 1)

    e = 65537
    if b1(e, ph) != 1:
        e = 3
        while b1(e, ph) != 1:
            e += 2

    d = c1(e, ph)
    return (e, d, n)

def e1(e, d, n, f=b.b64decode("cnNhX2tleXMudHh0").decode()):
    with open(f, "w") as x:
        x.write(f"{b.b64decode('UHVibGljIEtleSAoZSwgbik6').decode()} {e}, {n}\n")
        x.write(f"{b.b64decode('UHJpdmF0ZSBLZXkgKGQsIG4pOg==').decode()} {d}, {n}\n")

def f1(f=b.b64decode("cnNhX2tleXMudHh0").decode()):
    with open(f, "r") as x:
        l = x.readlines()
        e, n = map(int, l[0].split(":")[1].split(","))
        d, _ = map(int, l[1].split(":")[1].split(","))
        return (e, d, n)

e, d, n = d1()
print(f"{b.b64decode('R2VuZXJhdGVkIEtleXM6').decode()} {e}, {d}, {n}")
e1(e, d, n)
