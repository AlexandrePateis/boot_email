from email.policy import SMTP
import os
import smtplib
from email.message import EmailMessage
from SECRET import senha 

#configura email

EMAIL_ADDRESS = 'alexandre@cfaz.net'
EMAIL_PASSWORD = senha
msg = EmailMessage()
msg['Subject'] = 'Senha Cfaz'
msg['From'] = 'alexandre@cfaz.net'
msg['To'] = 'felipe@cfaz.net'
with open("mensagem.txt", "r") as arquivo:
    email=arquivo.read()
msg.set_content(email)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)