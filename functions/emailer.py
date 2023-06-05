from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib


def send_email(email, subject, text):
    message = MIMEMultipart()
    message["from"] = "SIMPLIC MC"
    message["to"] = email
    message["subject"] = subject
    message.attach(MIMEText(text))

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        # smtp.login("info@simplicmc.se", "Potta-321")
        smtp.login("leohansson93@gmail.com", "Jaja1234")
        smtp.send_message(message)
        print(f"Email sent to {email}")


send_email('steven.meesters@gmail.com', 'tester', 'testerdd')
