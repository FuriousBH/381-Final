# Monitor - Keith 11/23
from yaml import safe_load
from jinja2 import Environment, FileSystemLoader
from ncclient import manager
import routers
# Add subscriptions.yml to router configs found in routers.py
# def main():
def setup():
    """
    Execution begins here.
    """
    # File load
    with open("inputs.yml","r") as handle:
        data = safe_load(handle)

    # Jinja2 Connection
    j2_env = Environment(loader=FileSystemLoader("."), autoescape=True)
    template = j2_env.get_template("mdt_netconf.j2")
    new_config = template.render(data=data)

    # debug XML file
    print(new_config)

    #Netconf Management'
    with manager.connect(**routers.router) as conn:
        netconf_conn=("NETCONF session connected")

        # Peform updates and print success
        config_resp = conn.edit_config(target="running", config=new_config)
        if config_resp.ok:
            sub_resp=(f"Added {len(data['subscriptions'])} subcriptions")
        
    netconf_disc=("NETCONF session disconnected")
    return(netconf_conn, sub_resp,netconf_disc)

# if __name__ == "__main__":
#     main()