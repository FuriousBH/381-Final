import dhcp_update_file
import ansible_skills

ip_net='172.16.0.'
router_dev='r2'
def main():
#update DHCP lease txt - could cut, but its could be useful outside program
    dhcp_update_file.run(router_dev)
    print('Brocks Code Here')
    # show run
    ansible_skills.show_ip_brief(router_dev)
    # update vars.yaml
    ansible_skills.update_vars(router_dev)
    # update tunnel info w/ playbook
    ansible_skills.update_tunnel()
# Array of info for debug
    # dhcp_info=dhcp_parser.find_new_dhcp_ip(ip_net)
    # print(dhcp_info)
    # interface=dhcp_info[0]
    # ip_addr=dhcp_info[1]
    # renewal_time=(dhcp_info[2])
    # time_til_new_ip=(dhcp_info[3])
if __name__ == "__main__":
    main()

