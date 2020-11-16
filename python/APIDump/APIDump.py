import time
from pathlib import Path
from stackapi import StackAPI
import json

QUERY_SIZE = 100
NUM_OF_QUERIES = 250


def config_api():
    SITE = StackAPI('stackoverflow')
    SITE.key = 'kBC4LfDjAYFLSEFWyrDhdw(( '
    SITE.page_size = QUERY_SIZE
    SITE.max_pages = NUM_OF_QUERIES

    return SITE


def get_questions():
    return config_api().fetch(filter='withbody', endpoint='questions')


def get_answers_for_questions(question_ids):
    return config_api().fetch(filter='withbody', endpoint='questions/{ids}/answers', ids=question_ids)


def convert_dict_to_json(posts):
    return json.dumps(posts)


def convert_json_to_dict(json):
    return json.loads(json)


def export_json_to_file(posts, file_name='data'):
    data = json.dumps(posts, indent=4)

    epoch_time = int(time.time())
    Path("data/").mkdir(parents=True, exist_ok=True)
    f = open("data/" + file_name + str(epoch_time) + ".json", "w")
    f.write(data)
    f.close()


if __name__ == '__main__':
    posts = get_questions()
    export_json_to_file(posts)
