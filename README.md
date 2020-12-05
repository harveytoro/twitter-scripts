# Twitter Scripts

Scripts used to clean up a Twitter account. 

## Usage

There are 7 scripts to facilitate obtaining information about your twitter account and then adding members to lists and removing followers.

First you will need a Twitter V1 API app, the consumer key / secret for the app and the access token / secret for your account should be placed in a .env file (see: example.env) for details.

- `get_followers.py` : no command line arguments : will output a file called followers.json

- `get_following.py` : no command line arguments : will output a file called following.json

- `get_lists.py` : no command line arguments : will output a file called lists.json

- `get_list_members.py` : requires a single command line argument of the list_id which can be obtained by looking in the lists.json file : will output a file called lists_members.json

- `add_to_list.py` : 3 command line arguments required
    1. should be the file containing the members to add to the list, so following.json
    2. the list id, obtained by looking in lists.json for the required list
    3. the file containing the current members of the list, so lists_members.json

this script will add members from following.json to the specified list, who are not already a member.

- `generate_unfollow_file.py` : 2 command line arguments required
    1. should be the followers.json file
    2. should be the following.json file

will output a unfollow.json file that contains all the ids of users you are following that are not following you back.

- `unfollow_users.py` : 2 command line arguments required
    1. should be the file containing the ids to unfollow, so unfollow.json
    2. should be the current following file, so following.json




These scripts do not handle paging or Twitter rate limits, for small accounts that might not be an issue. However for the scripts that perform actions (`add_to_list.py` and `unfollow_users.py`) it is expected that the `lists_members.json` and `following.json` files be regenerated between independent runs, so that you do not duplicate trying to add members already in the list or unfollow members you are no longer following.
