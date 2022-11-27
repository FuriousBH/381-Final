# Runs MDT Docker - Keith 11/23
import subprocess
import os

# Need to use subprocess instead of os.system, but its functional - Keith
name='CNIT381_MDT'
image = 'jeremycohoe/tig_mdt'

def Docker_Check():
    docker_img=(f'{image}:latest')
    docker_inspect=(f'docker image inspect {image} | grep latest')
    rep1,rep2=0,0
    result=str(subprocess.check_output(docker_inspect, shell=True))
    # print(result)
    if docker_img not in result:
        rep1=(f'Docker img: {docker_img} not Found')
        os.system(f'docker pull {image}')
    else:
        rep2=(f'Docker Image: \'{docker_img}\' Found')
    # print(type(result))
    return rep1,rep2

def Docker_Run():
    command=(f'docker run --name {name} -p 3000:3000 -p 57500:57500 {image} &')
    os.system(command)
    return('Success')

def Docker_Cleanup():
    # Stops image with var=name
    command=(f'docker stop {name}')
    # Removes image with var=name
    command2=(f'docker rm {name}')
    
    os.system(command)
    resp1=('Stopping Container')
    resp2=('Removing Container')
    os.system(command2)

    #useful command for removing all instances of docker in cli
    #docker rm $( docker ps -aq )
    return resp1,resp2