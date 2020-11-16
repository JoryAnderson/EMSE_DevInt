import time
from pathlib import Path
from stackapi import StackAPI
import json


def config_api(query_size=100, num_of_queries=10):
    site = StackAPI('stackoverflow')
    site.key = 'kBC4LfDjAYFLSEFWyrDhdw(( '
    site.page_size = query_size
    site.max_pages = num_of_queries

    return site


def get_questions(site):
    return site.fetch(filter='withbody', endpoint='questions')


def get_answers_for_questions(site, question_ids):
    return site.fetch(filter='withbody', endpoint='questions/{ids}/answers', ids=question_ids)


def convert_dict_to_json(posts):
    return json.dumps(posts)


def convert_json_to_dict(json_file):
    return json.loads(json_file)


def export_json_to_file(posts, file_name='data'):
    data = json.dumps(posts, indent=4)

    epoch_time = int(time.time())
    Path("data/").mkdir(parents=True, exist_ok=True)
    f = open("data/" + file_name + str(epoch_time) + ".json", "w")
    f.write(data)
    f.close()
