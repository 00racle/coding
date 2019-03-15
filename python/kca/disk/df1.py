import paramiko
import re

hosts = {'192.168.6.222': '24477', '192.168.6.250': '24477', '192.168.6.239': '24477'}
cmd = "df -h | awk '{print $(NF-1), $(NF-0)}' | grep '%'"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def connection(host, port):
	print(host)
	ret = []
	ssh.connect(host, username='chk1417', port=port, password='8282op82@#')
	ssh.invoke_shell()
	stdin, stdout, stderr = ssh.exec_command(cmd)
		
	for line in stdout:
		#print(line, end="")
		
		ret.append(line.split())

	print(ret)

for i, p in hosts.items():
	connection(i, p)
