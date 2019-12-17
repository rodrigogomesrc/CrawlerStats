from config import *
from bs4 import BeautifulSoup
import requests
import txtstringify as txt
import time

def scrape():

	links = txt.txtstringify.raw_lines(LINKS_FILENAME, linebreaks=False)
	links_quantity = len(links)
	requested_links = 1
	print("Extracting pages from the links...")

	for n in range(links_quantity):

		time.sleep(DELAY)
		current_link = links[n]

		try:

			response = requests.get(current_link)

			if response.status_code == 200:

				print("Scraping %d of %d : %s" %(requested_links, links_quantity, current_link))
				requested_links += 1
				content = response.content
				soup = BeautifulSoup(content, 'html.parser')
				paragraphs = soup.find_all("p")
				text = " "

				for p in paragraphs:

					text += p.get_text()

				with open(TEXT_FILENAME, 'a') as file:

					file.write(text)
			else:

				print("Request Error: %d" %response.status_code)

		except:

			continue

		if requested_links >= LINKS_ACCESS_LIMIT and LINKS_ACCESS_LIMIT != -1:

			print("Link access limit reached")
			break


