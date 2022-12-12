import myparamiko as paramiko
import core_skills as Core

def run(incoming_msg):
    # workaround for Keith's auto update
    if incoming_msg is 'r2':
        router='r2'
    else:
        router = Core.to_text(incoming_msg)
    # end workaround
    router = Core.command_parser(router)
    username, password, address = Core.router_needs(router)
    filename = Core.combine_two_strings(router, 'dhcp_lease.txt')

    f = open('Outputs/' + filename, 'w')
    shell = Core.my_paramiko_client_shell(address, username, password)
    response = paramiko.show(shell, "show dhcp lease")
    f.writelines([response])
    f.close()
    return response
