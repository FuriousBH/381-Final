### teams Bot ###
### Utilities Libraries
import routers
import pull_skills as useful
import Chatbot.mod_skillsBACKUP1 as usefulP
from webexteamsbot import TeamsBot
from webexteamsbot.models import Response

# Router Info 
device_address = routers.router['host']
device_username = routers.router['username']
device_password = routers.router['password']

# RESTCONF Setup
port = '443'
url_base = "https://{h}/restconf".format(h=device_address)
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}

# Bot Details
bot_email = 'sirbot@webex.bot'
teams_token = 'YmIxMDIzZWMtNjU3OS00ZjA0LThjN2UtMDE0NWIzNDJkMzk5Y2I0N2I5NzQtNGE1_P0A1_b34062fa-24f1-480f-a815-05d10d8cf4f2'
bot_url = "https://27ab-66-188-182-24.ngrok.io"
bot_app_name = 'CNIT-381 Network Auto Chat Bot'

# Create a Bot Object
#   Note: debug mode prints out more details about processing to terminal
bot = TeamsBot(
    bot_app_name,
    teams_bot_token=teams_token,
    teams_bot_url=bot_url,
    teams_bot_email=bot_email,
    debug=True,
    webhook_resource_event=[
        {"resource": "messages", "event": "created"},
        {"resource": "attachmentActions", "event": "created"},],
)

# A standard greeting
def greeting(incoming_msg):
    # Loopkup details about sender
    sender = bot.teams.people.get(incoming_msg.personId)

    # Create a Response object and craft a reply in Markdown.
    response = Response()
    response.markdown = "Hello {}, I'm a friendly CSR1100v assistant .  ".format(
        sender.firstName
    )
    response.markdown += "\n\nSee what I can do by asking for **/help**."
    return response

# Show the Interfaces on the Router
def get_int_ips(incoming_msg):
    response = Response()
    intf_list = useful.get_configured_interfaces(url_base, headers,device_username,device_password)

    if len(intf_list) == 0:
        response.markdown = "I don't have any information of this device"
    else:
        response.markdown = "Here is the list of interfaces with IPs I know. \n\n"
    for intf in intf_list:
        response.markdown +="*Name:{}\n" .format(intf["name"])
        try:
            response.markdown +="IP Address:{}\{}\n".format(intf["ietf-ip:ipv4"]["address"][0]["ip"],
                                intf["ietf-ip:ipv4"]["address"][0]["netmask"])
        except KeyError:
            response.markdown +="IP Address: UNCONFIGURED\n"
    return response

# Push a new interface to the Router
def push_new_int(incoming_msg):
    name = "Loopback2"
    description = "Test Push LO2"
    type = "iana-if-type:softwareLoopback"
    enabled = True
    ip = "11.1.1.1"
    netmask = "255.255.255.0"
    new_int = usefulP.push_int(url_base,
                               device_username, 
                               device_password,
                               headers,
                               name, 
                               description, 
                               type, 
                               enabled, 
                               ip, 
                               netmask)
    
    return new_int.text
# Set the Bot's greeting
bot.set_greeting(greeting)

# Add Bot's Commands

bot.add_command(
    "show interfaces", "List all interfaces and their IP addresses", get_int_ips)
bot.add_command(
    "new in", "Use PUSH to add a new interface", push_new_int)

if __name__ == "__main__":
    # Run Bot
    bot.run(host="0.0.0.0", port=5000)