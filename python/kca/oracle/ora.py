import cx_Oracle
import paramiko

cmd = "free -m | awk '/Mem:/' | awk '{print $2, $3, $4}'"
conn = cx_Oracle.connect('db 계정')
db = conn.cursor()
db.execute('select ip, port from svr_list')


ret = []
for record in db:
	#print(list(record))
	c = list(record)
	#A = a[0].replace("'","",2)
	#print(A)
	#print(record[0])
	ret.append(c)

#print(ret)
db.close()
conn.close()


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def connection(host, port):
	print(host)
	ssh.connect(host, username='id', port=port, password='pw')
	ssh.invoke_shell()
	stdin, stdout, stderr = ssh.exec_command(cmd)
	for line in stdout:
		a = line.rstrip('\n').split(' ')
		b = int(a[2])*100/int(a[0])
		print("%0.1f"%b)
	ssh.close()


for i in range(len(ret)):
	#print(ret[i][0])
	connection(ret[i][0], ret[i][1])
		
