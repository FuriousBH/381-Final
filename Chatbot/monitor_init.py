import dhcp_update_file
import dhcp_parser
import cron_sched
from time import sleep
# from threading import Timer
import os
import ansible_skills

path_command=os.path.dirname(os.path.realpath(__file__))
py_command = ('python3 '+f'{path_command}/monitor_auto.py')
comment = 'VPN_CSR2'
ip_net='172.16.0.'

def dhcp_info(incoming_msg):
    dhcp_update_file.run(incoming_msg)
    dhcp_info=dhcp_parser.find_new_dhcp_ip(ip_net)
    #Array of info
    print(dhcp_info)
    interface=dhcp_info[0]
    ip_addr=dhcp_info[1]
    renewal_time=(dhcp_info[2])
    time_til_new_ip=(dhcp_info[3])
    return ip_addr,renewal_time,time_til_new_ip

def delete_cron():
    cron_del=cron_sched.del_cron(comment)
    return cron_del

router_dev='r2'
def run(incoming_msg):
    # Delete Cron Jobs
    cron_del=cron_sched.del_cron(comment)
    router_select=incoming_msg
# 1. Find DHCP timers
    ip_found,interval_time,time_to=dhcp_info(router_select)
# 2. Create Cron Job
        # Sleep Create Run
    print(f'Sleeping for {time_to}')
    sleep(time_to)
    cron_create=cron_sched.create_cron(interval_time,py_command,comment)
    cron_sched.run_cron(comment,py_command)
        #Invoke Ansible Here
    # update rShowRun.txt
    ans_resp1=ansible_skills.show_ip_brief(router_dev)
    # update vars.yaml
    ans_resp2=ansible_skills.update_vars(router_dev)
    # update tunnel info w/ playbook
    ans_resp3=ansible_skills.update_tunnel()
    resp1=(f'{cron_del}  and slept for  {time_to}. {cron_create}\n {ans_resp1}\n{ans_resp2}\n{ans_resp3}')
    return resp1


# Time Alternative Method
# def internal_cron_create():

    # cron_create=cron_sched.create_cron(interval_time,command,comment)
    # print(cron_create)
    # cron_sched.run_cron(comment,command)

    # return
#alternative threading module here
# t=Timer(time_to,internal_cron_create())