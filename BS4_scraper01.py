from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
from datetime import datetime

def webScrape():
	urlScrape = "http://www.ameratlanta.com/cocktails/"
	html_page = urlopen(urlScrape)
	html_text = html_page.read().decode('utf-8')
	my_soup = BeautifulSoup(html_text, "html.parser")
	
	name_box = my_soup.find_all('div', attrs={'class' :'sqs-block-content'})
	#print(name_box)
	
	cocktailList=my_soup.find_all(["p"])
		
	with open('cocktails01.csv', 'a') as csv_file:
		    #print(csv_file)
		scrapwriter = csv.writer(csv_file)
		for i in cocktailList:
			scrapwriter.writerow([i.text])
	print('Scraping finished, please see the csv file!') 

webScrape()
