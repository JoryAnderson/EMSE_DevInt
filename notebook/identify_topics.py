import numpy as np

answer_text = "using net server file java gt git"
answer_list = answer_text.split(" ")

topic1_list = np.array(["error", "android", "code", "change", "form", "project", "windows", "test", "app", "ios"])
topic2_list = np.array(["quot", "error", "file", "using", "image", "php", "get", "command", "time", "android"])
topic3_list = np.array(["using", "net", "server", "file", "java", "gt", "git", "lt", "js", "node"])
# topic4_list = np.array(["python", "list", "array", "text", "studio", "get", "android", "data", "javascript", "using"])
# topic5_list = np.array(["string", "use", "date", "using", "python", "convert", "script", "get", "file", "multiple"])

all_topics = np.array([topic1_list, topic2_list, topic3_list])
# all_topics = np.array([topic1_list, topic2_list, topic3_list, topic4_list, topic5_list])

count_list = np.array([0, 0, 0])
# count_list = np.array([count1, count2, count3, count4, count5])

for i in range(len(all_topics)):
    print(i)

    curr_topic_list = all_topics[i]

    for t in range(len(curr_topic_list)):

        curr_word = curr_topic_list[t]

        if curr_word in answer_list:

            count_list[i] = count_list[i] + 1


print(count_list)
idx_max = np.argmax(count_list)
print(idx_max)

print("Assign to Topic", idx_max + 1)

