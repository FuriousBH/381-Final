import myparamiko as m
### For RESTCONF
import requests


# Function for looking at configured Interfaces
def get_configured_interfaces(url_base,headers,username,password):
    url = url_base + "/data/ietf-interfaces:interfaces"

    # this statement performs a GET on the specified url
    response = requests.get(url,
                            auth=(username, password),
                            headers=headers,
                            verify=False
                            )
    return response.json()["ietf-interfaces:interfaces"]["interface"]

# This is a test function for adaptive cards
def get_configured_interfaces_test(url_base,headers,username,password):
    url = url_base + "/data/ietf-interfaces:interfaces"

    # this statement performs a GET on the specified url
    response = requests.get(url,
                            auth=(username, password),
                            headers=headers,
                            verify=False
                            )
    return response.json()["ietf-interfaces:interfaces"]["interface"]

