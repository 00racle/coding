import paramiko
import re

hosts = {'ip': 'port'}
cmd = "df -h"
#cmd = "df -h | awk '{print $(NF-1), $(NF-0)}'"

regex1 = re.compile(r'\d*\%')
regex2 = re.compile(r'\%\s*\/\w*')		# 

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def connection(host, port):
	print(host)
	ret = ''
	ssh.connect(host, username='id', port=port, password='pw')
	ssh.invoke_shell()
	stdin, stdout, stderr = ssh.exec_command(cmd)
	'''
	for line in stdout:
		#print(line, end="")
		match = regex.search(line)
		print(match)
	'''
	for line in stdout:
		ret += line
	match1 = regex1.findall(ret)
	match2 = regex2.findall(ret)
	print(match1)
	print(match2)
	ssh.close()

for i, p in hosts.items():
	connection(i, p)
