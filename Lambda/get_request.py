# This particular script requests api from a lambda list_buckets function
# but any api can be called with the request.get method

import requests
import json

x = requests.get('https://jpn4euqf70.execute-api.us-east-1.amazonaws.com')  # Can put any url here, good for api urls
print('Status Code:', x.status_code)

response_json = x.json()

for bucket in response_json:
    print(bucket)

# print(type(x)) # To print type
# print(dir(requests)) # to get all methods for module
