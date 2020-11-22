'''
Given a JSON file of question posts in argument:
	* split the body in each post into text and code
	* remove reserved key words in code
	* store (question_id, title, text, code) in csv format
'''

import sys
import json
import re
import pandas as pd
import reserved_key_words

# Input: the body of a post as a string
# Output: (a list of code blocks as strings, 
#          the body with code blocks removed as a string)
def split(body):
	pat_code = re.compile(r"<code>(.+?)<\/code>", flags=re.DOTALL)
	pat_tag = re.compile(r'<.*?>')

	codes = pat_code.findall(body) # extract code blocks
	code = '\n'.join(codes) # join into one

	text = pat_code.sub('', body) # remove code blocks from text
	text = pat_tag.sub('', text) # remove HTML tags

	return text, code


def process(data, outfile):
	qids = titles = texts = codes = []

	key_words = reserved_key_words.to_list()
	pat_key_words = re.compile('|'.join(map(re.escape, key_words))) # for removal

	for i in range(len(data["items"])):
		if i % 1000 == 0:
			print(i)

		post = data["items"][i]
		qids += [post["question_id"]]
		titles += [post["title"]]
		body = post["body"]

		text, code = split(body)

		code = pat_key_words.sub('', code) # remove key words

		texts += [text]
		codes += [code]

	list_of_tuples = list(zip(qids, titles, texts, codes))
	df = pd.DataFrame(list_of_tuples, columns=["qid", "title", "text", "code"])
	df.to_csv(outfile)


def main(argv):
	if len(argv) != 2:
		print("USAGE: python3 split_text_code.py <JSON_file_path>")
	else:
		infile = argv[-1]
		outfile = infile[:infile.rfind('.')] + ".csv"
		with open(infile) as f:
			process(json.load(f), outfile)

	
if __name__ == '__main__':
	main(sys.argv)
