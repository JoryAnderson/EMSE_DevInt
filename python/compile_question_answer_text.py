from lib import APIDump
from lib import JSONReader
import sys

if __name__ == '__main__':
    # Load Question Data, all unique
    question_data = JSONReader.load_json_to_dict(sys.argv[1])
    question_ids = JSONReader.grab_all_question_ids(question_data)

    # Grab next 25k questions from starting index
    start_index = int(sys.argv[2])
    end_index = min(start_index + 25000, len(question_data['items']))

    # Modify questions to only include specified 25k questions
    question_data['items'] = question_data['items'][start_index:end_index]
    question_ids = question_ids[start_index:end_index]
    print("Indices: ", start_index, end_index)
    print("Number of questions from dataset: ", len(question_data['items']))
    print("Number of questions from question_id list: ", len(question_ids))

    # Get answers using Question Data
    SITE = APIDump.config_api()
    answer_data = APIDump.get_answers_for_questions(SITE, question_ids)

    # Combine question/answer information
    important_text = JSONReader.get_combined_qa_list(question_data, answer_data, question_ids)
    APIDump.export_json_to_file(answer_data, "answers")
