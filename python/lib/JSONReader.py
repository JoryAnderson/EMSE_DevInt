import json
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
            answers = []
            if answer_data['items'][i]['question_id'] == question_id:
                answers.append(answer_data['items'][i]['body'])

        question_text.append(answers)
        all_question_answer_text[question_id] = question_text

    return all_question_answer_text


# get_question_indices
#   Get indices for where a question appears in the data set.
#   Returns a dict: {question_id : [indices, ...]}
def get_question_indices(questions):
    index_dict = defaultdict(list)

    for question in range(0, len(questions['items'])):
        question_id = questions['items'][question]['question_id']
        index_dict[question_id].append(question)

    return index_dict


# remove_duplicate_question
#   Returns a dataset with unique entries (i.e., no more than one instance of any question)
def remove_duplicate_questions(questions):
    questions = dict(questions)
    curr_questions = len(questions['items'])

    index_dict = get_question_indices(questions)
    for question_id in index_dict:
        index_dict[question_id] = index_dict[question_id][1:]

    joined_index_list = []
    for index in index_dict.values():
        joined_index_list = joined_index_list + index

    for index in sorted(joined_index_list, reverse=True):
        del questions['items'][index]

    print("Total deleted questions: " + str(curr_questions - len(questions['items'])))
    return questions
