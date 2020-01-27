import link_validation

"""
Language of the scraped and analysed text.

set to "portuguese" or "english"

It is used when extracting the stop words and other things that may vary based on the language.
"""
LANGUAGE_OF_SCRAPED_TEXT = "english"
"""
Set the day between each requisition to the wikipedia page. 
This is used to limitate the requisitions per second and mitigate the risk
of having the ip blocked.
"""
DELAY = 0.3 
"""
Set the max quantity of links you intend to obtain.
Without the limit, it wouldn't stop running if every link lead to another one.

It will still get all the links of the page it is acessing even if it is more than the limit.
But in this case it will stoping the search after that.
"""
LINKS_EXTRACTION_LIMIT = 10000
"""
Set how many links of those obtained will be acessed and scraped.

Set to -1 to allow it to acess all links.
"""
LINKS_ACCESS_LIMIT = -1
"""
Set the filename of the links txt file.
"""
LINKS_FILENAME = "wikipedia_links.txt"
"""
Set the filename of the txt file to save the text scraped from the links.
"""
TEXT_FILENAME = "wikipedia_articles.txt"

"""
Determine the position of the first link to be scraped. Set zero to start from the first link

It is useful when for some reason the scraping was interrupted and you want start from the last link scraped.

"""
SCRAPING_START = 0
"""
Set the filename to txt file to which will be saved the stats from the text obtained.
"""
FREQUENCY_FILE = "pt_wikipedia_frequency.txt"

"""
Link Filter.

Set a function that receives the links and validate it according to the type of link you're
looking for on your aplication.

Set the function for both languages
"""
pt_link_validation = link_validation.pt_wikipedia_link
en_link_validation = link_validation.en_wikipedia_link

"""
Link Fix for English.

Set a function to turn a relative into a absolute link according to the function criteria.

Set the function for both languages
"""

pt_link_fix = link_validation.pt_wikipedia_link_fix
en_link_fix = link_validation.en_wikipedia_link_fix





if LANGUAGE_OF_SCRAPED_TEXT == "portuguese":

	LINK_VALIDATION = pt_link_validation
	LINK_FIX = pt_link_fix

if LANGUAGE_OF_SCRAPED_TEXT == "english":

	LINK_VALIDATION = en_link_validation
	LINK_FIX = en_link_fix