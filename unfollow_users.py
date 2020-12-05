
import json
import os
import sys
import time
import requests
import request_helper
from dotenv import load_dotenv

load_dotenv()

def run():

    current_following = []
    with open(sys.argv[2]) as f:
        l = json.load(f)
        current_following = [uid for uid in l["ids"]]

    print(len(current_following))

    with open(sys.argv[1]) as jsonFile:
        data = json.load(jsonFile)
        
        have_unfollowed = 0
        for user_id in data["ids"]:

            if user_id not in current_following:
                continue

            unfollow_user(user_id)
            have_unfollowed += 1

            if have_unfollowed >= 100:
                have_unfollowed = 0
                time.sleep(60)

def unfollow_user(id):
    
    param_dict = {
        'get_parameters': {
            'user_id':"{0}".format(id)
        },
        'url':  "https://api.twitter.com/1.1/friendships/destroy.json",
        'method': 'post',
        'oauth_consumer_key':os.getenv("TD_OAUTH_CONSUMER_KEY"),
        'oauth_consumer_secret':os.getenv("TD_OAUTH_CONSUMER_SECRET"),
        'oauth_token':os.getenv("TD_OAUTH_TOKEN"),
        'oauth_token_secret':os.getenv("TD_OAUTH_TOKEN_SECRET")
    }

    response = request_helper.perform_signed_oauthv1_request(param_dict)
    print("Unfollowed: ", id)

if __name__ == '__main__':
    run()

