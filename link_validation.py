# set of rules to identify a specific cathegory of links

#get pt.wiki links
def pt_wiki_link(link):

	link = str(link)

	if link[0:4] != "http":

		return False

	if link[8] != "p" or link[9] != "t":

		return False

	return True

#concatenate wiki relative links
def pt_wiki_link(link):

	#no concatenation rule available at the moment
	return link
	

#get pt.wikipedia links
def pt_wikipedia_link(link):

	link = str(link)

	if link[0:4] != "http":

		return False

	if link[8:24] != "pt.wikipedia.org":

		return False

	return True

#concatenate pt-wikipedia relative links into absolute links
def pt_wikipedia_link_fix(link):

	link = str(link)

	if link[0] == "/":

		new_link = "https://pt.wikipedia.org" + link
		return new_link

	return link