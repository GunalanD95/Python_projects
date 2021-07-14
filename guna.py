import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

username = 'iamgunalan10@gmail.com'

password = 'abc'
def send_mail(text = "email body",from_mail = 'GUNA D <iamgunalan10@gmail.com>' ,sub = "hello world" , to_email = 'iamgunalan10@gmail.com'):
	msg = MIMEMultipart('alternative')
	msg['From'] = from_mail
	msg['To'] = ",".join(to_email)
	msg['Subject'] = sub

	txt_part = MIMEText(text,'plain')
	msg.attach(txt_part)

	#html_part = MIMEText("<h1>This is Working</h1>",'html')
	#msg.attach(txt_part)

	msg_str = msg.as_string()

	# login to SMTP
	server = smtplib.SMTP(host ='smtp.gmail.com',port = 587)
	server.ehlo()
	server.starttls()
	server.login(username,password)
	server.send_mail(from_mail,to_email,msg_str)

	server.quit()



		
