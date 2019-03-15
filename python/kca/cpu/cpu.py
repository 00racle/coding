import paramiko

hosts = {'192.168.6.222': '24477', '192.168.6.250': '24477', '192.168.6.239': '24477'}
cmd = "mpstat -P ALL | awk '{print $NF}' | sed -n '4, $'p"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def connection(host, port):
	ret = []
	print(host)
	ssh.connect(host, username='chk1417', port=port, password='8282op82@#')
	ssh.invoke_shell()
	stdin, stdout, stderr = ssh.exec_command(cmd)
	for line in stdout:
		ret.append(float(line.strip()))
	#s = sum(ret)
	#l = len(ret)
	#print(ret)
	print("%d"%(100-(sum(ret)/len(ret))))

	ssh.close()


for i, p in hosts.items():
	connection(i, p)
	


