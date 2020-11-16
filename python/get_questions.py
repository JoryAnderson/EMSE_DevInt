from lib import APIDump
import sys

if __name__ == '__main__':

    if len(sys.argv) == 3:
        SITE = APIDump.config_api(sys.argv[1], sys.argv[2])
        posts = APIDump.get_questions(SITE)
        APIDump.export_json_to_file(posts)
    else:
        SITE = APIDump.config_api(100, 10)
        posts = APIDump.get_questions(SITE)
        APIDump.export_json_to_file(posts)
