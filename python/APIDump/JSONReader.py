import json
import APIDump
from collections import defaultdict

def load_json_to_dict(file):
    with open(file) as json_file:
        return json.load(json_file)


def grab_all_question_ids(data):
    return [data['items'][i]['question_id'] for i in range(0, len(data['items']))]


# get_combined_qa_list
#   Combines question and answer texts into a list of lists. Still requires processing.
#   list[0] contains the first Q/A text(s)
#   list[0][0] contains the title of the first question
#   list[0][1] contains the body of the first question
#   list[0][n] contains body for any answers (of the first question) which may or may not exist.
def get_combined_qa_list(question_data, answer_data, question_ids):

    # {question_id : list}
    all_question_answer_text = {}

    for question_id in question_ids:
        question_text = []

        for i in range(0, len(question_data['items'])):
            if question_data['items'][i]['question_id'] == question_id:
                question_text.append(question_data['items'][i]['title'])
                question_text.append(question_data['items'][i]['body'])
                break

        for i in range(0, len(answer_data['items'])):
            if answer_data['items'][i]['question_id'] == question_id:
                question_text.append(answer_data['items'][i]['body'])

        all_question_answer_text[question_id] = question_text

    return all_question_answer_text


def get_question_indices(questions):
    index_dict = defaultdict(list)

    for question in range(0, len(questions['items'])):
        question_id = questions['items'][question]['question_id']
        index_dict[question_id].append(question)

    return index_dict


def remove_duplicate_questions(questions):
    questions = dict(questions)
    curr_questions = len(questions['items'])

    index_dict = get_question_indices(question_data)
    for question_id in index_dict:
        index_dict[question_id] = index_dict[question_id][1:]

    joined_index_list = []
    for index in index_dict.values():
        joined_index_list = joined_index_list + index

    for index in sorted(joined_index_list, reverse=True):
        del questions['items'][index]

    print("Total deleted questions: " + str(curr_questions - len(questions['items'])))
    return questions


if __name__ == '__main__':
    # Load Question Data
    question_data = load_json_to_dict('data/data1605396201.json.json')
    question_data = remove_duplicate_questions(question_data)
    APIDump.export_json_to_file(question_data, 'nodupe')

    '''
    # Load Question Data
    question_data = load_json_to_dict('data/small_question_sample.json')
    question_ids = grab_all_question_ids(question_data)

    # Get answers using Question Data
    answer_data = APIDump.get_answers_for_questions(question_ids)

    # Combine question/answer information
    important_text = get_combined_qa_list(question_data, answer_data, question_ids)
    for question_id in important_text:
        print(question_id)
        print(important_text.get(question_id))
    '''
