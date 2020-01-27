# set of rules to identify a specific cathegory of links

#get pt.wikipedia links
def pt_wikipedia_link(link):

	link = str(link)

	if link[8:24] != "pt.wikipedia.org":

		return False

	return True


#concatenate pt.wikipedia relative links into absolute links
def pt_wikipedia_link_fix(link):

	link = str(link)

	if link[0] == "/":

		new_link = "https://pt.wikipedia.org" + link
		return new_link

	return link


#get en.wikipedia links
def en_wikipedia_link(link):

	link = str(link)

	if link[8:24] != "en.wikipedia.org":

		return False

	return True


#concatenate en.wikipedia relative links into absolute links
def en_wikipedia_link_fix(link):

	link = str(link)

	if link[0] == "/":

		new_link = "https://en.wikipedia.org" + link
		return new_link

	return link
