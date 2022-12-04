# parse through r1dhcp_lease.txt
# find dhcp changed
# Interface, IP, Renewal time, and Time to next change

def find_new_dhcp_ip(expected_ip_net):
    #Internal Router that changes DHCP file
    file='Outputs/r1dhcp_lease.txt'
    #Lines to find
    ip_addr_pre='Temp IP addr: '
    renewal_time='Renewal: '
    next_time='Next timer fires after: '

    #Verification - also it breaks if some of these are initiated
    vpn_int_ip=expected_ip_net
    interface=''
    ip_addr1=''
    repeat_time=''
    waiting_time=''
    
    return_data=[]
    # Interface and IP found
    with open(file,'r') as f:
        # DONT DELETE l_no,
        for l_no, line in enumerate(f):
            # ip_addr_pre contains two things we need,IP and Int
            if ip_addr_pre in line:
            #IP ADDR SUBBLOCK
                ip_addr1=line.split(ip_addr_pre,1)[1]
                ip_addr1=ip_addr1.split('for',1)[0]
                #Remove Spaces
                ip_addr1=ip_addr1.strip()
            #Interface SUBBLOCK
                interface=line.split('Interface: ',1)[1]
                interface=interface.strip()
                # print('IP Addr1:',ip_addr1)
                # print('Interface: ',interface)
            # Renewal Time SUBBLOCK
            if renewal_time in line:
                repeat_time=line.split(renewal_time,1)[1]
                repeat_time=repeat_time.split(' secs',1)[0]
                repeat_time=str(repeat_time.strip())
                repeat_time=int(repeat_time)
            # NEXT TIME IP REFRESH SUBBLOCK
            if next_time in line:

                waiting_time=line.split(next_time,1)[1]
                waiting_time=waiting_time.strip()
                #Remove any :
                waiting_time=waiting_time.split(':')
                #Hours Convert
                hours=int(waiting_time[0])
                #Minutes Convert
                minutes=int(waiting_time[1])
                #Seconds Convert
                seconds=int(waiting_time[2])
                # Need to know when we have to run a task, Create cron job to do task once
                converted_waiting_time=hours*3600+minutes*60+seconds

            # Once all lines have been found
            # Printing output
            # INTERFACE IS EXPECTED OUTPUT AND WAITING TIME FOUND
            if ip_addr1==vpn_int_ip and waiting_time!='':
            #     print(interface)
            #     print(ip_addr1)
            #     print(repeat_time) # Type = INT
            #     print(waiting_time) # Type = Array
            #     print(converted_waiting_time) # Type = INT
                break
                # don't look for next lines
    
    #Returning Data
    return_data.append(interface)
    return_data.append(ip_addr1)
   
    return_data.append(repeat_time)# Renewal Time, Don't rename, int to remove float
    return_data.append(converted_waiting_time)
    return return_data #converts into string upon return
    # call Ansiblke()
# def main():
'''
APPENDIX
Useful debug during line parsing:
            if input in line:
                # # Useful Debug
                # print('string found in a file')
                # print('Line Number:', l_no)
                # print('Line:', line)
String Parsing
Split outputs into an array
Thats way you'll see this. [accesses the desired element]
    if next_time in line:
        waiting_time=line.split(next_time,1)[1]
Then we strip any white space
        waiting_time=waiting_time.strip()
Found a character that repeats, use split
        waiting_time=waiting_time.split(':')
'''