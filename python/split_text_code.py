'''
Given two JSON file for questions and answers in argument:
	* For each file:
		* split the body in each post into text and code
		* remove reserved key words in code
		* for questions, store (question_id, title, text, code) in a csv file;
		  for answers, store (question_id, text, code) in another csv file
'''

import sys
import json
import re
import pandas as pd
import reserved_key_words
from lib import JSONReader

OUT_QUESTIONS = "questions.csv"
OUT_ANSWERS = "answers.csv"
DO_QUESTIONS = False
DO_ANSWERS = True

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


def process(question_data, answer_data):
	# get reserved key words in code
	key_words = reserved_key_words.to_list()
	pat_key_words = re.compile('|'.join(map(re.escape, key_words))) # for removal

	# load all the data as a dictionary (use a lot of memory)
	# {question_id : [question_title, question_body, [answers, empty if none]]}
	print("Loading data")
	all_question_answer_text = JSONReader.get_combined_qa_list(question_data, answer_data)

	if DO_QUESTIONS:
		print("Processing questions")
		qids = titles = texts = codes = []

		i = 0
		for qid, entry in all_question_answer_text.items():
			i += 1
			if i % 1000 == 0:
				print(i)

			qids += [qid]
			titles += [entry[0]]
			text, code = split(entry[1])

			code = pat_key_words.sub('', code) # remove key words

			texts += [text]
			codes += [code]

		list_of_tuples = list(zip(qids, titles, texts, codes))
		df = pd.DataFrame(list_of_tuples, columns=["qid", "title", "text", "code"])
		df.to_csv(OUT_QUESTIONS)


	if DO_ANSWERS:
		print("Processing answers")
		qids = texts = codes = []

		i = 0
		for qid, entry in all_question_answer_text.items():
			i += 1
			if i % 1000 == 0:
				print(i)

			for ans in entry[2]:
				qids += [qid]
				text, code = split(ans)

				code = pat_key_words.sub('', code) # remove key words

				texts += [text]
				codes += [code]

		list_of_tuples = list(zip(qids, texts, codes))
		df = pd.DataFrame(list_of_tuples, columns=["qid", "text", "code"])
		df.to_csv(OUT_ANSWERS)


def main(argv):
	if len(argv) != 3:
		print("USAGE: python3 split_text_code.py <questions_JSON_file> <answers_JSON_file>")
	else:
		with open(argv[-2]) as f_q, open(argv[-1]) as f_a:
			process(json.load(f_q), json.load(f_a))

	
if __name__ == '__main__':
	main(sys.argv)
