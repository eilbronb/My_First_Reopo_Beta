import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://10.10.10.25/restconf'
https_header = {'content-type':'application/yang-data+json', 'accept':'application/yang-data+json'}

<<<<<<< HEAD
resp = requests.get(url, headers=https_header,  auth=('admin', 'password123'), verify=False)
json_resp = resp.json()
=======
resp = requests.get(f'{url}/data/Cisco-NX-OS-device:System/bgp-items/inst-items/dom-items/Dom-list?content=config', headers=https_header,  auth=('admin', 'password123'), verify=False)
json_resp = resp.json()
>>>>>>> d703b11111dc85abda05b0c621f8c52f85c79d82

print(resp.status_code)
print(resp.text)
print(json_resp)
