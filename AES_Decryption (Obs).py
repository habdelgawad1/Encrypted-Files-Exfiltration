import base64 as b

def a(x):
    return x[:-x[-1]]

def b1(x, y):
    z = bytearray(len(x))
    for i in range(len(x)):
        z[i] = x[i] ^ y[i % len(y)]
    return z

def c1(k, i_f, o_f):
    with open(i_f, "rb") as f:
        d = f.read()
    p = bytearray()
    for i in range(0, len(d), 16):
        blk = d[i:i + 16]
        p.extend(b1(blk, k))
    p = a(p)
    with open(o_f, "wb") as f:
        f.write(p)

def d1(f=b.b64decode("L2hvbWUvaGdhd2FkL0Rlc2t0b3AvY291cnNld29yay9hZXNfa2V5LnR4dA==").decode()):
    with open(f, "r") as kf:
        return kf.read().strip
