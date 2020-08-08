import smtplib

email = 'EMAIL@ADDRESS.com'
password = 'PASSWORD'
send_to = 'ANOTHER@gADDRESS.com'

#function that sends email 
def sendMail(body1):
	user = email
	pword = password
	sent_from = user
	to = [send_to]
	body = body1
	try:
		server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server_ssl.ehlo()
		server_ssl.login(user, pword)
		server_ssl.sendmail(sent_from, to, body)
		server_ssl.close()
		print("email sent!")
	except:
		print("There was an error")