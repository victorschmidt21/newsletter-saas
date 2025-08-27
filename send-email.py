import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

from_addr = os.getenv("SMTP_USERNAME")
to_addr = 'naoseivtx@icloud.com'
subject = 'Assunto do Email'
body = 'Corpo do Email'

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
smtp_port = int(os.getenv("SMTP_PORT", 587))
smtp_username = os.getenv("SMTP_USERNAME", from_addr)
smtp_password = os.getenv("SMTP_PASSWORD")

server = smtplib.SMTP(smtp_server, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(smtp_username, smtp_password)
try:
    server.sendmail(from_addr, to_addr, msg.as_string())
except ValueError:
    print(ValueError)
finally:
    server.quit()

        
