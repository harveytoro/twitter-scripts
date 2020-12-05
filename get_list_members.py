
import os
import sys
import request_helper
from dotenv import load_dotenv

load_dotenv()

param_dict = {
    'get_parameters': {
        'list_id':sys.argv[1],
        'count':'5000'
    },
    'url':  "https://api.twitter.com/1.1/lists/members.json",
    'method': 'get',
    'oauth_consumer_key':os.getenv("TD_OAUTH_CONSUMER_KEY"),
    'oauth_consumer_secret':os.getenv("TD_OAUTH_CONSUMER_SECRET"),
    'oauth_token':os.getenv("TD_OAUTH_TOKEN"),
    'oauth_token_secret':os.getenv("TD_OAUTH_TOKEN_SECRET")
}

response = request_helper.perform_signed_oauthv1_request(param_dict)

with open("lists_members.json",'w') as f:
    f.write(response.text)