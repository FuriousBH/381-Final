# 381-Final
This is a repository for the CNIT-381 Final Group Project.

## Project Overview
In this project our team utilized skills we developed throughout the CNIT-381 course to make a chatbot that uses several skills including Ansible, Restconf/Netconf, and Paramiko/Netmiko.

## Project Instructions
### Local Setup
1.   Install ruamel.yaml or pyyaml by issuing this command in the terminal: pip3 install ruamel.yaml OR pip3 install pyyaml, this is important for being able to update yaml files. ruamel.yaml is important for being able to open, modify, and save yaml files from within a python script.

![installPyYAML](https://user-images.githubusercontent.com/99046455/204409091-39012aad-ea3a-404a-8c72-c99aaac3d527.png)

2.   

### Ansible
1.  Ensure that you have installed Ansible onto your device with the command, python3 -m pip install --user ansible
2.  Using the "show run" command in the chatbot will issue the command "show ip interface brief" on the router specified in the host file.

![image](https://user-images.githubusercontent.com/99046455/206268266-c02aac33-030f-45a2-b1b6-b890189674c5.png)

3. After that command is succesfully issued, it will save the output into a text file "rShowRun.txt"
4. Pay special attention to line 19, or if we are using a list value [18], it contains the updated IP of the interface
5. Now using the "update_vars" command with the chat bot, the rShowRun.txt file will be read, split into lines, then line 18 will be split by the blank character ' ' which allows us to specifically grab the IP address we want. Lastly, that command will update the vars.yaml file with the new IP address, and move the previous IP to the oldIP variable.
6. Finally, the "update_tunnel" chat bot command will issue a shell command that will trigger the ansible playbook "updateTunnel-playbook.yaml" which will update the tunnel information of the router who is trying to peer with the dynamically changing router from the branch site.





### How this project went:
Figure1:
![Figure 1](https://user-images.githubusercontent.com/99046455/201501598-fdb5c8c6-0902-48c5-8d79-f3acacf2e2b6.png)
Figure2:
![Figure 2](https://user-images.githubusercontent.com/99046455/201501600-b4b37d5f-a2fd-4a0d-b16f-7fe3e2b0f846.png)
Figure3:
![Figure 3](https://user-images.githubusercontent.com/99046455/201501730-9e92ac8c-5565-490a-b43e-2deee8c18a24.png)
