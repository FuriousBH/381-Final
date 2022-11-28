import os
import sys
import routers as R
from datetime import date


def router_select(router_name):
    routers = R.routers
    data = {}
    r_list = []
    name = ''
    r_list = routers.keys()
    if router_name not in r_list:
        return f"Router {router_name} is not present."
    else:
        for k, v in routers[router_name].items():
            data[k] = str(v)
    
    return data

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