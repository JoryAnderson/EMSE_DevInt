import calendar
import datetime

from lib import APIDump
import sys

if __name__ == '__main__':

    if len(sys.argv) == 3:
        SITE = APIDump.config_api(sys.argv[1], sys.argv[2])
        posts = APIDump.get_questions(SITE, to_date=datetime.datetime(2020, 7, 31))
        APIDump.export_json_to_file(posts)
    else:
        SITE = APIDump.config_api(100, 100)
        posts = APIDump.get_questions(SITE, to_date=datetime.datetime(2020, 3, 31))
        APIDump.export_json_to_file(posts)
