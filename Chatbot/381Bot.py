### teams Bot ###
### Utilities Libraries
import routers
import pull_skills as useful
import mod_skills as usefulP
import card_skills as usefulC
import sub_mdt_file
import myparamiko as paramiko
import core_skills as Core
import monitor_init
from webexteamsbot import TeamsBot
from webexteamsbot.models import Response

# -------- Brock's Secret Stuff -----------------------
import sys
import ruamel.yaml
yaml = ruamel.yaml.YAML()

showRun = open('rShowRun.txt', 'r').read().splitlines()
# -----------------------------------------------------

# RESTCONF Setup
port = '443'
url_base = "https://{h}/restconf"
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}

# Bot Details
bot_email = 'sirbot@webex.bot'
teams_token = 'YmIxMDIzZWMtNjU3OS00ZjA0LThjN2UtMDE0NWIzNDJkMzk5Y2I0N2I5NzQtNGE1_P0A1_b34062fa-24f1-480f-a815-05d10d8cf4f2'
bot_url = "https://f94e-66-188-182-24.ngrok.io"
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
    device_name = Core.to_text(incoming_msg)
    # device_name = device_name[16:]
    device_name = Core.command_parser(device_name)
    device_dict = Core.router_select(device_name)
    intf_list = useful.get_configured_interfaces(url_base.format(h=device_dict['address']), headers, device_dict['username'], device_dict['password'])

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
# This function is spefically for Ansible
def show_run_config(incoming_msg):
    """Use paramiko to show the running configuration, and print add it to a directory"""
    # Todo: Make a method for selecting a specific router
    response = Response()
    router= Core.to_text(incoming_msg)
    router = Core.command_parser(router)
    username, password, address = Core.router_needs(router)
    
    f = open('/home/devasc/381-Final/Ansible/rShowRun.txt', 'w')
    shell = Core.my_paramiko_client_shell(address, username, password)
    response = paramiko.show(shell, "show run | section include crypto isakmp")
    f.writelines([response])
    f.close()
    
    return response

def show_dhcp_lease(incoming_msg):
    """Make use of Paramiko to pull the 'show dhcp lease' command output"""
    response = Response()
    router = Core.to_text(incoming_msg)
    router = Core.command_parser(router)
    username, password, address = Core.router_needs(router)
    filename = Core.combine_two_strings(router, 'dhcp_lease.txt')

    f = open('Outputs/' + filename, 'w')
    shell = Core.my_paramiko_client_shell(address, username, password)
    response = paramiko.show(shell, "show dhcp lease")
    f.writelines([response])
    f.close()    

    return response

def delete_int(incoming_msg):
    """Delete an interface. Use 
    delete int 'int name'"""
    # Delete int will require a different parser.
    response = Response()
    message_input = Core.to_text(incoming_msg)
    message_input = message_input[11:]
    name = message_input[:2]
    interface = message_input[3:]
    device_dict = Core.router_select(name)
    
    usefulP.delete_int(url_base.format(h=device_dict['address']), interface, device_dict['username'], device_dict['password'])
    response.markdown += "Deleted interface " + interface + "On device: " + name
    return response

#Docker
def check_docker(incoming_msg):
    response = Response()
    response.markdown+=usefulP.check_docker()
    return response
def run_docker(incoming_msg):
    response = Response()
    response.markdown+=usefulP.run_docker()
    return response

#Monitor
def init_monitor(incoming_msg):
    response = Response()
    response.markdown+=usefulP.monitor_init.run()
    return response
def del_cron(incoming_msg):
    response = Response()
    response.markdown+=usefulP.monitor_init.delete_cron()
    return response

def push_subs(incoming_msg):
    """Keith's Subscription stuff, just testing"""
    response = Response()
    subscriptions = sub_mdt_file.setup()
    
    response.markdown = f"Shut down {subscriptions}"
    
    return response

# -------- Brock's Secret Stuff -----------------------
def update_vars(incoming_msg):
    response = Response()
    #reads show run file and splits lines
    showRun = open('rShowRun.txt', 'r').read().splitlines()

    #opens the vars.yaml file, changes the old info with the new information
    with open('vars.yaml', 'r') as read_file:
           contents = yaml.load(read_file)
           #print(contents)
           #Assign the previous IP info to the Old variable
           contents['oldCrypto'] = contents['newCrypto']
           contents['oldSetPeer'] = contents['newSetPeer']
           #Updates the New variable with the new IP info
           contents['newCrypto'] = showRun[5]
           contents['newSetPeer'] = showRun[14]
           #print(contents)

    #dumps new yaml file into output.yaml 
    with open('vars.yaml', 'w') as dump_file:
           yaml.dump(contents, dump_file)
    return response
# -----------------------------------------------------


# Set the Bot's greeting
bot.set_greeting(greeting)

# Add Bot's Commands
# -------- Riley's Clean Stuff -----------------------
bot.add_command("show interfaces", "SYNTAX: show interfaces 'device'", get_int_ips)
bot.add_command("attachmentActions", "*", usefulC.handle_make_int_card)
bot.add_command("make int", "show an adaptive card", usefulC.show_make_int_card)
# bot.add_command("make int", "show an adaptive card", make_int_card--Riley--)
bot.add_command("delete int", "SYNTAX: delete int 'device' 'int_name'", delete_int)
bot.add_command("show run", "SYNTAX: show run 'device'", show_run_config)
bot.add_command("show dhcp lease", "SYNTAX: 'show dhcp lease 'device'", show_dhcp_lease)
bot.add_command("delete docker", "Deletes the container from docker", usefulP.delete_docker)
# -----------------------------------------------------
# -------- Brock's Secret Stuff -----------------------
bot.add_command("update vars", "Updating Vars", update_vars)
# -----------------------------------------------------
# -------- Keith's Public Stuff -----------------------
bot.add_command("check docker", "Check Docker image", usefulP.check_docker)
bot.add_command("run docker", "Runs the docker image jeremycohoe/tig_mdt", usefulP.run_docker)
bot.add_command("clean docker", "Stops docker, and removes the container", usefulP.cleanup_docker)
bot.add_command("vpn automate","runs monitor initialization with cron jobs and ansible",monitor_init.run)
bot.add_command("cron delete","Purely for lab purposes, remove corn jobs from vpn automate",monitor_init.delete_cron)
# bot.add_command("add subs", "Adds subscriptions from subscriptions.yml",push_subs)

# -----------------------------------------------------

if __name__ == "__main__":
    # Run Bot
    bot.run(host="0.0.0.0", port=5000)
