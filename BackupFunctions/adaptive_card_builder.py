from webexteamsbot import TeamsBot
from webexteamsbot.models import Response
from adaptivecardbuilder import *
import time
import json
import requests
import mod_skills as usefulP


def test_card(int_list):
    """Testing adaptive cards"""
    card = AdaptiveCard()
    response = Response()
    
    for int in int_list:
        card.add(TextBlock(text=f"Name: {int['ietf-ip:ipv4']}",
                           size= "Medium", weight="Bolder"))
    card_data = json.loads(asyncio.run(card.to_json()))
    
    card_payload = {
        "contentType": "application/vnd.microsoft.card.adaptive",
        "content": card_data,
    }
    response.text = "Test Card"
    response.attachments = card_payload
    
    return response