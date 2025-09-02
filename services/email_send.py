import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from emails import getEmails
load_dotenv()
from_addr = os.getenv("SMTP_USERNAME")
smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
smtp_port = int(os.getenv("SMTP_PORT", 587))
smtp_username = os.getenv("SMTP_USERNAME", from_addr)
smtp_password = os.getenv("SMTP_PASSWORD")


def sendEmails(body):
    
    to_addr = getEmails()
    subject = 'As 5 melhores ideias de SAAS da semana'
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))

    

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(smtp_username, smtp_password)
    try:
        server.sendmail(from_addr, to_addr.split(','), msg.as_string())
    except ValueError:
        print(f'erro: {ValueError}')
    finally:
        server.quit()
    return



        
