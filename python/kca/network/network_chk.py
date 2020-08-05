from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException
import pymysql
import time
from datetime import datetime
import sys

start_time = time.time()

conn_db = pymysql.connect(host = '192.168.6.160', user='chk1417', password='8282op82@#',db = 'dchk')
curs = conn_db.cursor()

#sql = "select * from net where hostname in ('hostname-01', 'hostname-02');"
#sql = "select * from net where port=22;"
#sql = "select * from net where class='CISCO';"
#sql = "select * from net order by n_num asc;"
sql = "select n_num, ip, port, id, AES_DECRYPT(UNHEX(pw), ip) as pw, class, model, hostname from net order by n_num;"
curs.execute(sql)

result = curs.fetchall()
conn_db.close()

# d[0]=n_num, d[1]=ip, d[2]=port, 2[3]=id, d[4]=pw, d[5]=class, d[6]=model, d[7]=hostname
def cisco(d):
    print("="*80+"\n")
    print("Device Info: 【%s】 (%s)".center(50)%(d[7], d[1])+"\n")
    print("="*80+"\n")
    cisco = {
            'device_type' : 'cisco_ios',
            'ip' : d[1],
            'username' : d[3],
            'password' : d[4].decode('utf-8'),
            'port' : d[2],
            }
    try:
        net_connect = ConnectHandler(**cisco)
        net_connect.send_command("enable"+'\n', expect_string=r'Password:')
        net_connect.send_command(d[4].decode('utf-8'), expect_string=r'#')
        print("\n"+"***********     Command: show start     *********** \n".center(80)+"\n"+net_connect.send_command("show start"))
        print("\n"+"***********     Command: show ver     *********** \n".center(80)+"\n"+net_connect.send_command("show ver"))
        print("\n"+"***********     Command: show vlan     *********** \n".center(80)+"\n"+net_connect.send_command("show vlan"))
        if d[1] in ('x.x.x.x', 'x.x.x.x', 'x.x.x.x', 'x.x.x.x'):
            print("\n"+"***********     Command: show env status     *********** \n".center(80)+"\n"+net_connect.send_command("show env status"))
            print("\n"+"***********     Command: show module all     *********** \n".center(80)+"\n"+net_connect.send_command("show module all"))
        else:
            print("\n"+"***********     Command: show env all     *********** \n".center(80)+"\n"+net_connect.send_command("show env all"))
            print("\n"+"***********     Command: show inventory     *********** \n".center(80)+"\n"+net_connect.send_command("show inventory"))
            print("\n"+"***********     Command: show processes cpu | in seconds:     *********** \n".center(80)+"\n"+net_connect.send_command("show processes cpu | in seconds:"))
            print("\n"+"***********     Command: show processes memory | in Total:     *********** \n".center(80)+"\n"+net_connect.send_command("show processes memory | in Total:"))
        if d[1] not in ('x.x.x.x', 'x.x.x.x'):
            print("\n"+"***********     Command: show standby br     *********** \n".center(80)+"\n"+net_connect.send_command("show standby br"))
            print("\n"+"***********     Command: show spanning-tree active     *********** \n".center(80)+"\n"+net_connect.send_command("show spanning-tree active"))
            print("\n"+"***********     Command: show arp     *********** \n".center(80)+"\n"+net_connect.send_command("show arp"))
            print("\n"+"***********     Command: show mac address-table     *********** \n".center(80)+"\n"+net_connect.send_command("show mac address-table"))
            print("\n"+"***********     Command: show int status     *********** \n".center(80)+"\n"+net_connect.send_command("show int status"))
        if d[1] in ('x.x.x.x', 'x.x.x.x'):
            print("\n"+"***********     Command: show power status all     *********** \n".center(80)+"\n"+net_connect.send_command("show power status all"))
            print("\n"+"***********     Command: show bootdisk:     *********** \n".center(80)+"\n"+net_connect.send_command("show bootdisk:"))
        elif d[1] in ('x.x.x.x', 'x.x.x.x'):
            print("\n"+"***********     Command: show power status     *********** \n".center(80)+"\n"+net_connect.send_command("show power status"))
            print("\n"+"***********     Command: show bootflash:     *********** \n".center(80)+"\n"+net_connect.send_command("show bootflash:"))
        elif d[1] in ('x.x.x.x', 'x.x.x.x', 'x.x.x.x', 'x.x.x.x'):
            print("\n"+"***********     Command: show power inline     *********** \n".center(80)+"\n"+net_connect.send_command("show power inline"))
            print("\n"+"***********     Command: show bootflash:     *********** \n".center(80)+"\n"+net_connect.send_command("show flash:"))
        else:
            print("\n"+"***********     Command: show power     *********** \n".center(80)+"\n"+net_connect.send_command("show power"))
            print("\n"+"***********     Command: show flash:     *********** \n".center(80)+"\n"+net_connect.send_command("show flash:"))
            print("\n"+"***********     Command: show logging     *********** \n".center(80)+"\n"+net_connect.send_command("show logging"))
            net_connect.disconnect()
    except NetMikoTimeoutException:
        print("장비 접속 불가(타임아웃)")
    except NetMikoAuthenticationException:
        print("장비 접속 불가(인증에러)")

	
	
