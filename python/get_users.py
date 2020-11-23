import JSONReader
import APIDump
import sys


# Gets user information from provided JSON file.
# Argument 1: JSON file path
# Argument 2 (optional): Starting index, grabs information from next 25k users, or until EOF.
if __name__ == '__main__':
    assert len(sys.argv) >= 2

    # Grab JSON and pull user_ids from it
    data = JSONReader.load_json_to_dict(sys.argv[1])
    user_ids = JSONReader.grab_unique_user_ids(data)

    if len(sys.argv) == 3:
        # Grab next 25k questions from starting index
        start_index = int(sys.argv[2])
        end_index = min(start_index + 25000, len(user_ids))
        user_ids = user_ids[start_index:end_index]

    # Split questions into chunks of size 100 (due to API limitations)
    user_ids = JSONReader.split_list_into_chunks(user_ids, 100)

    # Get answers using Question Data
    SITE = APIDump.config_api(100)
    user_data = APIDump.get_users_from_ids(SITE, user_ids[0])

    # Get user info from question_user_ids in batches and merge
    for split in user_ids[1::]:
        response = APIDump.get_users_from_ids(SITE, split)
        user_data['items'].extend(response['items'])

    # Export to file
    APIDump.export_json_to_file(user_data, "users")

