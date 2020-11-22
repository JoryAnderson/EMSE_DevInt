# List reserved key words (425) in source code using the infomation
# in this project:
# https://github.com/AnanthaRajuCprojects/Reserved-Key-Words-list-of-various-programming-languages

import os
import glob

PATH = "Reserved-Key-Words-list-of-various-programming-languages/"

def to_list():
	key_words = []

	#   /|
	#  / |
	# /__|______
	# |  __  __  |
	# | |  ||  | | 
	# | |__||__| |
	# |  __  __()|
	# | |  ||  | |
	# | |  ||  | |
	# | |__||__| |
	# |__________|
	# stairs to heaven...
	os.chdir(PATH)
	for file in glob.glob("*.md"):
		with open(file) as f:
			for line in f:
				line = line.lstrip()
				if len(line) > 1:
					if line[0] == '-':
						tokens = line.split()
						if len(tokens) > 1:
							key_word = line.split()[1]
							if len(key_word) != 1: # remove A-Z
								key_words += [key_word]
	os.chdir("..")
	return key_words