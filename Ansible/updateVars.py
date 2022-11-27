import sys
import ruamel.yaml
yaml = ruamel.yaml.YAML()

showRun = open('rShowRun.txt', 'r').read().splitlines()

with open('vars.yaml', 'r') as read_file:
    contents = yaml.load(read_file)
    print(contents)
    contents['newCrypto'] = showRun[5]
    contents['newSetPeer'] = showRun[14]
    print(contents)

with open('output.yaml', 'w') as dump_file:
    yaml.dump(contents, dump_file)
