from webexteamsbot import TeamsBot
from webexteamsbot.models import Response
from adaptivecardbuilder import *
import time
import json
import requests
import mod_skills as usefulP

teams_token = 'YmIxMDIzZWMtNjU3OS00ZjA0LThjN2UtMDE0NWIzNDJkMzk5Y2I0N2I5NzQtNGE1_P0A1_b34062fa-24f1-480f-a815-05d10d8cf4f2'

def show_card(incoming_msg):
    attachment = open("interfacecard.json").read()
    backupmessage = "You have an assignment!!!"

    c = create_message_with_attachment(
        incoming_msg.roomId, msgtxt=backupmessage, attachment=json.loads(attachment)
    )
    print(c)
    return ""


# An example of how to process card actions
def handle_cards(api, incoming_msg):
    """
    Function to handle card actions.
    :param api: webexteamssdk object
    :param incoming_msg: The incoming message object from Teams
    :return: A text or markdown based reply
    """
    m = get_attachment_actions(incoming_msg["data"]["id"])
    meeting = open("interfacecard.json").read()
    meeting = json.loads(meeting)
    # #print(meeting['content']['body'][0]['text'])
    usefulP.push_int(url='https://192.168.56.106/restconf',name=m['inputs']['name'], 
                     ip=m['inputs']['ip'],
                     netmask=m['inputs']['netmask'])
    return "New Interface Configured: {},\n {},\n {}".format(m["inputs"]["name"],
                                                    m['inputs']['ip'],
                                                    m['inputs']['netmask'])

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