import time
from pathlib import Path
from stackapi import StackAPI
import json


# config_api
#   Returns object to interact with API. Defaults to 10 queries
#   with 100 results each (~1000 results).
def config_api(num_of_queries=10):
    site = StackAPI('stackoverflow')
    site.key = 'kBC4LfDjAYFLSEFWyrDhdw(( '
    site.page_size = 100
    site.max_pages = int(num_of_queries)
    return site


# get_questions
#   Returns a dictionary containing questions
def get_questions(site, to_date=None, start_page=1):
    if to_date is None:
        return site.fetch(filter='withbody', endpoint='questions')
    else:
        return site.fetch(filter='withbody', endpoint='questions', todate=to_date, page=int(start_page))


# get_answers_for_questions
#   Returns a dictionary containing answers to the specified questions
def get_answers_for_questions(site, question_ids):
    return site.fetch(filter='withbody', endpoint='questions/{ids}/answers', ids=question_ids)


# Gets user information from a one or more user ids.
#   Returns a dictionary containing user information
def get_users_from_ids(site, user_ids):
    return site.fetch(filter='!)69Ph0.C7QpzLW2uqg2)FUdUlwkr', endpoint='users/{ids}', ids=user_ids)


def convert_json_to_dict(json_file):
    return json.loads(json_file)


def export_json_to_file(data, file_name='data'):
    data = json.dumps(data, indent=4)

    epoch_time = int(time.time())
    Path("data/").mkdir(parents=True, exist_ok=True)
    f = open("data/" + str(file_name) + str(epoch_time) + ".json", "w")
    f.write(data)
    f.close()
