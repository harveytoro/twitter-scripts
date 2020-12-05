
import json
import os
import sys
import time
import requests
import request_helper
from dotenv import load_dotenv

load_dotenv()

def run():
    list_id = sys.argv[2]

    existing_list_ids = []
    with open(sys.argv[3]) as f:
        l = json.load(f)
        existing_list_ids = [u["id"] for u in l["users"]]

    print(len(existing_list_ids))

    with open(sys.argv[1]) as jsonFile:
        data = json.load(jsonFile)
        
        up_to_100 = []
        for user_id in data["ids"]:

            if user_id in existing_list_ids:
                continue

            up_to_100.append(user_id)

            if len(up_to_100) >= 100:
                add_to_list(up_to_100, list_id)
                up_to_100 = []
            
        if len(up_to_100) > 0:
            add_to_list(up_to_100, list_id)
            up_to_100 = []


def add_to_list(ids, list_id):
    
    param_dict = {
        'get_parameters': {
            'user_id':','.join(str(x) for x in ids),
            'list_id':list_id
        },
        'url':  "https://api.twitter.com/1.1/lists/members/create_all.json",
        'method': 'post',
        'oauth_consumer_key':os.getenv("TD_OAUTH_CONSUMER_KEY"),
        'oauth_consumer_secret':os.getenv("TD_OAUTH_CONSUMER_SECRET"),
        'oauth_token':os.getenv("TD_OAUTH_TOKEN"),
        'oauth_token_secret':os.getenv("TD_OAUTH_TOKEN_SECRET")
    }

    response = request_helper.perform_signed_oauthv1_request(param_dict)
    print(response.status_code)
    print("Waiting 60 seconds before next batch")
    time.sleep(60)

if __name__ == '__main__':
    run()

