import json
import APIDump


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


if __name__ == '__main__':
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