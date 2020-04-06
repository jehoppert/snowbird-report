import smtplib
import ssl

import configparser

config = configparser.ConfigParser()
config.read('./config.ini')





#retreive snowbird report information to send out
#TODO: break out into seperate file





#for using SSL with GMail
port = config['EMAIL']['port']
smtp_host = config['EMAIL']['smtp_host']

#init login credentials
senderEmailUsername = config['CREDENTIALS']['senderEmailUsername']
senderEmailPassword = config['CREDENTIALS']['senderEmailPassword']


receiverEmail = config['CREDENTIALS']['receiverEmail'] #email/sms email gateway


'''
message = "From: %s\r\n" % senderEmailUsername + "To: %s\r\n" % receiverEmail + "Subject: %s\r\n" % "test subject text" + "\r\n" + "\rtest body text"

#create secure SSL context
context = ssl.create_default_context() 

#login to the GMail account
with smtplib.SMTP_SSL(smtp_host, port, context=context) as server:
    server.login(senderEmailUsername, senderEmailPassword)

    #send email here
    server.sendmail(senderEmailUsername, receiverEmail, message)
'''