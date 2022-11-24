# Runs MDT Docker - Keith 11/23
import subprocess
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
        print('='*5,f'Docker img: {docker_img} not Found','='*5)
        os.system(f'docker pull {image}')
    else:
        print('='*5,f'Docker Image: \'{docker_img}\' Found','='*5)
    # print(type(result))
    return

def Docker_Run():
    command=(f'docker run --name {name} -p 3000:3000 -p 57500:57500 {image} &')
    os.system(command)
    return

def Docker_Cleanup(name):
    # Stops image with var=name
    command=(f'docker stop {name}')
    # Removes image with var=name
    command2=(f'docker rm {name}')

    os.system(command)
    print('='*5,'Stopping Container','='*5)
    print('='*5,'Removing Container','='*5)
    os.system(command2)

    #useful command for removing all instances of docker in cli
    #docker rm $( docker ps -aq )
    return