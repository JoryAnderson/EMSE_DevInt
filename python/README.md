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
* Can be passed an optional second command line argument, specifying a starting index. Will grab
next 25k questions or until EOF is reached.

## remove_duplicate_questions.py
* For a given dataset (given by file path), this keeps one of each question, removing duplicates.

* Places output data inside data folder, labeled 'nodupe'

## split_text_code.py
Given two JSON file for questions and answers in argument:
* For each file:
	* split the body in each post into text and code
	* remove reserved key words in code
	* for questions, store (question_id, title, text, code) in a csv file; for answers, store (question_id, text, code) in another csv file

## create_csv.py
* Given a JSON file of question posts in argument:
	* split the body in each post into text and code
	* remove reserved key words in code
	* store (question_id, title, text, code) in csv format

## tokenize_csv.py
* combine the tile and text in the combined csv.
* this combined strings will be preproceesed using the tokenization.py in lib.
* the prepocessed data will be saved back as a new file togrhter with original data. the new file is also save to data_proceeed/ folder

## reserved_key_words.py
* List reserved key words (425) in source code using the infomation in this project:
   * https://github.com/AnanthaRajuCprojects/Reserved-Key-Words-list-of-various-programming-languages

## map_uname_qid.py
* Given a JSON file of question posts in argument, return a SQL file that contain a single table of (user name, question id) mapping for statistical purpose
* For RQ1: distribution of number of questions per questioner
