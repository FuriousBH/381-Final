import dhcp_parser


# import Brock_Ansible
ip_net='172.16.0.'
def main():
    dhcp_info=dhcp_parser.find_new_dhcp_ip(ip_net)
    #Array of info
    # print(dhcp_info)
    interface=dhcp_info[0]
    ip_addr=dhcp_info[1]
    renewal_time=(dhcp_info[2])
    time_til_new_ip=(dhcp_info[3])
    # can get rid of when Ansible is working, Use for debug    
    # print('Interface: ',interface)
    # print('IP Address: ',ip_addr)
    # print('Renewal Time: ',renewal_time)
    # print('Time until new IP: ',time_til_new_ip)
    ip_found=ip_addr
    ip_test=(ip_found) not in ip_net
    if ip_test and renewal_time==0 and time_til_new_ip==0:
        print(f'EXPECTED IP NET {ip_net} NOT FOUND')
        exit()
    #Brock Code
    # brock_ansible(ip_addr)
    print('Brocks Code Here')
if __name__ == "__main__":
    main()

