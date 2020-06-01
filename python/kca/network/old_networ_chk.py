import paramiko
import time
import sys
from datetime import datetime

start_time = time.time()
hosts = {'192.168.1.1': 'password01', '192.168.1.2': 'password02', '192.168.1.3': 'password03', '192.168.1.4': 'password04', '192.168.1.5': 'password05', '192.168.1.6': 'password06'}

now = datetime.now()

def conn(host, password):
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(host, username='계정명', port='포트번호', password=password)
		print("\r\n")
		print("="*80+"\r\n")
		print(host.center(80, " ")+"\r\n")
		print("="*80+"\r\n")
		print("\r\n")
		connection = ssh.invoke_shell()
		connection.send("enable\n")
		connection.send(password)
		connection.send("\n")
		connection.send("terminal length 0\n")
		connection.send("show start\n")
		time.sleep(2)
		connection.send("show ver\n")
		time.sleep(1)
		connection.send("show vlan\n")
		time.sleep(1)
		if host in ('192.168.1.1', '192.168.1.2'):
			connection.send("show env status\n")
		else:
			connection.send("show env all\n")
		time.sleep(1)
		if host in ('192.168.1.3', '192.168.1.4'):
			connection.send("show module all\n")
		time.sleep(1)
		if host in ('192.168.1.5', '192.168.1.6'):
			connection.send("show power status all\n")
		time.sleep(1)
		if host in ('192.168.1.1', '192.168.1.2'):
			connection.send("show power status\n")
		time.sleep(1)
		connection.send("show inventory\n")
		time.sleep(1)
		connection.send("show processes cpu | in seconds:\n")
		time.sleep(1)
		connection.send("show processes memory | in Total:\n")
		time.sleep(1)
		connection.send("show standby br\n")
		time.sleep(1)
		connection.send("show spanning-tree active\n")
		time.sleep(1)
		connection.send("show arp\n")
		time.sleep(1)
		connection.send("show mac address-table\n")
		time.sleep(1)
		connection.send("show int status\n")
		time.sleep(1)
		if host in ('192.168.1.3', '192.168.1.4'):
			connection.send("show bootdisk:\n")
		time.sleep(1)
		if host in ('192.168.1.5', '192.168.1.6'):
			connection.send("show bootflash:\n")
		time.sleep(1)
		if host not in ('192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5'):
			connection.send("show flash:\n")
		time.sleep(1)
		connection.send("show logging\n")
		time.sleep(2)
		output = connection.recv(999999).decode(encoding='utf-8')
		print(output)
		ssh.close()
	except paramiko.AuthenticationException:
		print(host, "인증에러")
	except paramiko.ssh_exception.NoValidConnectionsError:
	  	print(host, "접속불가")
	except TimeoutError:
	  	print(host, "타임아웃")
orig_stdout = sys.stdout
f = open('result_cisco.txt', 'w')
sys.stdout = f
print(now)

for h, p in hosts.items():
	conn(h, p)

sys.stdout = orig_stdout
f.close()

print("Runtime: %.02f"%(time.time()-start_time))
