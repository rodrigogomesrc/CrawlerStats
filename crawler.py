from config import *
from bs4 import BeautifulSoup
import requests
import txtstringify as txt
import link_validation
import time

def crawl():

	requested_links = list()
	links = txt.txtstringify.raw_lines(LINKS_FILENAME, linebreaks=False)
	links_quantity = len(links)
	print("Extracting links")

	while True:

		for n in range(links_quantity):

			time.sleep(DELAY)
			current_link = links[n]

			if current_link in requested_links:
				
				continue

			requested_links.append(current_link)

			try:

				response = requests.get(current_link)

				if response.status_code == 200:

					content = response.content
					soup = BeautifulSoup(content, 'html.parser')
					soup_links = soup.find_all("a")
					extracted_links = list()

					for i in range(len(soup_links)):

						new_link = soup_links[i].get('href')
						new_link = LINK_FIX(new_link)

						if new_link not in links and new_link not in extracted_links and LINK_VALIDATION(new_link):

							print("Extracted link: ", new_link)
							extracted_links.append(new_link)
				else:

					print("Request Error: %d" %response.status_code)

			except:

				continue

		for link in extracted_links:

			links.append(link)

		number_of_extracted_links = len(extracted_links)
		number_of_links = len(links)
		print("%d links extracted in this execution" %number_of_extracted_links)
		print("Total links: %d" %number_of_links)

		with open(LINKS_FILENAME, 'w') as file:

		    for link in links:

		        file.write("%s\n" %link)

		if(number_of_links >= LINKS_EXTRACTION_LIMIT):

			print("Link limits reached")
			break

		if(number_of_extracted_links == 0):

			print("All links provided were acessed")
			break
