## Crawler Stats

A collection of codes meant to get some stats on webpages using webscraping

#### About

This project consists of a tool to crawl a page, extract their links, extract the content of each link and analyse the texts obtained. Only some basic stats are made from the obtained text at the present momen. It is counted the words and characters as well as their frequency on the text. Later on I intend to use those tools to implement more deep analyses and statistcs.

### How it works

The Crawler makes a request using the initial links and save them into a file. Then this file is read again by other function that will acess all of those links and retrieve the text of those pages (I tested with wikipedia). The text is saved into another file and it is accessed by the function that will make the stats. After the stats are done, it is save into another txt file.


### How to use it

Create a txt file to the links, a file to save the text from the website and one to save the statistics.

In order to work, the link file must contain at least one link. That or those links are the one(s) will be accessed in order to get more links.

Open the config.py file and change the name of those files on the place provided in case the names differs from the default written there.

**Important:** On the config.py file there is a constant "LINK_VALIDATION" and "LINK_FIX". Both of them are set to functions in the link_validation.py file. 
The "LINK_VALIDATION" is a function to receives a url and check if it is valid or not (depending on the page you want to work with. In my case I created functions with rules to the portuguese wikipedia). And the "LINK_FIX" receives a url and returns it modified in case you make some checks and modify something (In my case the code is set by default to a function that turns the relative url into a valid portuguse wikipedia link)

Run the CrawlerStats.py file and the results of the analyses of the text will be saved to the file you set to receive them.

### Dependencies

The codes uses the FTDHandler and the StringStats libraries (built by me and also available on my Github) that are copied into this project. Besides that, you'll need to install the BeautifulSoup library and the requests library.

To install them using pip:

```
pip install requests

pip install beautifulsoup4

```



