import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(name,receiver_email):
    def get_thank_you_template(path):
        with open(path, mode='r', encoding='utf-8') as html:
            return html.read()


    def send_email(sender_email, app_password, receiver_email, subject, text_content, html_content):

        with smtplib.SMTP('smtp.gmail.com', 587) as mail:

            mail.starttls()
            mail.login(sender_email, app_password)

            msg = MIMEMultipart('alternative')
            msg['SUBJECT'] = subject
            msg['FROM'] = sender_email
            msg['TO'] = receiver_email

            text_part = MIMEText(text_content)
            html_part = MIMEText(html_content, 'html')

            msg.attach(text_part)
            msg.attach(html_part)

            mail.send_message(msg)
            print('message successfully sent.')


    sender_email = 'your_gmail@gmail.com'
    app_password = 'your_password'
    subject = 'Thank You' +' '+ name 
    text_content = '''Thank you contacting me. I will try as fast as possible to try and contact with you very soon .'''
    html_content = get_thank_you_template('./templates/thank_you_template.html')
    send_email(sender_email, app_password, receiver_email,subject, text_content, html_content)
