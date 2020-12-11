from collections import defaultdict

import JSONReader
import matplotlib.pyplot as plt


def stratify_proportions(proportion_data):
    stratified_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for percentage in proportion_data:
        if percentage == 0:
            stratified_counts[0] = stratified_counts[0] + 1
        elif percentage < 0.1:
            stratified_counts[1] = stratified_counts[1] + 1
        elif percentage < 0.2:
            stratified_counts[2] = stratified_counts[2] + 1
        elif percentage < 0.3:
            stratified_counts[3] = stratified_counts[3] + 1
        elif percentage < 0.4:
            stratified_counts[4] = stratified_counts[4] + 1
        elif percentage < 0.5:
            stratified_counts[5] = stratified_counts[5] + 1
        elif percentage < 0.6:
            stratified_counts[6] = stratified_counts[6] + 1
        elif percentage < 0.7:
            stratified_counts[7] = stratified_counts[7] + 1
        elif percentage < 0.8:
            stratified_counts[8] = stratified_counts[8] + 1
        elif percentage < 0.9:
            stratified_counts[9] = stratified_counts[9] + 1
        elif percentage < 1:
            stratified_counts[10] = stratified_counts[10] + 1
        elif percentage == 1:
            stratified_counts[11] = stratified_counts[11] + 1
    return stratified_counts


def stratified_statistics_and_plot(stratified_counts):

    y_labels = ["0%", "1%-9%", "10%-19%", "20%-29%", "30%-39%", "40%-49%", "50%-59%", "60%-69%", "70%-79%", "80%-89%",
                "90%-99%", "100%"]
    y_pos = [i for i, _ in enumerate(y_labels)]

    num_of_users_with_answers = 0
    num_of_users_with_no_answers = stratified_counts[0]
    less_than_50_percent = num_of_users_with_no_answers
    more_than_50_percent = 0

    for collection in stratified_counts[1:6:]:
        num_of_users_with_answers = num_of_users_with_answers + collection
        less_than_50_percent = less_than_50_percent + collection

    for collection in stratified_counts[6::]:
        num_of_users_with_answers = num_of_users_with_answers + collection
        more_than_50_percent = more_than_50_percent + collection

    print("Percentage of users with no answers: " +
          str(num_of_users_with_no_answers / (num_of_users_with_no_answers + num_of_users_with_answers)))
    print("Num of no-answerers: " + str(num_of_users_with_no_answers))
    print("Num of answerers: " + str(num_of_users_with_answers))
    print("Percentage of users with more answers than questions: "
          + str(more_than_50_percent / (more_than_50_percent + less_than_50_percent)))
    print("Less than 50% answers: " + str(less_than_50_percent))
    print("More than 50% answers: " + str(more_than_50_percent))

    plt.barh(y_pos, stratified_counts)
    plt.yticks(y_pos, y_labels)
    plt.xscale("log")
    plt.xlabel("Number of users who have asked a question")
    plt.ylabel("The proportion of answers in each user's posts")


def sampled_answers_proportion(questions_data, answers_data):

    answer_user_occurrence_map = JSONReader.map_users_to_post(answers_data)
    questions_user_occurrence_map = JSONReader.map_users_to_post(questions_data)

    question_answer_proportions = []
    for user_id in questions_user_occurrence_map.keys():
        question_count = len(questions_user_occurrence_map[user_id])
        answer_count = len(answer_user_occurrence_map[user_id])
        if (answer_count + question_count) == 0:
            question_answer_proportions.append(0)
        else:
            question_answer_proportions.append(answer_count / (answer_count + question_count))

    stratified_counts = stratify_proportions(question_answer_proportions)
    stratified_statistics_and_plot(stratified_counts)


if __name__ == '__main__':

    answers = JSONReader.load_json_to_dict('data/answers_100k_full.json')
    questions = JSONReader.load_json_to_dict('data/nodupe_100k_from_236k.json')

    sampled_answers_proportion(questions, answers)
    plt.show()
