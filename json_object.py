__author__ = 'kathiria'

import requests
import json
from pprint import pprint


# globals #
web_url = 'http://16.78.126.214:8080/v2/apps/ankit-jain'
uid = 'root'
pwd = 'admin@123'


response = requests.get(web_url, auth=(uid, pwd))
jresponse = response.json()
jobject = json.dumps(jresponse)
json_object = json.loads(jobject)

print("*"*100)
pprint(json_object)
print("*"*100)

# read the specific keypair from the JSON data structure #


pprint(json_object['app']['container']['docker']['portMappings'][0]['servicePort'])
pprint(json_object['app']['container']['docker']['portMappings'][1]['servicePort'])
pprint(json_object['app']['container']['docker']['portMappings'][2]['servicePort'])