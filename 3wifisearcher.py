import requests
import json
import time

data = {"key": "23ZRA8UBSLsdhbdJMp7IpbbsrDFDLuBC", "bssid": "*", "essid": "timanovskiy", "sens": "True"}
headers = {"Content-Type": "application/json"}
r = requests.post("http://3wifi.stascorp.com/api/apiquery",
json=data,
headers=headers
)

k = r.text
dict = json.loads(k)

def print_pass():
    time.sleep(1)
    try:
        print(dict['data']['*|timanovskiy'][0]['key'])
    except:
        print_pass()
print_pass()
