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
1.  Ensure that you have installed Ansible onto your device with the command, "python3 -m pip install --user ansible"
2.  Using the "show run *router name*" command in the chatbot will issue the command "show ip interface brief" on the router specified in the host file.

![image](https://user-images.githubusercontent.com/99046455/206283453-e7c4cab2-8b1c-4730-9b16-d1075c62a712.png)

3. After that command is succesfully issued, it will save the output into a text file "rShowRun.txt"
4. Pay special attention to line 19, or if we are using a list value [18], it contains the updated IP of the interface

![image](https://user-images.githubusercontent.com/99046455/206273954-4c8dbae6-9010-4964-857f-ce941fdf82a8.png)

6. Now using the "update vars" command with the chat bot, the rShowRun.txt file will be read, split into lines, then line 18 will be split by the blank character ' ' which allows us to specifically grab the IP address we want. Lastly, that command will update the vars.yaml file with the new IP address, and move the previous IP to the oldIP variable.

![image](https://user-images.githubusercontent.com/99046455/206283197-c2a1f125-dc3e-4d4b-93b6-0ab60a5bdf05.png)

8. Finally, the "update tunnel" chat bot command will issue a shell command that will trigger the ansible playbook "updateTunnel-playbook.yaml" which will update the tunnel information of the router who is trying to peer with the dynamically changing router from the branch site.

![image](https://user-images.githubusercontent.com/99046455/206282598-6fe9be3d-b493-4fc4-8eb0-cd68c7abc5df.png)

8. With those commands the chatbot did the following: grab the ip interface information, updated the rShowRun.txt file with the new info, updated the vars.yaml file with the new IP info, then used Ansible to update the HQ router's crypto isakmp information with the new peer's IP address.





### How this project went:
Figure1:
![Figure 1](https://user-images.githubusercontent.com/99046455/201501598-fdb5c8c6-0902-48c5-8d79-f3acacf2e2b6.png)
Figure2:
![Figure 2](https://user-images.githubusercontent.com/99046455/201501600-b4b37d5f-a2fd-4a0d-b16f-7fe3e2b0f846.png)
Figure3:
![Figure 3](https://user-images.githubusercontent.com/99046455/201501730-9e92ac8c-5565-490a-b43e-2deee8c18a24.png)
