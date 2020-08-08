import send, query

#email notification for 1USD below 22MXN
def email22():
	last = query.queryDB()[1]
	if last < 21.99:
		pass	
	else:
		current = query.queryDB()[0]
		body = f'X-rate is going down at MXN{current}/USD'
		send.sendMail(body)
