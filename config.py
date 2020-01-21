import link_validation

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
Set the filename to txt file to which will be saved the stats from the text obtained.
"""
FREQUENCY_FILE = "pt_wikipedia_frequency.txt"
"""
Link Filter.

Set a function that receives the links and validate it according to the type of link you're
looking for on your aplication.
"""
LINK_VALIDATION = link_validation.pt_wikipedia_link
"""
Link Fix.

Set a function to turn a relative into a absolute link according to the function criteria.
"""
LINK_FIX = link_validation.pt_wikipedia_link_fix
