import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = 'https://10.10.10.25/ins'
https_header = {'content-type':'application/json-rpc'}

reqList = []
showList = []

reqItem1 = {
    "jsonrpc":"2.0",
    "method":"cli",
    "params": {"cmd": "vlan 2", "version": 1},
    "id": 1
}
reqList.append(reqItem1)

reqItem2 = {
    "jsonrpc":"2.0",
    "method":"cli",
    "params": {"cmd":"interface vlan 2", "version": 1 },
    "id": 1
}
reqList.append(reqItem2)

reqItem3 = {
    "jsonrpc":"2.0",
    "method":"cli",
    "params": {"cmd":"ip address 200.200.200.254 255.255.255.0", "version": 1},
    "id": 1
}
reqList.append(reqItem3)

showItem1 = {
    "jsonrpc":"2.0",
    "method":"cli",
    "params": {"cmd":"show ip interface brief", "version": 1},
    "id": 1
}
showList.append(showItem1)

showItem2 = {
    "jsonrpc":"2.0",
    "method":"cli",
    "params": {"cmd":"show version" , "version": 1},
    "id": 1
}
showList.append(showItem2)


https_payload = json.dumps(reqList)
resp = requests.post(url, data=https_payload, headers=https_header, auth=('admin' , 'password123'), verify=False)
json_resp = resp.json()


#Creating another call for the show command
http_resp = json.dumps(showList)
resp1 = requests.post(url, data=http_resp, headers=https_header ,  auth=('admin' , 'password123'), verify=False)
json_resp1 = resp1.json()


#creating a map to get to Data
print(json_resp1)
