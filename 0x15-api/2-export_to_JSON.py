#!/usr/bin/python3
'''
Export data in the JSON format.
'''

import json
import requests
from sys import argv

if __name__ == '__main__':
    uid = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(uid)
    user = requests.get(url, verify=False).json()
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(uid)
    todo = requests.get(url, verify=False).json()
    name = user.get('username')
    k = [{"task": k.get("title"),
          "username": name,
          "completed": k.get("completed")} for k in todo]
    bj = {}
    bj[uid] = k
    with open("{}.json".format(uid), 'w') as filejs:
        json.dump(bj, filejs)
