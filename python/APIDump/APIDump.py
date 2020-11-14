import time
from pathlib import Path
from stackapi import StackAPI
import json

QUERY_SIZE = 3
NUM_OF_QUERIES = 1


def get_posts():
    SITE = StackAPI('stackoverflow')

    # Adjust returning data
    SITE.page_size = QUERY_SIZE
    SITE.max_pages = NUM_OF_QUERIES

    # Get Data
    posts = SITE.fetch('posts')

    return posts


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
    posts = get_posts()
    export_json_to_file(posts)
