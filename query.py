import os, psycopg2

#query database and return current rate and previous rate
def queryDB():
	try:
		DATABASE_URL = os.environ['DATABASE_URL']
		conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		rates_db = conn.cursor()
	except:
		print('The database could not be accessed')
		
	sql = "SELECT * FROM rates ORDER BY checked_at DESC limit 2;"
	rates_db.execute(sql)
	last = rates_db.fetchall()
	conn.rollback()
	rates_db.close()	
	lastRate = float(last[1][0])
	currentRate = float(last[0][0])
	return (currentRate, lastRate)