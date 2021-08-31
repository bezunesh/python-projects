import os
import smtplib

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PWD')

def sendEmail(available_dates):
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls()
        server.ehlo()

        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'DMV appointment for motor driving Test'
        body = f'Currently available dates: \n{available_dates}'
        msg = f'Subject: {subject}\n\n{body}'

        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)
        
        print('Email sent successfully.')
