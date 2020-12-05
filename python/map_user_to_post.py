'''
Given two JSON files of questions and answers in argument, return
a SQL file that contain two tables (username, question_id) and
(username, answer_id) mapping for statistical purpose (RQ1 & 2: the
distribution of number of questions/answers per developer)
(Did not use user id since found it does not exist in 768 question posts:
'user_type': 'does_not_exist')
'''

import sys
import json
import sqlite3

IN_QUESTIONS = "../data/questions_100k_full.json"
IN_ANSWERS = "../data/answers_100k_full_nodup.json"
OUT_DB = "../data/user_post.db"

q_data = json.load(open(IN_QUESTIONS))
a_data = json.load(open(IN_ANSWERS))

conn = sqlite3.connect(OUT_DB)
conn.execute("CREATE TABLE questions(uid INT, qid INT)")
conn.execute("CREATE TABLE answers(uid INT, aid INT)")

for post in q_data["items"]:
	user = post["owner"]
	if user['user_type'] != "does_not_exist":
		uid = user['user_id']
		qid = post["question_id"]
		conn.execute("INSERT INTO questions VALUES (?, ?)", (uid, qid))

for post in a_data["items"]:
	user = post["owner"]
	if user['user_type'] != "does_not_exist":
		uid = user['user_id']
		aid = post["answer_id"]
		conn.execute("INSERT INTO answers VALUES (?, ?)", (uid, aid))

conn.commit()
conn.close()
