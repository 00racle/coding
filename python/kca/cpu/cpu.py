import paramiko

hosts = {'ip': 'port', 'ip': 'port'}
cmd = "mpstat -P ALL | awk '{print $NF}' | sed -n '4, $'p"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def connection(host, port):
	ret = []
	print(host)
	ssh.connect(host, username='id', port=port, password='pw')
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
	


