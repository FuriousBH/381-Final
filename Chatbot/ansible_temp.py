import core_skills as Core
import myparamiko as paramiko
import os
import ruamel.yaml
yaml = ruamel.yaml.YAML()
fileRShowRun="../Ansible/rShowRun.txt"
vpnInt="GigabitEthernet2"
# showRun = open('../Ansible/rShowRun.txt', 'r').read().splitlines()
# splitShowRun = showRun[18].split(' ')
# def update_vars(incoming_msg):
        #reads show run file and splits lines
splitShowRun=''
# Old
# showRun = open('rShowRun.txt', 'r').read().splitlines()
with open(fileRShowRun,"r") as f:
    for line in enumerate(f):
        # if vpnInt in line:
        #     print(line)
        #     splitShowRun=line.split(' ')
        for line in enumerate(f):
            if vpnInt in line:
                # Useful Debug
                print('string found in a file')
                # print('Line Number:', l_no)
                print('Line:', line)
                splitShowRun=(line.split())
                print(splitShowRun)
    
            
        
print(splitShowRun)

# Old
# splitShowRun = showRun[18].split(' ')
#opens the vars.yaml file, changes the old info with the new information

# with open('../Ansible/vars.yaml', 'r') as read_file:
#         contents = yaml.load(read_file)
#         #Assign the previous IP info to the Old variable
#         contents['oldIP'] = contents['newIP']
#         #Updates the New variable with the new IP info
#         contents['newIP'] = splitShowRun[1]
        

# #dumps new yaml file into output.yaml 
# with open('../Ansible/vars.yaml', 'w') as dump_file:
#         yaml.dump(contents, dump_file)
# return