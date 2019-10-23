import requests
import json
import random
API_URL = "https://abcd12345.execute-api.us-west-1.amazonaws.com/stage"

# unique ID -- uuid
message ={ "MessageID" : { "S" : str(random.randint(0,999999)) }, 
"type" : { "S" : "type" }, 
"page" : { "S" : "page"}}

headers = {'Content-Type':'application/json',
           'X-Api-Key':'abcd12345'}

for i in range(0,8):
    try:
        rr=requests.post(API_URL, data=json.dumps(message),headers=headers)
        rr
        print(rr)
        print("ok")
    except:
        print("error")    
