# Ad-Hoc Python Scripts
A series of scripts which utilize the functions in the lib module.

## get_questions.py
* Grabs a specified number of questions. Can be passed two arguments
specifying query_size and num_of_queries. 

    * Defaults to (100, 10), which
is about ~1000 results. 

* Data will be placed in a data/ folder where script
is executed.

## compile_question_answer_text.py
* For a given dataset, this queries for all answers for each question and pairs them
appropriately. Returns a dictionary {question_id : list}.
    * list is composed as [question title, question_body, [answers]]

* MUST be passed a file path to a .json file.

## remove_duplicate_questions.py
* For a given dataset, this keeps one of each question, removing duplicates.

* Places resulting data inside data folder, labeled 'nodupe'
