## Crawler Stats

A collection of codes meant to get some stats on webpages using webscraping

#### About

This collections of codes contain a crawler, a tool to copy articles from the wikipedia using webscraping, and a tool for analize its contents, extracting some stats about the text. Those stats at the present moment are onnly very basic. They only count the words and characters as well as their frequency on the text. Later on I intend to use those tools to implement more deep analyses and statistcs.


### How it works

The Crawler make a request to the link provided (I tested with wikipedia) and copy all the links. For as long as the limit of links initialized, the program continues to acess those links copying more of them. The links are read and saved in a file.

After that, you can execute the wikipedia_scraper.py file to acess all of the links and save the paragraph into a txt file.

After you have copied the paragraphs, you run the file that make the analises to provide the statistics.

### How to use it

Create a txt file to the links, a file to save the text from the website and one to save the statistcs.

Change the code of the crawler where is set the filename to the links. Do the same to wikipedia_scraper.py file and the text_stats.py with their correspondent files.

**Important:** On the crawler.py file there is a variable "LINK_VALIDATION" and "LINK_FIX". Both of them are set to functions in the link_validation.py file. The "LINK_VALIDATION" is a function to receives a url and check if it s valid or not (according with our objectives). And the "LINK_FIX" receives a url and returns it modified in case you make some checks and modify something. On our case the code is set by default to functions that check thoses variables to see if they correspond to a portuguese wikipedia url and fix and turn into a absolute url (of the portuguese wikipedia) if it's a relative url.

Run each of the files on this order (one at a time): crawler.py, wikipedia_scraper.py and text_stats.py

### Dependencies

The codes uses the TxtStringify and the StringStats libraries (built by me) that comes with the other files. Besides that, you'll need to install the BeautifulSoup library and the requests library.

To install them using pip:

```
pip install requests

pip install beautifulsoup4

```



