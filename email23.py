import send, query 

#email notification for 1USD above 23MXN
def email23():
	last = query.queryDB()[1]
	if last > 23:
		pass
	else:
		current = query.queryDB()[0]
		body = f'X-rate is going up at MXN{current}/USD'
		send.sendMail(body)

