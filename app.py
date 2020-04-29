import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
	word = word.lower()
	if word in data:
		return data[word]
	elif word.title() in data:
		return data[word.title()]	
	elif word.upper() in data:
		return data[word.upper()]	
	elif len(get_close_matches(word, data.keys(), cutoff = 0.75)) > 0:
		yn = input("Did u mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
		if yn == "Y":
			return data[get_close_matches(word, data.keys())[0]]
		elif yn == "N":
			return "There word doesn't exist. Please double check it."
		else:
			return "U entered undefined query."		
	else:
		return "There word doesn't exist. Please double check it."

word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)		