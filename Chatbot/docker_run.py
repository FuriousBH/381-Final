# Runs MDT Docker - Keith --Riley 11/27
import subprocess
from time import sleep
import os

# Need to use subprocess instead of os.system, but its functional - Keith
name='CNIT381_MDT'
image = 'jeremycohoe/tig_mdt'

def Docker_Check():
    # Assign variables for finding Image
    # Find if Image is on machine
    docker_img=(f'{image}:latest')
    docker_inspect=(f'docker image inspect {image} | grep latest')

    result=str(subprocess.check_output(docker_inspect, shell=True))
    # print(result)
    # If Image not found download
    if docker_img not in result:
        not_found = f'Docker img: {docker_img} not Found'
        os.system(f'docker pull {image}')
        return not_found
    else:
        found = f'Docker Image: \'{docker_img}\' Found'
    # print(type(result))
        return found

def Docker_Run():
    # Modifying this so it runs docker in the background
    # -t A terminal that can be accessed
    # -d Background so it doesn't take over the Flask Terminal
    # -Riley 11/24
    response = ''
    #Image Not Found Test
    # You were checking docker container ls, but we were looking for existing docker storage.
    # docker ps -a is the way to go for that
    if name in (os.popen('docker ps -a --filter "name=CNIT"').read()):
        command=(f'docker start {name}')
    else:
        response +=('Creating first time image')
        command=(f'docker run -dit --name {name} -p 3000:3000 -p 57500:57500 {image}')
        
    response = f"Starting Image {name}"
    # -d 
    os.system(command)
    return response

def Docker_Cleanup():
    # Going to get the id of the docker container.
    # docker container ls --quiet --filter "name=CNIT"
    # Stops image with var=name
    # name = os.popen('docker container ls --quiet --filter "name=CNIT"').read()
    command=(f'docker stop {name}')
    # Removes image with var=name
    # command2=(f'docker rm {name}')
    
    os.system(command)
    print(f'Stopping Container {name}')
    # Stopping the container takes time. This is a placeholder for pausing
    sleep(15)
    # print('='*5,'Removing Container','='*5)
    # os.system(command2)

    #useful command for removing all instances of docker in cli
    #docker rm $( docker ps -aq )
    return name

def Docker_Delete():
    #Delete Docker Container = var(name)
    response = ''
    
    if name in (os.popen('docker ps -a --filter "name=CNIT"').read()):
        response = (f"Deleting container {name}")
        command = (f'docker rm {name}')
    else:
        response = (f"Container {name} not found")
    os.system(command)
    return response