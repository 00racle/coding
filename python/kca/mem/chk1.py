import paramiko
import time
import sys
from datetime import datetime

hosts = {'192.168.6.222': '24477', '192.168.6.250': '24477'}
cmd = "free -m | awk '/Mem:/' | awk '{print $2, $3, $4}'"
#cmd = 'hostname'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def conn(host, port):
	ret = []
	print(host)
	ssh.connect(host, username='chk1417', port=port, password='8282op82@#')
	ssh.invoke_shell()
	stdin, stdout, stderr = ssh.exec_command(cmd)
	for line in stdout:
		#print(line, end='')
		#ret.append(line.split(' '))
		#print(line.rstrip('\n').split(' '))
		a = line.rstrip('\n').split(' ')
		b = int(a[2])*100/int(a[0])
		#print("%0.3f%%"%b)
		print("%0.3f"%b)
	#print(ret)
	ssh.close()


for i, p in hosts.items():
	conn(i, p)
	


