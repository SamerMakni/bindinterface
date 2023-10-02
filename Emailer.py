import smtplib
from email.message import EmailMessage
# import config

class EmailSender:
    def __init__(self, smtp_server=st.secrets["SMTP_SERVER"], smtp_port=st.secrets["SMTP_PORT"], username=st.secrets["USERNAME"], password=st.secrets["PASSWORD"]):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, to_email, subject, content):
        msg = EmailMessage()
        msg.set_content(content)
        msg['Subject'] = subject
        msg['From'] = self.username
        msg['To'] = to_email

        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.username, self.password)
            server.send_message(msg)
            server.quit()
            print("Email sent successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")
