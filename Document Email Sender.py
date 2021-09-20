import smtplib

import os

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

email_address = os.environ.get("user1")
email_pass = os.environ.get("pass1")

msg = MIMEMultipart()
msg["From"] = email_address
msg["To"] = "victormerida55@gmail.com"


desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
os.chdir(desktop)


file = input("file name +  .docx (word) or .pdf :  ")
msg["Subject"] = file
attachment = open(file,"rb")
part = MIMEBase("application","octect-stream")
part.set_payload(attachment.read())
encoders.encode_base64(part)
msg.attach(part)

with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
    smtp.login(email_address,email_pass)
    smtp.send_message(msg)

print("The email has been sent")






