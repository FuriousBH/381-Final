import dhcp_parser
import cron_sched
from time import sleep
# from threading import Timer
import os
from webexteamsbot.models import Response
path_command=os.path.dirname(os.path.realpath(__file__))
print(path_command)
command = ('python3 '+f'{path_command}/monitor_auto.py')
comment = 'VPN_CSR1'
ip_net='172.16.0'
def dhcp_info():
    dhcp_info=dhcp_parser.find_new_dhcp_ip(ip_net)
    #Array of info
    print(dhcp_info)
    interface=dhcp_info[0]
    ip_addr=dhcp_info[1]
    renewal_time=(dhcp_info[2])
    time_til_new_ip=(dhcp_info[3])
    return ip_addr,renewal_time,time_til_new_ip
def delete_cron(incoming_msg):
    # response = Response()
    cron_del=cron_sched.del_cron(comment)
    # print(cron_del)
    # response.markdown += str(cron_del)
    return cron_del
# Insert Time Alternative Method Here
def run(incoming_msg):
    # response = Response()
    # Delete Cron Jobs
    cron_del=cron_sched.del_cron(comment)
    # print(cron_del)
    
    # Create Cron Jobs
    # 1. Find DHCP timers
    ip_found,interval_time,time_to=dhcp_info()
    vpn_ip_test=(ip_found) in ip_net
    print(vpn_ip_test)
    if vpn_ip_test and interval_time==0 and time_to==0:
        print(f'EXPECTED IP NET {ip_net} NOT FOUND')
        #FATAL ERROR
        # response.markdown += str(f"{cron_del} and slept for {time_to}. {cron_create}")
        return (f'EXPECTED IP NET {ip_net} NOT FOUND')
    # 2. Create Cron Job
    # Sleep Create Run
    print(f'Sleeping for {time_to}')
    sleep(time_to)
    cron_create=cron_sched.create_cron(interval_time,command,comment)
    # print(cron_create)
    cron_sched.run_cron(comment,command)
    #Invoke Ansible Here
    resp1=(f'{cron_del}  and slept for  {time_to}. {cron_create}')
    return resp1
#Insert alternative threading module here

# Time Alternative Method
# def internal_cron_create():

    # cron_create=cron_sched.create_cron(interval_time,command,comment)
    # print(cron_create)
    # cron_sched.run_cron(comment,command)

    # return
#alternative threading module here
# t=Timer(time_to,internal_cron_create())

# if __name__ == '__main__':
    # main()