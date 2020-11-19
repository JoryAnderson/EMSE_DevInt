<<<<<<< HEAD
'''
Given a JSON file of question posts, split the body in each post
into text and code block(s), then save title, text, and each code
block into seperated files.
'''

import sys
import json
import os
import re

PATH_OUT = "data_splitted/"

=======
# Split body in post into text and code block(s)

import re

>>>>>>> 5816c2a05f735bb5e70b183fff184311a65ea352
# Remove HTML tags in text
def remove_tags(text):
	pat = re.compile(r'<.*?>')
	return pat.sub('', text)

<<<<<<< HEAD

=======
>>>>>>> 5816c2a05f735bb5e70b183fff184311a65ea352
# Input: the body of a post as a string
# Output: (a list of code blocks as strings, 
#		   the body with code blocks removed as a string)
def split(body):
	pat = re.compile(r"<code>(.+?)<\/code>", flags=re.DOTALL)
	codes = pat.findall(body) # extraction
	text = remove_tags(pat.sub('', body)) # removal
	return text, codes

<<<<<<< HEAD

def split_questions_in_json(data):
	os.system("mkdir " + PATH_OUT)

	for item in data["items"]:
		qid = item["question_id"]
		title = item["title"]
		body = item["body"]

		text, codes = split(body)

		path = PATH_OUT + str(qid) + '/' # use question_id as directory name
		os.system("mkdir " + path)

		with open(path+"title.txt", 'w') as f:
			f.write(title)
		with open(path+"text.txt", 'w') as f:
			f.write(text)
		for i in range(len(codes)):
			with open(path+"code_"+str(i)+".txt", 'w') as f:
				f.write(codes[i])


def test_split():
	body = "<p>I want to write some automation to website. Simply filling in forms and simulating clicks on elements. But for some elements JavaScript function click() doesn't work. For example it is on this page: <a href=\"http://www1.plus.pl/bsm/\" rel=\"noreferrer\">http://www1.plus.pl/bsm/</a> If I do click() on \"Wy\u015blij\" button, nothing happens. It is my command:</p>\n\n<pre><code>document.getElementsByClassName('tab-button')[0].click()\n</code></pre>\n\n<p>What is wrong? Why on other elements this function works?</p>\n"
	text, codes = split(body)
	print(text)
	print(codes)


def main(argv):
	if len(argv) != 2:
		print("USAGE: python3 split_text_code.py <JSON_file_path>")
	else:
		with open(argv[-1]) as f:
			split_questions_in_json(json.load(f))


if __name__ == '__main__':
	main(sys.argv)
=======
def main():
	example = "<p>I want to write some automation to website. Simply filling in forms and simulating clicks on elements. But for some elements JavaScript function click() doesn't work. For example it is on this page: <a href=\"http://www1.plus.pl/bsm/\" rel=\"noreferrer\">http://www1.plus.pl/bsm/</a> If I do click() on \"Wy\u015blij\" button, nothing happens. It is my command:</p>\n\n<pre><code>document.getElementsByClassName('tab-button')[0].click()\n</code></pre>\n\n<p>What is wrong? Why on other elements this function works?</p>\n"
	text, code = split(example)
	print(text)
	print(code)

if __name__ == '__main__':
	main()
>>>>>>> 5816c2a05f735bb5e70b183fff184311a65ea352
