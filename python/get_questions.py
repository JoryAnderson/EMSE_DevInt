import calendar
import datetime

from lib import APIDump
import sys

# Query size is always 100.
# Arg 1: The maximum number of pages in the response
# Arg 2: Which page to start on
# If no arguments provided, starts on page 1.
#   Max pages defaults to 100. (Therefore maximum result size on default is  100*100 = 10000)

if __name__ == '__main__':

    if len(sys.argv) == 3:
        SITE = APIDump.config_api(sys.argv[1])
        posts = APIDump.get_questions(SITE, to_date=datetime.datetime(2020, 10, 31), start_page=sys.argv[2])
        APIDump.export_json_to_file(posts)
    else:
        SITE = APIDump.config_api(100)
        posts = APIDump.get_questions(SITE, to_date=datetime.datetime(2020, 10, 31))
        APIDump.export_json_to_file(posts)
