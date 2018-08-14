import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def mail(sender,passwd,recievers):
	ret = True
	try:
		msg = MIMEText('hello world ','plain','utf-8')
		msg['From'] = formataddr(("XXX",sender))
		msg['To'] = formataddr(['XXX',recievers[0]])
		msg['Subject'] = "邮件测试"
		server = smtplib.SMTP_SSL('smtp.qq.com',465)
		print("hello")
		server.login(sender,passwd)
		server.sendmail(sender,recievers,msg.as_string())
		server.quit()
	except Exception:
		ret = False
	return ret

if __name__ == '__main__':
	my_sender = 'XXX@qq.com'
	my_reciever = ['XXX@163.com']
	my_passwd = 'XXXX' 
	result = mail(my_sender,my_passwd,my_reciever)
	print(result)
	if result:
		print("邮件发送成功")
	else:
		print("邮件发送失败")
