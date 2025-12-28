import smtplib
from email.message import EmailMessage
import streamlit as st

class EmailHandler:
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    email_id = st.secrets.get('EMAIL_ID')
    email_password = st.secrets.get('EMAIL_PASSWORD')

    def __init__(self):
        self.msg = None

    def generate_mail(self, to_email, subject, html_body=None, files=None):

        msg = EmailMessage()
        msg["From"] = self.email_id
        msg["To"] = to_email
        msg["Subject"] = subject

        if html_body:
            msg.add_alternative(html_body, subtype="html")

        for f in files or []:
            data = f.getvalue()
            maintype, subtype = (f.type or "application/octet-stream").split("/", 1)
            msg.add_attachment(data, maintype=maintype, subtype=subtype, filename=f.name)

        self.msg = msg

    def send(self):
        msg = self.msg
        with smtplib.SMTP(self.smtp_server, self.smtp_port) as s:
            s.starttls()
            s.login(self.email_id, self.email_password)
            s.send_message(msg)