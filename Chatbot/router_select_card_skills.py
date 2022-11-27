from webexteamsbot import TeamsBot
from webexteamsbot.models import Response
from adaptivecardbuilder import *
import time
import json
import requests

teams_token = 'YmIxMDIzZWMtNjU3OS00ZjA0LThjN2UtMDE0NWIzNDJkMzk5Y2I0N2I5NzQtNGE1_P0A1_b34062fa-24f1-480f-a815-05d10d8cf4f2'

def select_router_card(incoming_msg):
    attachment = open("./Cards/router_select.json").read()
    backupmessage = "A dropdown menu for selecting the router"
    
    
    c = create_message_with_attachment(
        incoming_msg.roomId, msgtxt=backupmessage, attachment=json.loads(attachment)
    )
    print(c)
    return""

def handle_select_router_card(api, incoming_msg):
    """
    Function to handle card actions.
    :param api: webexteamssdk object
    :param incoming_msg: The incoming message object from Teams
    :return: A text or markdown based reply
    """
    m = get_attachment_actions(incoming_msg)
    meeting = open("./Cards/router_select.json").read()
    meeting = json.loads(meeting)
    # #print(meeting['content']['body'][0]['text'])
    print(meeting)
    
    
def create_message_with_attachment(rid, msgtxt, attachment):
    headers = {
        "content-type": "application/json; charset=utf-8",
        "authorization": "Bearer " + teams_token,
    }

    url = "https://api.ciscospark.com/v1/messages"
    data = {"roomId": rid, "attachments": [attachment], "markdown": msgtxt}
    response = requests.post(url, json=data, headers=headers)
    return response.json()

def get_attachment_actions(attachmentid):
    headers = {
        "content-type": "application/json; charset=utf-8",
        "authorization": "Bearer " + teams_token,
    }

    url = "https://api.ciscospark.com/v1/attachment/actions/" + attachmentid
    response = requests.get(url, headers=headers)
    return response.json()