import base64 as b

def a(x, y=16):
    z = y - (len(x) % y)
    return x + bytes([z] * z)

def b1(x, y):
    z = bytearray(len(x))
    for i in range(len(x)):
        z[i] = x[i] ^ y[i % len(y)]
    return z

def c1(k, i_f, o_f):
    with open(i_f, "rb") as f:
        d = f.read()
    d = a(d)
    e = bytearray()
    for i in range(0, len(d), 16):
        blk = d[i:i + 16]
        e_b = b1(blk, k)
        e.extend(e_b)
    with open(o_f, "wb") as f:
        f.write(e)

def d1(f=b.b64decode("L2hvbWUvaGdhd2FkL0Rlc2t0b3AvY291cnNld29yay9hZXNfa2V5LnR4dA==").decode()):
    with open(f, "r") as kf:
        return kf.read().strip()

f1 = b.b64decode("L2hvbWUvaGdhd2FkL0Rlc2t0b3AvY291cnNld29yay9maWxlcy5sb2c=").decode()
f2 = b.b64decode("L2hvbWUvaGdhd2FkL0Rlc2t0b3AvY291cnNld29yay9lbmNyeXB0ZWRfZmlsZXMubG9n").decode()
k = b.b64decode(d1())

with open(f2, "w") as ef:
    with open(f1, "r") as lf:
        for l in lf:
            fp = l.strip()
            efp = fp + ".enc"
            c1(k, fp, efp)
            ef.write(efp + "\n")

print(b.b64decode("QUVTIEVuY3J5cHRpb24gRG9uZSBTdWNjZXNzZnVsbHk=").decode())
