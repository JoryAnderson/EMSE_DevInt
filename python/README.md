# Ad-Hoc Python Scripts
A series of scripts which utilize the functions in the lib module.

## get_questions.py
* Grabs a specified number of questions. Can be passed two arguments (at terminal)
specifying **max_pages** and **starting_page**. Query size is limited to 100, 
so the maximum size of the response is equal to 100*max_pages.

    * **max_pages**: The maximum number of pages in the response. Each page consists of 100 questions.
    * **starting_page**: Specifies the page to start collecting data from, iterating forward until it either exhausts
    available data or reaches the **max_pages**
    * Defaults to (100, 1), which is about ~10000 results. 

* Data will be placed in a data/ folder where script
is executed.

## compile_question_answer_text.py
* For a given dataset, this queries for all answers for each question and pairs them
appropriately. Returns a dictionary {question_id : list}.
    * list is composed as [question title, question_body, [answers]]

* MUST be passed a file path to a .json file.

## remove_duplicate_questions.py
* For a given dataset (given by file path), this keeps one of each question, removing duplicates.

* Places output data inside data folder, labeled 'nodupe'

## split_text_code.py
* For a given JSON file of question posts, split the body in each post into text and code block(s), then save title, text, and each code
block into seperated files.
