import routers as R
import myparamiko as paramiko
from datetime import date


def router_select(router_name):
    routers = R.routers
    data = {}
    r_list = []
    r_list = routers.keys()
    if router_name not in r_list:
        return f"Router {router_name} is not present."
    else:
        for k, v in routers[router_name].items():
            data[k] = str(v)
    
    return data

def command_parser(incoming_message):
    """This is a parser that takes the incoming message
    and looks for a string that is associated with a router.
    While this could be refractored more, it will serve for now.
    Give us some extra room for odd commands."""
    r_list = R.routers.keys()
    device = ''
    for key in r_list:
        if key in incoming_message:
            device = key
    return device

def credentials_return(router_name):
    """Returns the credentials for the device"""
    device_dict = router_select(router_name)
    username = device_dict['username']
    password = device_dict['password']
    return username, password

def address_return(router_name):
    device_dict = router_select(router_name)
    address = device_dict['address']
    return address

def router_needs(router_name):
    username, password = credentials_return(router_name)
    address = address_return(router_name)
    return username, password, address

def my_paramiko_client_shell(address, username, password):
    """MyParamiko skill. To calm down some nonesense"""
    ssh_client = paramiko.connect(address, 22, username, password)
    shell = paramiko.get_shell(ssh_client)
    return shell

def datetime():
    today = date.today()
    print(today)
    return today

def to_text(string):
    export = string.text
    return export

def combine_two_strings(string1, string2):
    """Combining two strings to output as one string"""
    output = str(string1) + str(string2)
    return output