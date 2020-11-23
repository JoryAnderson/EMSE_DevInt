import gc
import json
from collections import defaultdict


def load_json_to_dict(file):
    with open(file) as json_file:
        return json.load(json_file)


def grab_flat_question_id_list(questions):
    return [question['question_id'] for question in questions['items']]


# get_question_indices
# FOR USE WITH REMOVING DUPLICATE QUESTIONS
#   Get indices for where a question appears in the data set. Then slices the first index from each question.
#   Returns a dict: {question_id : [indices, ...]}
def get_duplicate_question_indices(questions):
    index_dict = defaultdict(list)

    for question in range(0, len(questions['items'])):
        question_id = questions['items'][question]['question_id']
        index_dict[question_id].append(question)

    # Slice first index of every question
    for question_id in index_dict:
        index_dict[question_id] = index_dict[question_id][1:]

    return index_dict


# Maps all question_ids to the indices used in the question JSON.
# You'd probably want to use this after running remove_duplicate_questions
# A dictionary entry looks like: {question_id: index}
def grab_unique_question_ids_and_indices(question_data):
    return {question_data['items'][i]['question_id']: i for i in range(0, len(question_data['items']))}


# Grabs user_ids from a JSON file, then returns a distinct set.
def grab_unique_user_ids(data):
    unique_user_ids = []
    for user in [post['owner'] for post in data['items']]:
        if user['user_type'] != "does_not_exist" and user['user_id'] not in unique_user_ids:
            unique_user_ids.append(user['user_id'])
    return unique_user_ids


def split_list_into_chunks(data, chunk_size):
    data = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    print("Number of chunks: ", len(data), "Size of chunk: ", len(data[0]))
    return data


# Maps question ids to answer indices from answer JSON to a . Allows for easy searching of answers  using a question id.
# Try passing a question_id to the dict and iterate over the index list to quickly find answers in the JSON.
# A dictionary entry looks like: {question_id: [answer_index1, answer_index2, ...]}
def grab_all_answer_indices(answer_data):
    result = defaultdict(list)
    for i in range(0, len(answer_data['items'])):
        answer = answer_data['items'][i]
        question_id = answer['question_id']
        result[question_id].append(i)

    return result


# get_combined_qa_list
#   Combines question and answer texts into a list of lists. Still requires processing. Returns a dictionary
#   {question_id : [question_title, question_body [answers, empty if none]]}
def get_combined_qa_list(question_data, answer_data):
    question_ids = grab_unique_question_ids_and_indices(question_data)
    all_question_answer_text = {}
    answer_indices = grab_all_answer_indices(answer_data)

    for question_id in question_ids:
        question_ind = question_ids[question_id]
        question = question_data['items'][question_ind]
        question_text = [question['title'], question['body'],
                         [answer_data['items'][index]['body'] for index in answer_indices[question_id]]]

        all_question_answer_text[question_id] = question_text

    return all_question_answer_text


# remove_duplicate_question
#   Returns a dataset with unique entries (i.e., no more than one instance of any question)
def remove_duplicate_questions(questions):
    curr_questions = len(questions['items'])
    print("Original number of questions: " + str(curr_questions))

    # Get {question_id : [index1, ...]}
    index_dict = get_duplicate_question_indices(questions)

    # Add duplicate question_ids to flat list
    joined_index_list = []
    for index in index_dict.values():
        joined_index_list = joined_index_list + index

    # Delete duplicate questions
    for index in sorted(joined_index_list, reverse=True):
        del questions['items'][index]
    gc.collect()

    # Delete excess questions (due to MemoryError), set to 100,000.
    joined_index_list = [x for x in range(100000, len(questions['items']))]
    for i in sorted(joined_index_list, reverse=True):
        del questions['items'][i]

    curr_questions = len(questions['items'])
    print("Number of unique questions: " + str(curr_questions))

    return questions
