from lib import APIDump
from lib import JSONReader
import sys
import gc

if __name__ == '__main__':
    answer_data = JSONReader.load_json_to_dict(sys.argv[1])
    answer_data = JSONReader.remove_duplicate_answers(answer_data)

    gc.collect()
    APIDump.export_json_to_file(answer_data, 'nodupe')
