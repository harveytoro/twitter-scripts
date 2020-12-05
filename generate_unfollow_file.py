
import json
import os
import sys
import time
import requests
import request_helper
from dotenv import load_dotenv

load_dotenv()

def run():

    follower_ids = []
    with open(sys.argv[1]) as f:
        l = json.load(f)
        follower_ids = [uid for uid in l["ids"]]

    print("Followers: ",len(follower_ids))

    following_ids = []
    with open(sys.argv[2]) as f:
        l = json.load(f)
        following_ids = [uid for uid in l["ids"]]

    print("Following: ",len(following_ids))

    unfollow_ids = [uid for uid in following_ids if uid not in follower_ids]

    print("To unfollow: ",len(unfollow_ids)) 

    unfollow_obj = {
        "ids":unfollow_ids
    }
    with open("unfollow.json",'w') as f:
        f.write(json.dumps(unfollow_obj))



if __name__ == '__main__':
    run()
