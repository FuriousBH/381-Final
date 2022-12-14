<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/381logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">381-Final</h3>

  <p align="center">
    381-Final Project. Using a chatbot  to automate Cisco Router.
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <ul>
        <li><a href="#ansible">Ansible</a></li>
        <li><a href="#creating-an-interface">Create an Interface</a></li>
    </ul>
    <ul>
        <li><a href="#monitor">Monitor</a></li>
        <li><a href="#bonus">Bonus</a></li>
    </ul>
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![ProductNameScreenShot][product-screenshot]

This project aims to automate the maintenance of a Cisco Router using a webex chatbot.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python.js]][Python-url]
* [![Ansible][Ansible.js]][Ansible-url]
* [![Docker][Docker.js]][Docker-url]
* [![Devnet][Devnet.js]][Devnet-url]
* [![Flask][Flask.js]][Flask-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get started, make sure you have Python installed. In addition you will need to install Ansible and Docker. 

### Prerequisites
<br />
Make sure that you have Python installed on your machine. <br />
Feel free to follow the tutorials listed below. <br /> 


Download the following libraries
* adaptivecardbuilder, Flask, Jinja2, ncclient, paramiko, python_crontab, PyYAML, requests, ruamel.base, webexteamsbot
```sh
  pip3 install adaptivecardbuilder
  pip3 install Flask
  pip3 install Jinja2
  pip3 install ncclient
  pip3 install paramiko
  pip3 install python_crontab
  pip3 install PyYAML
  pip3 install requests
  pip3 install ruamel.base
  pip3 install webexteamsbot
  ```

This runs on a flask server, so you'll want to ensure that you have that ready to go. <br />
* Flask
  ```sh
  https://flask.palletsprojects.com/en/2.2.x/installation/
  ```
Now, make sure that you have Docker installed
* Docker
  ```sh
  https://docs.docker.com/get-docker/
  ```

You will need the following Docker image to set up the monitor
* jeremycohoe/tig_mdt
  ```sh
  https://hub.docker.com/r/jeremycohoe/tig_mdt
  ```

With that taken care of, the last prerequisite will be to download Ansible
* Ansible
  ```sh
  https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html
  ```
### Installation

1. Clone the repo


2. Set up a webex bot.
    ```sh
    https://developer.webex.com/docs/bots
    ```


3. Navigate to the Directory with the 381Bot.py app <br>
![PWD][PWD-screenshot]

4. Modify the routers.py dictionary to match your devices & the Ansible hosts file with the address of the Branch Router.<br>

![Router][Routers-screenshot]
<br>
![ANSIBLE][AnsibleHosts-screenshot]

5. Update your Bot URL with the relevant ngrok Forwarding URL.
![Ngrok][Ngrok-screenshot]
<br>
![BotUrl][BotUrl-screenshot]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### Ansible
1.  Using the "show run *router name*" command in the chatbot will issue the command "show ip interface brief" on the router specified in the host file.

![image](https://user-images.githubusercontent.com/99046455/206283453-e7c4cab2-8b1c-4730-9b16-d1075c62a712.png)

2. After that command is succesfully issued, it will save the output into a text file "rShowRun.txt"
3. Pay special attention to line 19, or if we are using a list value [18], it contains the updated IP of the interface

![image](https://user-images.githubusercontent.com/99046455/206273954-4c8dbae6-9010-4964-857f-ce941fdf82a8.png)

4. Now using the "update vars" command with the chat bot, the rShowRun.txt file will be read, split into lines, then line 18 will be split by the blank character ' ' which allows us to specifically grab the IP address we want. Lastly, that command will update the vars.yaml file with the new IP address, and move the previous IP to the oldIP variable.

![image](https://user-images.githubusercontent.com/99046455/206283197-c2a1f125-dc3e-4d4b-93b6-0ab60a5bdf05.png)

5. Finally, the "update tunnel" chat bot command will issue a shell command that will trigger the ansible playbook "updateTunnel-playbook.yaml" which will update the tunnel information of the router who is trying to peer with the dynamically changing router from the branch site.

![image](https://user-images.githubusercontent.com/99046455/206282598-6fe9be3d-b493-4fc4-8eb0-cd68c7abc5df.png)

6. With those commands the chatbot did the following: grab the ip interface information, updated the rShowRun.txt file with the new info, updated the vars.yaml file with the new IP info, then used Ansible to update the HQ router's crypto isakmp information with the new peer's IP address.

### Creating an Interface
1. By sending the command "make int" to the bot, you will be presented with a Webex Card.


2. Fill out the appropriate information (You need to use proper case)

![image][Card-screenshot]
![image][CardComplete-screenshot]

3. Verify that the interface has been configured.

![image][CardIPBrief-screenshot]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Monitor
- Commands
  ```sh
  vpn automate (device-name-here)
  vpn stop
  ```
- Command Flow for 'vpn automate r2'
  ```sh
  381bot.py 
  > monitor_init.py 
    # Runs
    > dhcp_update_file
    > dhcp_parser
    # wait for dhcp lease expire
    # create and run crontab for monitor_auto
  > monitor_auto.py
    # Runs
    > ansible_skill
        > dhcp_update_file.run
        # show run
        show_ip_brief
        # update vars.yaml
        update_vars
        # update tunnel info w/ playbook
        update_tunnel
  #Crontab waits until next dhcp lease time
  ```
### Monitor Explanation
We needed a way to time the next dhcp renewal. The way we chose was executing the cisco command "ip dhcp lease". This output allows us to parse the time until a new lease. When the new lease expires, a cron job is created with crontab using the monitor_auto.py. That file is then executed immedietly through crontab. <br>
Monitor auto then executes the ansible skills. Ansible needs its variables for r2 updated so we executed a cisco ios command show ip brief and return that info to the vars.yaml. Then we update the tunnel info.
  

### Bonus
This section is for things we researched but not ended up being used.
- We tried to implement monitor through MDT. MDT is model driven telemetry. Basically it runs telemetry and reports back to a server. This server runs a graphical hub of various variables. When we realized we would have to add routing\DNS to be accessible from the Chatbot, we realized this was not the solution for us.
- Commands
```sh
"docker check" - 'Checks for and downloads MDT image'
"docker run" - 'Runs the docker image'
"docker stop" - 'Stops the docker image'
"docker delete" - 'Deletes the docker image'
``` 
<!-- ROADMAP -->
## Roadmap

- Changing static variables
Static variables for dhcp found in these files
dhcp_parser.py, monitor_init.py, monitor_auto.py
  - dhcp_parser.py 
    - file - needs to be progammatic based on the user input. In case of multiple branch locations

  - monitor_init.py
    - router_dev='r2'
  - monitor_auto.py
    - ip_net=172.16.0 - would want this in a config file of some sort. Different IP schemas
    - router_dev='r2'
<!-- CONTRIBUTING -->
## Contributing
RA - Led the team and developed RESConf skills, useful tools, and general oversite over production.
<br>BH - developed Ansible solution.
<br>KG - developed Monitoring solution and integration with Ansible.
<br><br>
If you would like to contribute, please make a Fork & submit a Pull request!
<br>

THANKS!
<br>


<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/FuriousBH/381-Final
[contributors-url]: https://github.com/FuriousBH/381-Final/graphs/contributors
[product-screenshot]: images/ProductScreenshot.png
[Python.js]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org
[Ansible.js]: https://img.shields.io/badge/ansible-%231A1918.svg?style=for-the-badge&logo=ansible&logoColor=white
[Ansible-url]: https://www.ansible.com
[Docker.js]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com
[Devnet.js]: images/Devnet.png
[Devnet-url]: https://developer.cisco.com
[Flask.js]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white
[flask-url]: https://flask.palletsprojects.com/en/2.2.x/
[PWD-screenshot]: images/PWD.png
[Routers-screenshot]: images/Routers.png
[AnsibleHosts-screenshot]: images/Hosts.png
[Ngrok-screenshot]: images/ngrok.png
[BotUrl-screenshot]: images/BotUrl.PNG
[Card-screenshot]: images/IntCard.PNG
[CardComplete-screenshot]: images/MadeCard.PNG
[CardIPBrief-screenshot]: images/intBriefCard.PNG


### How this project went:
Code work:
![Figure 1](https://user-images.githubusercontent.com/99046455/201501598-fdb5c8c6-0902-48c5-8d79-f3acacf2e2b6.png)
Code stop work:
![Figure 2](https://user-images.githubusercontent.com/99046455/201501600-b4b37d5f-a2fd-4a0d-b16f-7fe3e2b0f846.png)
Code really stop work:
![Figure 3](https://user-images.githubusercontent.com/99046455/201501730-9e92ac8c-5565-490a-b43e-2deee8c18a24.png)
