import base64 as b

def a(x, d, n):
    d = pow(x, d, n)
    return d.to_bytes((d.bit_length() + 7) // 8, byteorder='big')

def b1(f):
    with open(f, 'rb') as x:
        d = x.read()
    r = []
    for i in range(0, len(d), 4):
        r.append(int.from_bytes(d[i:i + 4], byteorder='big'))
    return r

def c1(f=b.b64decode("cnNhX2tleXMudHh0").decode()):
    with open(f, "r") as x:
        l = x.readlines()
        e, n = map(int, l[0].split(":")[1].split(","))
        d, _ = map(int, l[1].split(":")[1].split(","))
        return (e, d, n)

e, d, n = c1()
e_k = b1(b.b64decode("YWVzX2tleS5iaW4=").decode())
d_k = b''.join(a(k, d, n) for k in e_k)
print(b.b64decode("UlNBIERlY3J5cH R0aW9uIERvbmUgc3VjY2Vz c2Z1bGx5").decode())
