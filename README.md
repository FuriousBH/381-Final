# 381-Final
This is a repository for the CNIT-381 Final Group Project.

# Project Overview
In this project our team utilized skills we developed throughout the CNIT-381 course to make a chatbot that uses several skills including Ansible, Restconf/Netconf, and Paramiko/Netmiko.

# Project Instructions
### Local Setup
1.   Install ruamel.yaml or pyyaml by issuing this command in the terminal: pip3 install ruamel.yaml OR pip3 install pyyaml
![installPyYAML](https://user-images.githubusercontent.com/99046455/204409091-39012aad-ea3a-404a-8c72-c99aaac3d527.png)

2.   

### Ansible
1.  Download the files from the Ansible folder in this repository
2.  tunnelPlaybook.yaml is the playbook Ansible uses to render the Jinja2 template, finalTemplate.j2, with the vars from vars.yaml
3.  updateVars.py is the script used to update the vars.yaml file with the current tunnel IP info that's grabbed from the routers
4.  Combined together, these files gather new tunnel IP info, render a new template, and configure the routers dynamically when it's IP changes



#How this project went:
Figure1:
![Figure 1](https://user-images.githubusercontent.com/99046455/201501598-fdb5c8c6-0902-48c5-8d79-f3acacf2e2b6.png)
Figure2:
![Figure 2](https://user-images.githubusercontent.com/99046455/201501600-b4b37d5f-a2fd-4a0d-b16f-7fe3e2b0f846.png)
Figure3:
![Figure 3](https://user-images.githubusercontent.com/99046455/201501730-9e92ac8c-5565-490a-b43e-2deee8c18a24.png)
