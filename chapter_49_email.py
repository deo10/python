# work with email SMTPLIB in python

from email.message import EmailMessage
import smtplib

from string import Template
from pathlib import Path


my_email = EmailMessage()

html_template = Template(Path("templates/index.html")) #path to the html template
html = html_template.substitute({'name':'Andrei', 'date':'tomorrow'}) # change $name to the real name



my_email['from'] = 'Andrei'
my_email['to'] = 'test@gmail.com'
my_email['subject'] = 'test email'
#my_email.set_content("Hello! It's test email")
my_email.set_content(html_template, 'html')

with open('images/image.jpg', 'rb') as img:  #rb - read binary
    image_data = img.read() # read image
    add_attachment = my_email.add_attachment(image_data, maintype='image', subtype='jpeg', filename='image.jpg') # add attachment
    

with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
    smtp_server.ehlo()
    #smtp_server.starttls()
    #smtp_server.login('username', 'password')
    smtp_server.send_message(my_email)
    print("Email was sent")


