import os
import sys
import myparamiko as m
### For RESTCONF
import requests
import json
import urllib3

from requests.auth import HTTPBasicAuth

# Skills for pushing configs

def push_int(url, name, description, ip, netmask):
    """Function to push a change using RESTCONF"""
    url = url + "/data/ietf-interfaces:interfaces/interface=Loopback2"
    
    payload = {
        "ietf-interfaces:interface": {
            "name": name,
            "description": description,
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
    
    return response


