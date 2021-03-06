from lib import APIDump
from lib import JSONReader
import sys
import gc

if __name__ == '__main__':
    question_data = JSONReader.load_json_to_dict(sys.argv[1])
    question_data = JSONReader.remove_duplicate_questions(question_data)

    gc.collect()
    APIDump.export_json_to_file(question_data, 'nodupe')
