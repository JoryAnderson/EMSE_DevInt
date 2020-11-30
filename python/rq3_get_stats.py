import JSONReader
import matplotlib.pyplot as plt
import numpy as np


def num_posted_answers(answers_users):
    num_posted_answers_per_user = [user['answer_count'] for user in answers_users['items']]

    distinct_answer_counts = sorted(list(set(num_posted_answers_per_user)))
    num_of_devs = []
    five_or_more_answers = 0
    less_than_5_answers = 0
    for count in distinct_answer_counts:
        num_of_devs_per_count = num_posted_answers_per_user.count(count)
        num_of_devs.append(num_of_devs_per_count)
        if count >= 5:
            five_or_more_answers = five_or_more_answers + num_of_devs_per_count
        else:
            less_than_5_answers = less_than_5_answers + num_of_devs_per_count

    print("Total users who posted answers: " + str(five_or_more_answers + less_than_5_answers))
    print("Users with 5 or more answers: " + str(five_or_more_answers))
    print("Users with less than 5 answers: " + str(less_than_5_answers))
    print("Percentage of users with less than 5 answers: " +
          str(less_than_5_answers / (five_or_more_answers + less_than_5_answers)))

    plt.xlim(1, 150)
    plt.ylim(100, 100000)
    plt.xscale('linear')
    plt.yscale('log')
    plt.xlabel("Number of posted answers")
    plt.ylabel("Number of developers")
    plt.plot(distinct_answer_counts, num_of_devs)


def posts_as_percentages(users):
    percentages = []
    for user in users['items']:
        answer_count = user['answer_count']
        question_count = user['question_count']

        if (answer_count + question_count) == 0:
            percentages.append(0)
        else:
            percentages.append(answer_count / (answer_count + question_count))

    stratified_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for percentage in percentages:
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

    y_labels = ["0%", "1%-9%", "10%-19%", "20%-29%", "30%-39%", "40%-49%", "50%-59%", "60%-69%", "70%-79%", "80%-89%",
                "90%-99%", "100%"]
    y_pos = [i for i, _ in enumerate(y_labels)]

    num_of_users_with_answers = 0
    num_of_users_with_no_answers = stratified_counts[0]
    less_than_50_percent = 0
    more_than_50_percent = 0

    for collection in stratified_counts[1:6:]:
        num_of_users_with_answers = num_of_users_with_answers + collection
        less_than_50_percent = less_than_50_percent + collection

    for collection in stratified_counts[6::]:
        num_of_users_with_answers = num_of_users_with_answers + collection
        more_than_50_percent = more_than_50_percent + collection

    print("Percentage of users with no answers: " +
          str(num_of_users_with_no_answers/(num_of_users_with_no_answers + num_of_users_with_answers)))
    print("Num of no-answerers: " + str(num_of_users_with_no_answers))
    print("Num of answerers: " + str(num_of_users_with_answers))
    print("Percentage of users with more answers than questions: "
          + str(more_than_50_percent / (more_than_50_percent + less_than_50_percent)))
    print("Less than 50% answers: " + str(less_than_50_percent))
    print("More than 50% answers: " + str(more_than_50_percent))

    plt.barh(y_pos, stratified_counts)
    plt.yticks(y_pos, y_labels)
    plt.xlabel("Number of developers who have asked a question")
    plt.ylabel("The proportion of answers in each developer's posts")


if __name__ == '__main__':
    users_from_questions = JSONReader.load_json_to_dict('data/users_from_questions.json')
    users_from_answers = JSONReader.load_json_to_dict('data/users_from_answers.json')

    #plt.subplot(1, 2, 1)
    num_posted_answers(users_from_answers)
    #plt.subplot(1, 2, 2)
    #posts_as_percentages(users_from_questions)
    plt.show()
