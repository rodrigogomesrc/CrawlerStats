import requests
from bs4 import BeautifulSoup
import txtstringify as txt
import time

LINKS_FILENAME = "wikipedia_links.txt"
TEXT_FILENAME = "wikipedia_articles.txt"
DELAY = 0.3

links = txt.txtstringify.raw_lines(LINKS_FILENAME, linebreaks=False)
links_quantity = len(links)
requested_links = 1

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


