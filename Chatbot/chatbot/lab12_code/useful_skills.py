import os
import sys
import myparamiko as m
### For RESTCONF
import requests
import json
import urllib3

def get_arp(url_base,headers,username,password):
    url = url_base + "/data/Cisco-IOS-XE-arp-oper:arp-data/"

    # this statement performs a GET on the specified url
    response = requests.get(url,
                            auth=(username, password),
                            headers=headers,
                            verify=False
                            )

    # return the json as text
    return response.json()['Cisco-IOS-XE-arp-oper:arp-data']['arp-vrf'][0]['arp-oper']


def get_sys_info(url_base,headers,username,password):
    url = url_base + "/data/Cisco-IOS-XE-device-hardware-oper:device-hardware-data/"

    # this statement performs a GET on the specified url
    response = requests.get(url,
                            auth=(username, password),
                            headers=headers,
                            verify=False
                            )

    # return the json as text
    return response.json()["Cisco-IOS-XE-device-hardware-oper:device-hardware-data"]["device-hardware"]

# Function to retrieve the list of interfaces on a device
def get_configured_interfaces(url_base,headers,username,password):
    url = url_base + "/data/ietf-interfaces:interfaces"

    # this statement performs a GET on the specified url
    response = requests.get(url,
                            auth=(username, password),
                            headers=headers,
                            verify=False
                            )
    return response.json()["ietf-interfaces:interfaces"]["interface"]

# A function to show IP protocols on the device
def get_acl_lists(url_base, headers, username, password):
    url = url_base + "data/Cisco-IOS-XE-acl-oper:access-lists"
    
    # this statement performs a GET on the specified URL
    response = requests.get(url,
                            auth=(username, password),
                            headers=headers,
                            verify=False
                            )
    return response.json()["Cisco-IOS-XE-acl-oper:access-lists"]

# Test Get DHCP Information
def get_dhcp_info(url_base, headers, username, password):
    http = urllib3.PoolManager()
    url = url_base + "data/Cisco-IOS-XE-dhcp-oper:dhcp-oper-data"
    response = http.request('GET', url)
    return response.data.decode('utf-8')
"""
# Get DHCP Information
def get_dhcp_info(url_base, headers, username, password):
    url = url_base + "data/Cisco-IOS-XE-dhcp-oper:dhcp-oper-data"
    
    response = requests.get(url,
                            auth=(username, password),
                            headers=headers,
                            verify=False
                            )
    return response.json()["Cisco-IOS-XE-dhcp-oper:dhcp-oper-data"]['dhcpv4-client-oper']
"""
if __name__ == "__main__":
    import routers
    # Router Info 
    device_address = routers.router['host']
    device_username = routers.router['username']
    device_password = routers.router['password']
    # RESTCONF Setup
    port = '443'
    url_base = "https://{h}/restconf".format(h=device_address)
    headers = {'Content-Type': 'application/yang-data+json',
            'Accept': 'application/yang-data+json'}

    intf_list = get_configured_interfaces(url_base, headers,device_username,device_password)
    for intf in intf_list:
        print("Name:{}" .format(intf["name"]))
        try:
            print("IP Address:{}\{}\n".format(intf["ietf-ip:ipv4"]["address"][0]["ip"],
                                intf["ietf-ip:ipv4"]["address"][0]["netmask"]))
        except KeyError:
            print("IP Address: UNCONFIGURED\n")