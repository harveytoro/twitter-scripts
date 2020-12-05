
import os
import request_helper
from dotenv import load_dotenv

load_dotenv()

param_dict = {
    'get_parameters': {
        'screen_name':os.getenv("TD_USER_NAME")
    },
    'url':  "https://api.twitter.com/1.1/friends/ids.json",
    'method': 'get',
    'oauth_consumer_key':os.getenv("TD_OAUTH_CONSUMER_KEY"),
    'oauth_consumer_secret':os.getenv("TD_OAUTH_CONSUMER_SECRET"),
    'oauth_token':os.getenv("TD_OAUTH_TOKEN"),
    'oauth_token_secret':os.getenv("TD_OAUTH_TOKEN_SECRET")
}

response = request_helper.perform_signed_oauthv1_request(param_dict)

with open("following.json",'w') as f:
    f.write(response.text)