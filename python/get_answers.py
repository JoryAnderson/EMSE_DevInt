from lib import APIDump
from lib import JSONReader
import sys
import gc

# Creates an 'answers' JSON containing the answers to the selected 25k questions.
# First argument: File path to data.json
# Second argument: Specifies a starting index, will grab 25k questions from this index or until EOF is reached.

# EXAMPLE -------
# Get the answers from the first 25k questions: get_answers.py data/nodupe_100k_from_236k.json 0

if __name__ == '__main__':

    # Load Question Data, all unique
    question_data = JSONReader.load_json_to_dict(sys.argv[1])

    # Assert that we have all the command line arguments
    assert len(sys.argv) == 3

    # Grab next 25k questions from starting index
    start_index = int(sys.argv[2])
    end_index = min(start_index + 25000, len(question_data['items']))
    question_data['items'] = question_data['items'][start_index:end_index]

    # Get final list of questions
    question_ids = JSONReader.grab_flat_question_id_list(question_data)

    # Debug Statements
    print("Number of questions from dataset: ", len(question_data['items']))
    print("Number of questions from question_id list: ", len(question_ids))
    print("Final Question in Set: " + str(question_ids[len(question_ids)-1]),
          question_data['items'][len(question_data['items'])-1])
    print("Indices: ", start_index, end_index)
    gc.collect()

    # Split questions into chunks of size 100 (due to API limitations)
    question_ids = [question_ids[i:i + 100] for i in range(0, len(question_ids), 100)]
    print("Number of chunks: ", len(question_ids), "Size of chunk: ", len(question_ids[0]))

    # Get answers using Question Data
    SITE = APIDump.config_api(100)
    answer_data = APIDump.get_answers_for_questions(SITE, question_ids[0])

    # Get answers in batches and merge
    for split in question_ids:
        response = APIDump.get_answers_for_questions(SITE, split)
        answer_data['items'].extend(response['items'])

    # Export to file
    APIDump.export_json_to_file(answer_data, "answers")