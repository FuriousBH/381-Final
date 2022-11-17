import os
import sys
import myparamiko as m
### For RESTCONF
import requests
import json
import urllib3

from requests.auth import HTTPBasicAuth

# Skills for pushing configs

def push_int(url, name, username, password, headers, description, type, enabled, ip, netmask):
    """Function to push a change using RESTCONF"""
    url = url + "/data/ietf-interfaces:interfaces/interface=Loopback2"
    
    payload = """
        {
            "ietf-interfaces:interface": {
                "name": "Loopback2",
                "description": "FLASK TEST",
                "type": "iana-if-type:softwareLoopback",
                "enabled": true,
                "ietf-ip:ipv4": {
                    "address": [
                    {
                    "ip": "11.11.11.11",
                    "netmask": "255.255.255.0"
                    }
            ]
            },
            "ietf-ip:ipv6": {}
            }
        }
"""

    headers = {'Content-Type': 'application/yang-data+json', 'Accept': 'application/yang-data+json'}
    AUTH = HTTPBasicAuth('cisco', 'cisco123!')
    response = requests.put(url,
                              headers=headers,
                              auth=AUTH,
                              data=payload,
                              verify=False)
    
    return response.text


