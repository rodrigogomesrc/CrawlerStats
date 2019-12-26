from config import *
from StringStats import stringstats as stats
from FTDHandler import ftdhandler as txt 


def reset_file():

	with open(FREQUENCY_FILE, 'w') as file:

		file.write("")


def general_stats(text):

	words_count = stats.stringstats.words_count(text)
	characters_count = len(text)
	general_stats = "There are %d words and %d characters on the processed text" %(words_count, characters_count)

	with open(FREQUENCY_FILE, 'a') as file:

		file.write("TEXT STATISTICS\n\n")
		file.write(general_stats + "\n")


def words_frequency(text):

	words_frequency = stats.stringstats.words_frequency_list(text, limit=1000)

	with open(FREQUENCY_FILE, 'a') as file:

		file.write("\n")
		file.write("Words Frequency: \n\n")

	for line in words_frequency:
		
		with open(FREQUENCY_FILE, 'a') as file:

		   file.write("%s\n" %line)


def characters_frequency(text):

	characters_frequency = stats.stringstats.character_frequency_list(text)

	with open(FREQUENCY_FILE, 'a') as file:

		file.write("\nCharacters Frequency: \n\n")

	for line in characters_frequency:
		
		with open(FREQUENCY_FILE, 'a') as file:

		   file.write("%s\n" %line)


def analyse_text():

	reset_file()
	print("Getting text for analyze...")
	text = txt.ftdhandler.clean_text(TEXT_FILENAME, nonumbers=True, lower=True)
	print("Analyzing text...")
	general_stats(text)
	print("Calculating words frequency...")
	words_frequency(text)
	print("Calculating characters frequency...")
	characters_frequency(text)

	with open(FREQUENCY_FILE, 'a') as file:

		file.write("\nWITHOUT STOPWORDS: \n\n")

	print("Getting text for analyze...")
	text = txt.ftdhandler.clean_text(TEXT_FILENAME, nonumbers=True, lower=True, nostopwords="portuguese")
	print("Analyzing text...")
	general_stats(text)
	print("Calculating words frequency...")
	words_frequency(text)
	print("Calculating characters frequency...")
	characters_frequency(text)

	print("Finished")

if __name__ == "__main__":
	
	analyse_text()
	

