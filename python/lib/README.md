# Retrieving Data

1. Call APIDump.config_api(query_size, num_of_queries) to initialize a StackAPI object.
    2.  Default Values:
        * query_size: 100
        * num_of_queries: 10
        
        Produces ~1000 results. Can be modified to produce more or less data.
        
2. Call get_question or get_answers_for_questions to send a request to the API. 
Returns a dictionary containing the data.
    * JSONReader contains useful functions for operating on the data.
    
# Specifying Data
    
**Below is an example of interacting with the dictionary response.**


    print(data)
    > {'backoff': 10, 'has_more': True, 'page': 1, 'quota_max': 300, 'quota_remaining': 300, 'total': 0, 'items'...
The entire query

    print(data['quota_remaining'])
    > 300
A portion of the header data.

    print(data['items'][0])
    > {'owner': {'reputation': 1, 'user_id': 14635777, 'user_type': 'registered', 'profile_image':...
The first question / answer / post

    print(data['items'][1])
    > {'owner': {'reputation': 65, 'user_id': 13592374, 'user_type': 'registered', 'profile_image':...

The second question / answer / post

    print(data['items'][0]['user_id']
    > 14635777
    
An attribute within a question / answer / post

# Storing Data
* APIDump has an export_json_to_file(data, file_name) function, which allows you to store a hard copy of the JSON data.
    * file_name is an optional parameter, which will have a time-stamp appended to it when saved.
    
# Tockening strings
* tokenization.py include the wrapper for nltk toolkit for preprocessing data. The most important method is process (title).
