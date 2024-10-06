import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import os

'''
    https://myaccount.google.com/apppasswords
    https://mailtrap.io/blog/python-send-email-gmail/
'''

def send_email(subject, body1, body2, sender, recipients, password):
    # multipart/alternative.
    message = MIMEMultipart("alternative")

    message['Subject'] = subject
    message['From'] = sender
    message['To'] = ', '.join(recipients)

    # plain/html
    plain_part = MIMEText(body1, 'plain')
    html_part = MIMEText(body2, 'html')

    message.attach(plain_part)
    message.attach(html_part)
    message.attach(part)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, message.as_string())
    print("Message sent!")


if __name__ == '__main__':
    root = os.path.abspath(os.getcwd())
    os.chdir(root)

    sender = "huy.hoquang@ninjavan.co"
    receiver = ["huy.hoquang@ninjavan.co", "quanghuyho06@gmail.com"]
    password = "oakw pwyn uirh mseq"

    subject = "Subject"
    body1 = "This is the body email."

    with open('teamplate.html', mode="r", encoding="utf8") as template:
        index = template.read()
        body2 = BeautifulSoup(index, 'html.parser')
        body2.format(mail=sender)


    with open('attachment.txt', mode="rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename=attachment.txt",
        )

    send_email(subject, body1, body2, sender, receiver, password)
