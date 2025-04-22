import os

def A():
    B = []
    C = [".txt", ".docx", ".jpg"]
    D = os.path.dirname(os.path.abspath(__file__))

    for E, F, G in os.walk(D):
        for H in G:
            if any(H.lower().endswith(I) for I in C):
                J = os.path.join(E, H)
                B.append(J)

    K = os.path.join(D, "files.log")  
    with open(K, "w") as L:
        for M in B:
            L.write(M + "\n")

    print(f"{len(B)} files found and logged in {K}")

A()
