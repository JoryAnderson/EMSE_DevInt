import time
from pathlib import Path
from stackapi import StackAPI
import json

QUERY_SIZE = 10
NUM_OF_QUERIES = 1

SITE = StackAPI('stackoverflow')
SITE.key = 'kBC4LfDjAYFLSEFWyrDhdw(( '
SITE.page_size = QUERY_SIZE
SITE.max_pages = NUM_OF_QUERIES


def get_questions():
    return SITE.fetch(filter='withbody', endpoint='questions')


def get_answers_for_questions(question_ids):
    return SITE.fetch(filter='withbody', endpoint='questions/{ids}/answers', ids=question_ids)


def convert_dict_to_json(posts):
    return json.dumps(posts)


def convert_json_to_dict(json):
    return json.loads(json)


def export_json_to_file(posts):
    data = json.dumps(posts, indent=4)

    epoch_time = int(time.time())
    Path("data/").mkdir(parents=True, exist_ok=True)
    f = open("data/data" + str(epoch_time) + ".json", "w")
    f.write(data)
    f.close()


if __name__ == '__main__':
    posts = get_questions()
    export_json_to_file(posts)
