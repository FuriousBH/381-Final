import core_skills as Core
import myparamiko as paramiko
import os
import ruamel.yaml
yaml = ruamel.yaml.YAML()
fileRShowRun="../Ansible/rShowRun.txt"
playbook='ansible-playbook ../Ansible/updateTunnel-Playbook.yaml'
vpnInt="GigabitEthernet2"
# showRun = open('../Ansible/rShowRun.txt', 'r').read().splitlines()
# splitShowRun = showRun[18].split(' ')
def update_vars(incoming_msg):
        #reads show run file and splits lines
    splitShowRun=''
    # Old
    # showRun = open('rShowRun.txt', 'r').read().splitlines()
    with open(fileRShowRun,"r") as f:
        for l_no,line in enumerate(f):
            if vpnInt in line:
                # Useful Debug
                # print('string found in a file')
                # print('Line Number:', l_no)
                # print('Line:', line)
                response=line
                splitShowRun=(line.split())
                # print(splitShowRun)
            
    # Old
    # splitShowRun = showRun[18].split(' ')
    #opens the vars.yaml file, changes the old info with the new information
    with open('../Ansible/vars.yaml', 'r') as read_file:
           contents = yaml.load(read_file)
           #Assign the previous IP info to the Old variable
           contents['oldIP'] = contents['newIP']
           #Updates the New variable with the new IP info
           contents['newIP'] = splitShowRun[1]
           

    #dumps new yaml file into output.yaml 
    with open('../Ansible/vars.yaml', 'w') as dump_file:
           yaml.dump(contents, dump_file)
    return f'''Searched for {vpnInt}
    Found {response}
    Updated IP to {splitShowRun[1]}'''

def update_tunnel():
    response=os.system(playbook)
    return f'Ran Update Tunnel Playbook\n'

def show_ip_brief(incoming_msg):
    if incoming_msg!='r2':
        router= Core.to_text(incoming_msg)
        router = Core.command_parser(router)
    else:
        router=incoming_msg
    
    username, password, address = Core.router_needs(router)
    
    f = open(fileRShowRun, 'w')
    shell = Core.my_paramiko_client_shell(address, username, password)
    response = paramiko.show(shell, "show ip int brief")
    f.writelines([response])
    f.close()
    return response

"""
# -------- Brock's Secret Stuff -----------------------
import os
import sys
import ruamel.yaml
yaml = ruamel.yaml.YAML()

# -----------------------------------------------------
"""