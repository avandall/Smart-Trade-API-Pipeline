import os
from email.message import EmailMessage
import smtplib
import mimetypes

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(subject: str, body: str, to: str, file_path: str= None):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to
    msg.set_content(body)

    if file_path and os.path.exists(file_path):
        mimetype, _ = mimetypes.guess_type(file_path)
        if mimetype is None:
            mimetype = 'application/octet-stream'
        
        maintype, subtype = mimetype.split('/', 1)
        with open(file_path, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(file_path)
            msg.add_attachment(
                file_data,
                maintype = maintype,
                subtype = subtype,
                filename = file_name
            )

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)