import stringstats as stats 
import txtstringify as txt

FILENAME = "wikipedia_articles.txt"
FREQUENCY_FILE = "pt_wikipedia_frequency.txt"

print("Getting text...")
text = txt.txtstringify.clean_text(FILENAME, nonumbers=True, lower=True)

print("Processing text...")

words_frequency = stats.stringstats.words_frequency_list(text, limit=1000)
characters_frequency = stats.stringstats.character_frequency_list(text)
words_count = stats.stringstats.words_count(text)
characters_count = len(text)
general_stats = "There are %d words and %d characters on the processed text" %(words_count, characters_count)

print("Saving results...")

with open(FREQUENCY_FILE, 'w') as file:

	file.write("TEXT STATISTICS\n\n")
	file.write(general_stats + "\n\n")
	file.write("Words Frequency: \n\n")

for line in words_frequency:
	
	with open(FREQUENCY_FILE, 'a') as file:

	   file.write("%s\n" %line)

with open(FREQUENCY_FILE, 'a') as file:

		file.write("\n")
		file.write("Characters Frequency: \n\n")

for line in characters_frequency:
	
	with open(FREQUENCY_FILE, 'a') as file:

	   file.write("%s\n" %line)
	   
print("Finished")