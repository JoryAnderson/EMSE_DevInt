'''
Given a JSON file of question posts in argument, return
a SQL file that contain a single table of (user name, question id)
mapping for statistical purpose (RQ1: distribution of number of
questions per questioner)
(Did not use user id since it does not exist in 768 posts:
'user_type': 'does_not_exist')
'''

import sys
import json
import sqlite3

DB = "uname_qid.db"

def process(data):
	conn = sqlite3.connect(DB)
	conn.execute("CREATE TABLE uname_qid(uname VARCHAR, qid INT)")

	for post in data["items"]:
		try:
			uname = post["owner"]["display_name"]
			qid = post["question_id"]
			conn.execute("INSERT INTO uname_qid VALUES (?, ?)", (uname, qid))
		except:
			print(post["owner"])

	conn.commit()
	conn.close()


def main(argv):
	if len(argv) != 2:
		print("USAGE: python3 map_uid_qid.py <JSON_file_path>")
	else:
		with open(argv[-1]) as f:
			process(json.load(f))


if __name__ == '__main__':
	main(sys.argv)