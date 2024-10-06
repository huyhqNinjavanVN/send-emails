import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
import os
import json
from jinja2 import Template

'''
    https://myaccount.google.com/apppasswords
    https://mailtrap.io/blog/python-send-email-gmail/
'''

def send_email(subject, body, attachment, account, password, sender_alias, email_alias, recipients):
    # Choose multipart/alternative.
    message = MIMEMultipart("alternative")

    message['Subject'] = subject
    message['From'] = formataddr((str(Header(sender_alias, 'utf-8')), email_alias))
    message['To'] = ', '.join(recipients)

    # Choose plain/html
    plain_part = MIMEText(body, 'html')

    message.attach(plain_part)
    message.attach(attachment)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(account, password)
       smtp_server.sendmail(
           account,
           recipients,
           message.as_string()
       )
       smtp_server.quit()

    print("Sent Successfully!")



if __name__ == '__main__':
    root = os.path.abspath(os.path.abspath('__file__' + '/..'))


    with open(os.path.join(root, 'conf/conf.json'), mode='r', encoding='utf8') as conf:
        conf_ = json.load(conf)

    account = conf_.get('account').get('email')
    password = conf_.get('account').get('key')
    email_alias = conf_.get('email_alias')
    sender_alias = conf_.get('sender_alias')
    receiver = conf_.get('receiver')
    subject = conf_.get('subject')
    template_file = conf_.get('template')
    user_name = conf_.get('user_name')
    attachment_file = conf_.get('attachment')
    file_name = conf_.get('attachment_alias')

    # HTML
    with open(os.path.join(root, f'templates/teamplate.html'), mode="r", encoding="utf8") as html_file:
        html_content = html_file.read()
        template = Template(html_content)
        rendered_html = template.render(user_name=user_name)

    # Attachment
    with open(os.path.join(root, 'attachment/file_1.txt'), mode='rb') as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={file_name}"
        )

    send_email(
        subject=subject,
        body=rendered_html,
        attachment=part,
        account=account, 
        password=password, 
        sender_alias=sender_alias, 
        email_alias=email_alias, 
        recipients=receiver
    )