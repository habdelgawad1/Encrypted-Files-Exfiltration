import base64 as b

def a(x, e, n):
    d = int.from_bytes(x, byteorder='big')
    return [pow(d, e, n)]

def b1(f):
    with open(f, "rb") as x:
        return x.read(16)

def c1(k, e, n):
    enc = a(k, e, n)
    with open(b.b64decode("YWVzX2tleS5iaW4=").decode(), "wb") as x:
        for v in enc:
            x.write(v.to_bytes((v.bit_length() + 7) // 8, byteorder='big'))

def d1(f=b.b64decode("cnNhX2tleXMudHh0").decode()):
    with open(f, "r") as x:
        l = x.readlines()
        e, n = map(int, l[0].split(":")[1].split(","))
        d, _ = map(int, l[1].split(":")[1].split(","))
        return (e, d, n)

e, d, n = d1()
k = b1(b.b64decode("YWVzX2tleS50eHQ=").decode())
c1(k, e, n)
print(b.b64decode("UlNBIEVuY3J5cH R0aW9uIERvbmUgc3VjY2Vz c2Z1bGx5").decode())
