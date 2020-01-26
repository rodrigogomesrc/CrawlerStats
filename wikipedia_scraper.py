from config import *
from bs4 import BeautifulSoup
import requests
from FTDHandler import ftdhandler as txt 
import time


def extract_page_text(content):

	soup = BeautifulSoup(content, 'html.parser')
	paragraphs_list = soup.find_all("p")
	page_text = " "

	for paragraph in paragraphs_list:

		page_text += paragraph.get_text()

	return page_text

def scrape():

	links = txt.ftdhandler.raw_lines(LINKS_FILENAME, linebreaks=False)
	links_quantity = len(links)
	requested_links = SCRAPING_START
	print("Extracting pages from the links...")

	for n in range(SCRAPING_START, links_quantity):

		time.sleep(DELAY)
		current_link = links[n]

		try:

			response = requests.get(current_link)

			if response.status_code == 200:

				requested_links += 1
				print("Scraping %d of %d : %s" %(requested_links, links_quantity, current_link))
				text = extract_page_text(response.content)

				if (requested_links >= LINKS_ACCESS_LIMIT) and LINKS_ACCESS_LIMIT != -1:

					print("Link access limit reached")
					break

				with open(TEXT_FILENAME, 'a') as file:

					file.write(text)

			else:

				print("Request Error: %d" %response.status_code)

		except:

			continue



if __name__ == "__main__":
	
	scrape()
	