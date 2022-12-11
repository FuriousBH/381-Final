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
    <li><a href="#roadmap">Roadmap</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot][product-screenshot]

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
* pyyaml paramiko webexteamsbot
  ```sh
  pip3 install pyyaml
  pip3 install paramiko
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

This is where we'll show examples of what the chatbot can do. <br>
Things like configuring an interface or pulling information from the router.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [This is optional] Let me know if we want this section
<br>Theoreticals and implementations. Two of Guilleman's favorite things...


<!-- CONTRIBUTING -->
## Contributing

This is a little thing so we can all put in our own information. <br>
Thought it might be kind of nice.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/FuriousBH/381-Final
[contributors-url]: https://github.com/FuriousBH/381-Final/graphs/contributors
[product-screenshot]: images/ProductScreenshot.PNG
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
Code work:
![Figure 1](https://user-images.githubusercontent.com/99046455/201501598-fdb5c8c6-0902-48c5-8d79-f3acacf2e2b6.png)
Code stop work:
![Figure 2](https://user-images.githubusercontent.com/99046455/201501600-b4b37d5f-a2fd-4a0d-b16f-7fe3e2b0f846.png)
Code really stop work:
![Figure 3](https://user-images.githubusercontent.com/99046455/201501730-9e92ac8c-5565-490a-b43e-2deee8c18a24.png)
