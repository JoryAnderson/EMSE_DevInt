from lib import APIDump
from lib import JSONReader
import sys

if __name__ == '__main__':
    # Load Question Data
    question_data = JSONReader.load_json_to_dict(sys.argv[1])
    question_ids = JSONReader.grab_all_question_ids(question_data)

    # Get answers using Question Data
    SITE = APIDump.config_api()
    answer_data = APIDump.get_answers_for_questions(SITE, question_ids)

    # Combine question/answer information
    important_text = JSONReader.get_combined_qa_list(question_data, answer_data, question_ids)
    for question_id in important_text:
        print(question_id)
        print(important_text.get(question_id))
