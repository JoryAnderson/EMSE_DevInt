import time
from pathlib import Path
from stackapi import StackAPI
import json


def config_api(query_size=100, num_of_queries=10):
    SITE = StackAPI('stackoverflow')
    SITE.key = 'kBC4LfDjAYFLSEFWyrDhdw(( '
    SITE.page_size = query_size
    SITE.max_pages = num_of_queries

    return SITE


def get_questions(SITE):
    return SITE.fetch(filter='withbody', endpoint='questions')


def get_answers_for_questions(SITE, question_ids):
    return SITE.fetch(filter='withbody', endpoint='questions/{ids}/answers', ids=question_ids)


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