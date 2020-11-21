from lib import APIDump
from lib import JSONReader
import sys
import gc

# First argument: File path to data.json
# Second argument (optional): Specifies a starting index, will grab 25k questions from this index or until
#                             EOF is reached.

if __name__ == '__main__':
    # Load Question Data, all unique
    question_data = JSONReader.load_json_to_dict(sys.argv[1])
    question_ids, start_index, end_index = [], None, None

    # Grab next 25k questions from starting index if second argument passed
    if len(sys.argv) == 3:
        start_index = int(sys.argv[2])
        end_index = min(start_index + 25000, len(question_data['items']))
        question_data['items'] = question_data['items'][start_index:end_index]

        # Debug Statement
        print("Indices: ", start_index, end_index)

    # Get final list of questions
    question_ids = JSONReader.grab_all_question_ids(question_data)

    # Debug Statements
    print("Number of questions from dataset: ", len(question_data['items']))
    print("Number of questions from question_id list: ", len(question_ids))
    print("Final Question in Set: " + str(question_ids[len(question_ids)-1]),
          question_data['items'][len(question_data['items'])-1])
    gc.collect()

    # Get answers using Question Data
    SITE = APIDump.config_api()
    answer_data = APIDump.get_answers_for_questions(SITE, question_ids)

    # Combine question/answer information
    important_text = JSONReader.get_combined_qa_list(question_data, answer_data, question_ids)

    APIDump.export_json_to_file(answer_data, "answers")
    if len(sys.argv) == 3:
        APIDump.export_json_to_file(question_data, "questions")
