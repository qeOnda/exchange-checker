import time, bs4, os
from selenium import webdriver

#scrape exchange rate and return it as a variable
def getMxn():	
	chrome_options = webdriver.ChromeOptions()
	chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
	chrome_options.add_argument("--headless")
	chrome_options.add_argument("--disable-dev-shm-usage")
	chrome_options.add_argument("--no-sandbox")
	browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
	url = 'https://www.investing.com/currencies/usd-mxn'	
	browser.get(url)
	time.sleep(1)
	#get exchange element
	soup = bs4.BeautifulSoup(browser.page_source, 'lxml')
	elem = soup.find(id='last_last')
	xchange = elem.text
	browser.close()
	
	
	return xchange