def alcatel(d):
    print("+"+"-"*80+"+")
    print("Device Info: 【%s】 (%s)".center(50)%(d[7], d[1]))
    print("+"+"-"*80+"+")
    alcatel = {
            'device_type' : 'alcatel_aos',
            'ip' : d[1],
            'username' : d[3],
            'password' : d[4].decode('utf-8'),
            'port' : d[2],
            }
    try:
        net_connect = ConnectHandler(**alcatel)
        print("\n"+"***********     Command: show configuration snapshot     *********** \n".center(80)+"\n"+net_connect.send_command("show configuration snapshot", delay_factor=20))
        print("\n"+"***********     Command: show chassis     *********** \n".center(80)+"\n"+net_connect.send_command("show chassis"))
        print("\n"+"***********     Command: show system     *********** \n".center(80)+"\n"+net_connect.send_command("show system"))
        print("\n"+"***********     Command: show hardware info     *********** \n".center(80)+"\n"+net_connect.send_command("show hardware info"))
        print("\n"+"***********     Command: show running-directory     *********** \n".center(80)+"\n"+net_connect.send_command("show running-directory"))
        print("\n"+"***********     Command: show module status     *********** \n".center(80)+"\n"+net_connect.send_command("show module status"))
        print("\n"+"***********     Command: show power supply     *********** \n".center(80)+"\n"+net_connect.send_command("show power supply"))
        print("\n"+"***********     Command: show temperature     *********** \n".center(80)+"\n"+net_connect.send_command("show temperature"))
        print("\n"+"***********     Command: show interfaces counters errors     *********** \n".center(80)+"\n"+net_connect.send_command("show interfaces counters errors"))
        print("\n"+"***********     Command: show vrrp     *********** \n".center(80)+"\n"+net_connect.send_command("show vrrp"))
        print("\n"+"***********     Command: show vlan     *********** \n".center(80)+"\n"+net_connect.send_command("show vlan"))
        print("\n"+"***********     Command: show arp     *********** \n".center(80)+"\n"+net_connect.send_command("show arp"))
        print("\n"+"***********     Command: show mac-address-table     *********** \n".center(80)+"\n"+net_connect.send_command("show mac-address-table"))
        print("\n"+"***********     Command: ls -R     *********** \n".center(80)+"\n"+net_connect.send_command("ls -R"))
        print("\n"+"***********     Command: show interfaces status     *********** \n".center(80)+"\n"+net_connect.send_command("show interfaces status"))
        net_connect.disconnect()
    except NetMikoTimeoutException:
        print("장비 접속 불가(타임아웃)")
    except NetMikoAuthenticationException:
        print("장비 접속 불가(인증에러)")

orig_stdout = sys.stdout
f = open("_".join([datetime.now().strftime("%Y%m%d"), "network_result.txt"]), 'w')
sys.stdout = f

print(datetime.now())
for d in result:
    if d[5] == 'CISCO':
        cisco(d)
    if d[5] == 'ALCATEL-LUCENT':
        alcatel(d)
sys.stdout = orig_stdout
f.close()

print("Runtime: %.02f"%(time.time()-start_time))
