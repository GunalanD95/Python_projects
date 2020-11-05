import smtplib

username = 'iamgunalan10@gmail.com'

password = 'Guna19@NMC'

sender = 'iamgunalan10@gmail.com'
receivers = ['iamgunalan10@gmail.com']

message = """From: From Person <iamgunalan10@gmail.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
    smtpObj = smtplib.SMTP(host ='smtp.gmail.com',port = 587)
    smtpObj.starttls();
    smtpObj.login(username,password)
    smtpObj.sendmail(sender, receivers, message);        
    print ("Successfully sent email");
except smtplib.SMTPException:
    print ("Error: unable to send email")
