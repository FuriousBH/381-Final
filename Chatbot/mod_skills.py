import os
import sys
import myparamiko as m
### For RESTCONF
import requests
import json
import urllib3

from requests.auth import HTTPBasicAuth

# Skills for pushing configs

# Adding an interface
def push_int(url, name, ip, netmask):
    """Function to push a change using RESTCONF"""
    url = url + "/data/ietf-interfaces:interfaces/interface=" + name
    
    payload = {
        "ietf-interfaces:interface": {
            "name": name,
            "description": "TEST DESCRIPTION",
            "type": "iana-if-type:softwareLoopback",
            "enabled": "true",
            "ietf-ip:ipv4": {
                "address": [
                    {
                    "ip": ip,
                    "netmask": netmask
                    }
            ]
            },
            "ietf-ip:ipv6": {}
        }
    }
    headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}
    AUTH = HTTPBasicAuth('cisco', 'cisco123!')
    response = requests.put(url,
                              headers=headers,
                              auth=AUTH,
                              data=json.dumps(payload),
                              verify=False)
    print("SUCCESS")
    
    return response

def delete_int(url, name, username, password):
    """Function to delete an interface"""
    url = url + "/data/ietf-interfaces:interfaces/interface=" + name
    
    payload = {}
    headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}
    
    response = requests.delete(url,
                               headers=headers,
                               auth=(username, password),
                               data=json.dumps(payload),
                               verify=False)
    return ""