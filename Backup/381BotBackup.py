### teams Bot ###
### Utilities Libraries
import routers
import pull_skills as useful
import mod_skills as usefulP
import card_skills as usefulC
import docker_run as docker
import myparamiko as paramiko
from webexteamsbot import TeamsBot
from webexteamsbot.models import Response
from datetime import date

device_username = routers.credentials['username']
device_password = routers.credentials['password']
# Router 1 Info
r1_address = routers.routers['r1']['address']
# Router 2 Info
r2_address = routers.routers['r2']['address']

# RESTCONF Setup
port = '443'
url_base_1 = "https://{h}/restconf".format(h=r1_address)
url_base_2 = "https://{h}/restconf".format(h=r2_address)
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}

# Bot Details
bot_email = 'sirbot@webex.bot'
teams_token = 'YmIxMDIzZWMtNjU3OS00ZjA0LThjN2UtMDE0NWIzNDJkMzk5Y2I0N2I5NzQtNGE1_P0A1_b34062fa-24f1-480f-a815-05d10d8cf4f2'
bot_url = "https://07e4-66-188-182-24.ngrok.io"
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
    intf_list = useful.get_configured_interfaces(url_base_1, headers,device_username,device_password)

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

# Function for pulling the running configuration
def show_run_config(incoming_msg):
    """Use paramiko to show the running configuration, and print add it to a directory"""
    response = Response()
    today = date.today()
    name = str(r1_address) + str(today)
    
    f = open('Outputs/'+name , 'w')
    ssh_client = paramiko.connect(r1_address, 22, device_username, device_password)
    shell = paramiko.get_shell(ssh_client)
    response = paramiko.show(shell, "show run")
    f.writelines([response])
    
    return response
    
def delete_int(incoming_msg):
    """Delete an interface. Use 
    delete int 'int name'"""
    response = Response()
    
    name = incoming_msg.text
    name = name[11:]
    
    usefulP.delete_int(url_base_1, name, device_username, device_password)
    response.markdown += "Deleted interface " + name 
    return response

# Commands for interacting with Docker
def check_docker(incoming_msg):
    """Makes use of Keith's lib. Nothing to add atm"""
    response = Response()
    check = docker.Docker_Check()

    response.markdown = f"{check}"
    
    return response

def run_docker(incoming_msg):
    """Keith's Docker stuff, just testing atm"""
    response = Response()
    run = docker.Docker_Run()
    response.markdown = f"{run}"
    
    return response

def cleanup_docker(incoming_msg):
    """Keith's Docker Stuff, just testing"""
    response = Response()
    container_id = docker.Docker_Cleanup()
    
    response.markdown = f"Shut down {container_id}"
    
    return response

# Set the Bot's greeting
bot.set_greeting(greeting)

# Add Bot's Commands
bot.add_command(
    "show interfaces", "List all interfaces and their IP addresses", get_int_ips)
bot.add_command("check docker", "Check Docker image", check_docker)
bot.add_command("run docker", "Runs the docker image jeremycohoe/tig_mdt", run_docker)
bot.add_command("clean docker", "Stops docker, and removes the container", cleanup_docker)
bot.add_command("attachmentActions", "*", usefulC.handle_make_int_card)
bot.add_command("make int", "show an adaptive card", usefulC.show_make_int_card)
bot.add_command("delete int", "Delete an interface. 'delete int int_name'", delete_int)
bot.add_command("show run", "Shows the running configuration of router", show_run_config)

if __name__ == "__main__":
    # Run Bot
    bot.run(host="0.0.0.0", port=5000)
