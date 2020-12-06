'''
Given two JSON file for questions and answers in argument:
	* For each file:
		* split the body in each post into text and code
		* remove reserved key words in code
		* for questions, store (question_id, user_id, title, tags, text, code) in a csv file;
		  for answers, store (question_id, user_id(answer-er), text, code) in another csv file
'''

import sys
import json
import re
import pandas as pd
import reserved_key_words
from lib import JSONReader

IN_QUESTIONS = "../data/questions_100k_full.json"
IN_ANSWERS = "../data/answers_100k_full_nodup.json"
OUT_QUESTIONS = "../data/split_questions.csv"
OUT_ANSWERS = "../data/split_answers.csv"
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

	if DO_QUESTIONS:
		print("Processing questions")

		qids = []
		uids = []
		titles = []
		tags = []
		texts = []
		codes = []

		i = 0
		dne = 0
		for question in question_data["items"]:
			i += 1
			if i % 1000 == 0:
				print(i)

			qids += [question["question_id"]]

			user = question["owner"]
			if user['user_type'] != "does_not_exist":
				uid = user['user_id']
			else:
				uid = None
				print('\t', question["question_id"], user)
				dne += 1
			uids += [uid]

			titles += [question["title"]]
			tags += [','.join(question["tags"])]

			text, code = split(question["body"])
			code = pat_key_words.sub('', code) # remove key words
			texts += [text]
			codes += [code]

		list_of_tuples = list(zip(qids, uids, titles, tags, texts, codes))
		df = pd.DataFrame(list_of_tuples, columns=["qid", "uid", "title", "tags", "text", "code"])
		df.to_csv(OUT_QUESTIONS)
		print("User ID does not exist:", dne)


	if DO_ANSWERS:
		print("Processing answers")

		# {question_id : [(user_id, answer_body)]}
		qid_answers = JSONReader.get_answer_list(question_data, answer_data)

		qids = []
		uids = []
		texts = []
		codes = []

		i = 0
		dne = 0
		# for each question
		for qid, answers in qid_answers.items():
			i += 1
			if i % 1000 == 0:
				print(i)

			# for each answer to the question
			for uid, body in answers:
				qids += [qid]
				uids += [uid]
				text, code = split(body)
				code = pat_key_words.sub('', code) # remove key words
				texts += [text]
				codes += [code]

				if uid == None:
					dne += 1

		list_of_tuples = list(zip(qids, uids, texts, codes))
		df = pd.DataFrame(list_of_tuples, columns=["qid", "uid", "text", "code"])
		df.to_csv(OUT_ANSWERS)
		print("User ID does not exist:", dne)


def main():
	with open(IN_QUESTIONS) as f_q, open(IN_ANSWERS) as f_a:
		process(json.load(f_q), json.load(f_a))

	
if __name__ == '__main__':
	main()
