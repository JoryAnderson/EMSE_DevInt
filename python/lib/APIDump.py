import time
from pathlib import Path
from stackapi import StackAPI
import json


# config_api
#   Returns object to interact with API. Defaults to 10 queries
#   with 100 results each (~1000 results).
def config_api(query_size=100, num_of_queries=10):
    site = StackAPI('stackoverflow')
    site.key = 'kBC4LfDjAYFLSEFWyrDhdw(( '
    site.page_size = query_size
    site.max_pages = num_of_queries
    return site


# get_questions
#   Returns a dictionary containing questions
def get_questions(site):
    return site.fetch(filter='withbody', endpoint='questions')


# get_answers_for_questions
#   Returns a dictionary containing answers to the specified questions
def get_answers_for_questions(site, question_ids):
    return site.fetch(filter='withbody', endpoint='questions/{ids}/answers', ids=question_ids)


def convert_json_to_dict(json_file):
    return json.loads(json_file)


def export_json_to_file(data, file_name='data'):
    data = json.dumps(data, indent=4)

    epoch_time = int(time.time())
    Path("data/").mkdir(parents=True, exist_ok=True)
    f = open("data/" + str(file_name) + str(epoch_time) + ".json", "w")
    f.write(data)
    f.close()
