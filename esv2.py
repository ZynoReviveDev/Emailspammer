import smtplib
import ssl
from email.message import EmailMessage
from time import sleep
mailboks = """"
    _________
   |\       /|
   | \     / |
   |  `...'  |
   |__/___\_
"""
#varibler
count = 0 
print(mailboks + 'tool by Wefring')
Subject = input('mail topic: ') 
body = input('message in the mail: ')
sender_email = input('bot email: ')  #
password = input('bot password: ')   
reciver_mail = input('target: ')
print('Your bot account', sender_email, ' ', ('with password'), ' ', password, ' ', ('target'), ' >', reciver_mail,)
print('MAIL PREVIEW:V')
print(Subject)
print(body)
print('MAIL PREVIEW^')
message = EmailMessage()
message["From"] = sender_email 
message["To"] = reciver_mail
message["Subject"] = Subject 
message.set_content(body)

def sendmailen(): #
    context = ssl.create_default_context()
    print("sending mail NR",count)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, reciver_mail, message.as_string())
        print("sent! mail > NR",count) 
print('to make sure you entered everything right!')
conf = input('type confirm to start mail spam > ')
if conf == "confirm": 
    print('Starting spam ')
    for repeat in range(90): 
        count = count+1
        sendmailen()
        sleep(0.3)
else:
    print('ERROR', ' > ', 'remember to type confirm lowercase!')
    print('relaunch program and be carefull with spelling ')
    print('report issues to Wefring')
    sleep(10)
    quit()
print('spam is done total of ', count, 'mails')
sleep(10)
quit()
