import json
import os
import sys
import time
import requests
import urllib
import hmac
import hashlib
import base64
import time

def perform_signed_oauthv1_request(param_dict):

    method = param_dict.get('method', "get").upper()
    url = param_dict['url']
    get_parameters = param_dict.get('get_parameters', {})
    post_parameters = param_dict.get('post_parameters', {})
    auth = {
        "oauth_consumer_key": param_dict['oauth_consumer_key'],
        "oauth_token": param_dict['oauth_token'],
        "oauth_signature_method": "HMAC-SHA1",
        "oauth_timestamp": "{0}".format(int(time.time())),
        "oauth_nonce": base64.b64encode(os.urandom(10)),
        "oauth_version": "1.0",
    }

    signable_parts = {**get_parameters, **post_parameters, **auth}

    authorisation_header_str = ""
    parameter_str = ""
    get_parameter_str = ""
    for key, value in  sorted(signable_parts.items(), key=lambda t: urllib.parse.quote_plus(t[0])):
        if len(parameter_str) > 0:
            parameter_str += "&"
        parameter_str += "{0}={1}".format(urllib.parse.quote_plus(key), urllib.parse.quote(value))

        if key in auth.keys():
            if len(authorisation_header_str) > 0:
                authorisation_header_str += ","
            authorisation_header_str += "{0}=\"{1}\"".format(urllib.parse.quote_plus(key), urllib.parse.quote(value))
        
        if key in get_parameters.keys():
            if len(get_parameter_str) == 0:
                get_parameter_str = "?"
            else:
                get_parameter_str += "&"
            get_parameter_str += "{0}={1}".format(urllib.parse.quote_plus(key), urllib.parse.quote(value))
    
    signable_str = "{0}&{1}&{2}".format(method, urllib.parse.quote_plus(url), urllib.parse.quote_plus(parameter_str))

    signing_key = "{0}&{1}" \
        .format(urllib.parse.quote_plus(param_dict['oauth_consumer_secret']), \
        urllib.parse.quote_plus(param_dict['oauth_token_secret']))

    signature = hmac.new(bytes(signing_key,'utf-8'), bytes(signable_str,'utf-8'), hashlib.sha1)
    signature = base64.b64encode(signature.digest()).decode('UTF-8')

    headers = {
        'Authorization': "OAuth {0},oauth_signature=\"{1}\"".format(authorisation_header_str, urllib.parse.quote_plus(signature)),
    }

    response = requests.request(method, url + get_parameter_str, headers=headers, data=post_parameters)
    return response
