import requests
import json

url = 'https://10.10.10.25/ins'
https_header = {'content-type':'application/json-rpc'}

reqList = []
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

https_payload = json.dumps(reqList)
resp = requests.post(url, data=https_payload, headers=https_header, auth=('admin' , 'password123'))
json_resp = resp.json()
