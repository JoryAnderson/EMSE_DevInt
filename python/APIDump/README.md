# Retrieving Data

    QUERY_SIZE = 100
    NUM_OF_QUERIES = 100
**QUERY_SIZE**: The number of posts returned per API call

**NUM_OF_QUERIES**: The number of API calls.

Therefore, the number of results = **QUERY_SIZE * NUM_OF_QUERIES**

    posts = SITE.fetch('posts')

Returns the JSON data in a dictionary, 'posts' refers to the specified entry point 
(others include 'comments', 'answers', etc.). Post represents the entire query.

The script will export the resulting JSON to the data folder. 

# Specifying Data
    
**Below is an example of interacting with the dictionary response.**


    print(posts)
    > {'backoff': 10, 'has_more': True, 'page': 1, 'quota_max': 300, 'quota_remaining': 300, 'total': 0, 'items'...
The entire query

    print(posts['quota_remaining'])
    > 300
A portion of the header data.

    print(posts['items'][0])
    > {'owner': {'reputation': 1, 'user_id': 14635777, 'user_type': 'registered', 'profile_image':...
The first question / answer / post

    print(posts['items'][1])
    > {'owner': {'reputation': 65, 'user_id': 13592374, 'user_type': 'registered', 'profile_image':...

The second question / answer / post