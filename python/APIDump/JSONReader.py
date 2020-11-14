import json
import APIDump


def load_json_to_dict(file):
    with open(file) as json_file:
        return json.load(json_file)


def grab_all_question_ids(data):
    return [data['items'][i]['question_id'] for i in range(0, len(data['items']))]


# For each question:
#   Get question title and text
#   Get the answers for each question
#   For each answer
#       Grab each answer text
#       Append answer text to question title/text
def get_combined_qa_list(question_data, answer_data, question_ids):
    all_question_answer_text = []

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

        all_question_answer_text.append(question_text)

    return all_question_answer_text


if __name__ == '__main__':
    # Load Question Data
    question_data = load_json_to_dict('data/data1605387199.json')
    question_ids = grab_all_question_ids(question_data)
    print(question_ids)

    # Get answers using Question Data
    answer_data = APIDump.get_answers_for_questions(question_ids)

    # Combine question/answer information
    important_text = get_combined_qa_list(question_data, answer_data, question_ids)
    print(important_text[0])
    print(important_text[1])
