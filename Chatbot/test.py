import core_skills as Core
import myparamiko as paramiko
import routers as R

# Example Input from Chatbot
incoming = 'show int r2'


# The beginnings of an example function
r_list = R.routers.keys()

for key in r_list:
    if key in incoming:
        device = key
        print(f"Found the key: {device}")
    else:
        device = "Device not found"
        print(device)