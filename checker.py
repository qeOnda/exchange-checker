import time, bs4, csv, smtplib, os, psycopg2, random
from datetime import datetime
from selenium import webdriver
import getmxn, email22, getmxn 

#save mxn value to database and send email notifications when criteria is met
def saveToDB():
	try:
		DATABASE_URL = os.environ['DATABASE_URL']
		conn = psycopg2.connect(DATABASE_URL, sslmode='require')
		rates_db = conn.cursor()
		rates_db.execute('CREATE TABLE IF NOT EXISTS rates (mxn TEXT, checked_at  TIMESTAMP)')
	except:
		print('The database could not be accessed')
	#add rate to database
	rate = getmxn.getMxn()
	dt = datetime.now()
	time = dt.strftime("%Y-%m-%d, %H:%M:%S")
	rates_db.execute('INSERT INTO rates (mxn, checked_at) VALUES (%s, %s)', (rate, time,))
	conn.commit()
	rates_db.close()
	print(f"Rate logged at MXN{rate} per USD.")
	#trigger emails according to criteria
	if rate > str(23):
		email23.email23()
	elif rate < str(21.99):
		email22.email22()	



while True:
	saveToDB()
	time.sleep(60*30)