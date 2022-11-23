import paramiko

from flask import Flask
from flask import request

# creating an ssh client object
ssh_client = paramiko.SSHClient()
# print(type(ssh_client))

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print('Connecting to 10.1.1.10')
ssh_client.connect(hostname='192.168.122.10', port='22', username='cisco', password='cisco',
                   look_for_keys=False, allow_agent=False)


# checking if the connection is active
print(ssh_client.get_transport().is_active())

# sending commands
# ...

print('Closing connection')
ssh_client.close()

sample = Flask(__name__)
@sample.route("/")
def main():
    return "You are calling me from " + request.remote_addr + "\n"

if __name__ == "__main__":
    sample.run(host="0.0.0.0", port=8080)
