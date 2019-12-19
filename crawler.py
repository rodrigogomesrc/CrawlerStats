from config import *
from bs4 import BeautifulSoup
import requests
import txtstringify as txt
import link_validation
import time

def extract_link_tags(response_content):

	urls = list()
	soup = BeautifulSoup(response_content, 'html.parser')
	soup_links = soup.find_all("a")

	for link in soup_links:
		
		url = link.get('href')
		urls.append(url)

	return urls

def get_validated_links(links):

	validated_links = list()

	for link in links:

		fixed_link = LINK_FIX(link)

		if LINK_VALIDATION(fixed_link):

			validated_links.append(fixed_link)

	return validated_links


def save_links(links_to_save, link_save_list):
	
	links_count = 0

	for link in links_to_save:

		if link not in link_save_list:

			print("Extracted link: ", link)
			link_save_list.append(link)
			links_count += 1

	return links_count


def crawl():

	requested_links = list()
	links = txt.txtstringify.raw_lines(LINKS_FILENAME, linebreaks=False)
	total_extracted_links = 0
	limit = False
	print("Extracting links...")

	while True:

		for link in links:

			time.sleep(DELAY)

			if link in requested_links:
				
				continue

			requested_links.append(link)

			try:

				response = requests.get(link)
		
				if response.status_code == 200:

					extracted_links = list()
					page_links = extract_link_tags(response.content)
					validated_links = get_validated_links(page_links)
					execution_extracted_links = save_links(validated_links, extracted_links)
					total_extracted_links += execution_extracted_links

					if(execution_extracted_links == 0):

						print("All links provided were acessed")
						limit = True
						break

					if(total_extracted_links >= LINKS_EXTRACTION_LIMIT):

						print("Link limits reached")
						limit = True
						break

				else:

					print("Request Error: %d" %response.status_code)

			except:

				print("Error making the request")
				continue

		for link in extracted_links:

			links.append(link)

		if limit: break


	with open(LINKS_FILENAME, 'w') as file:

		for link in links:

		    file.write("%s\n" %link)


	print("%d Links Extracted" %total_extracted_links)