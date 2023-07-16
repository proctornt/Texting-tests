import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
message = MIMEMultipart()
message["To"] = 'proctornt@gmail.com'
message["From"] = 'noahp5162@gmail.com'
message["Subject"] = 'Subject line here.'

title = '<b> Title line here. </b>'
messageText = MIMEText('''Message body goes here.''','html')
message.attach(messageText)

email = 'noahp5162@gmail.com'
password = 'hcwo uqse dlqa geup'

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo('Gmail')
server.starttls()
server.login(email,password)
fromaddr = 'noahp5162@gmail.com'
toaddrs  = 'proctornt@gmail.com'
server.sendmail(fromaddr,toaddrs,message.as_string())
