import sys
import ruamel.yaml
yaml = ruamel.yaml.YAML()

#reads show run file and splits lines
showRun = open('rShowRun.txt', 'r').read().splitlines()

#opens the vars.yaml file, changes the old info with the new information
with open('vars.yaml', 'r') as read_file:
    contents = yaml.load(read_file)
    print(contents)
    #Assign the previous IP info to the Old variable
    contents['oldCrypto'] = contents['newCrypto']
    contents['oldSetPeer'] = contents['newSetPeer']
    #Updates the New variable with the new IP info
    contents['newCrypto'] = showRun[5]
    contents['newSetPeer'] = showRun[14]
    print(contents)

#dumps new yaml file into output.yaml 
with open('output.yaml', 'w') as dump_file:
    yaml.dump(contents, dump_file)
