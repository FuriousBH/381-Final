# Runs MDT Docker - Keith 11/23
import subprocess
from time import sleep
import os

# Need to use subprocess instead of os.system, but its functional - Keith
name='CNIT381_MDT'
image = 'jeremycohoe/tig_mdt'

def Docker_Check():
    docker_img=(f'{image}:latest')
    docker_inspect=(f'docker image inspect {image} | grep latest')

    result=str(subprocess.check_output(docker_inspect, shell=True))
    # print(result)
    if docker_img not in result:
        not_found = '='*5,f'Docker img: {docker_img} not Found','='*5
        os.system(f'docker pull {image}')
        return not_found
    else:
        found = '='*5,f'Docker Image: \'{docker_img}\' Found','='*5
    # print(type(result))
        return found

def Docker_Run():
    # Modifying this so it runs docker in the background
    # -t A terminal that can be accessed
    # -d Background so it doesn't take over the Flask Terminal
    # -Riley 11/24
    command=(f'docker run -t -d --name {name} -p 3000:3000 -p 57500:57500 {image} &')
    response = f"Starting Image {name}"
    os.system(command)
    return response

def Docker_Cleanup():
    # Going to get the id of the docker container.
    # docker container ls --quiet --filter "name=CNIT"
    # Stops image with var=name
    name = os.popen('docker container ls --quiet --filter "name=CNIT"').read()
    containerid = name
    command=(f'docker stop {name}')
    # Removes image with var=name
    command2=(f'docker rm {name}')
    
    
    os.system(command)
    print('='*5,f'Stopping Container {name}','='*5)
    # Stopping the container takes time. This is a placeholder for pausing
    sleep(20)
    print('='*5,'Removing Container','='*5)
    os.system(command2)

    #useful command for removing all instances of docker in cli
    #docker rm $( docker ps -aq )
    return containerid


