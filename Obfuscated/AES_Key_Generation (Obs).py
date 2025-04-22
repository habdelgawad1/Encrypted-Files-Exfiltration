import random as r
import base64 as b

def a():
    x = bytearray(r.getrandbits(8) for _ in range(32))
    return b.b64encode(x).decode()

def b1(x, y=b.b64decode("YWVzX2tleS50eHQ=").decode()):
    with open(y, "w") as z:
        z.write(x)

def c1(y=b.b64decode("L2hvbWUvaGdhd2FkL0Rlc2t0b3AvY291cnNld29yay9hZXNfa2V5LnR4dA==").decode()):
    with open(y, "r") as z:
        return z.read().strip()

d = a()
b1(d)
print(b.b64decode("R2VuZXJhdGVkIEtleTog").decode() + d)
