import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

send(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

def send(name, email, subject, inquriy):
	message = MIMEMultipart()
	message['From'] = email
	message['Subject'] = subject
	message.attach(MIMEText(inquriy, 'text'))

	session = smtplib.SMTP('smtp.gmail.com', 587)
	session.starttls()  # enable security
	session.login('darpan.pmun@gmail.com', rwxgtashjdcluiac)
	session.sendmail('darpan.pmun@gmail.com', 'darpan.pmun@gmail.com', message.as_string())
	session.quit()

	print(f'**************************** Email inquiry by {name} sent. Check kar na! ****************************')