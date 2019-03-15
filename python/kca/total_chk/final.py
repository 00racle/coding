import paramiko
import cx_Oracle

cmd_mem = "free -m | awk '/Mem:/' | awk '{print $2, $3, $4}'"
cmd_df = "df -h | awk '{print $(NF-1), $(NF-0)}' | grep '%'"
cmd_cpu = "mpstat -P ALL | awk '{print $NF}' | sed -n '4, $'p" 
cmd_uptime = "uptime | awk '{print $3}'"

conn_db = cx_Oracle.connect('espresso/8282082@192.168.6.206:1521/cpberp11')
db = conn_db.cursor()
db.execute('select ip, port from svr_list')

host_ret = []
for record in db:
	c = list(record)
	host_ret.append(c)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def conn(host, port):
	df_ret = []
	cpu_ret = []
	print(host)
	ssh.connect(host, username='chk1417', port=port, password='8282op82@#')
	ssh.invoke_shell()

	stdin, stdout, stderr = ssh.exec_command(cmd_uptime)
	for line in stdout:
		print("Uptime:",line, end='')

	stdin, stdout, stderr = ssh.exec_command(cmd_mem)
	for line in stdout:
		a = line.rstrip('\n').split(' ')
		b = int(a[2])*100/int(a[0])
	#print("Mem:","%0.3f"%b)
	print("Mem:","%d"%b)

	stdin, stdout, stderr = ssh.exec_command(cmd_cpu)
	for line in stdout:
		cpu_ret.append(float(line.strip()))
	print("Cpu:","%d"%(100-(sum(cpu_ret)/len(cpu_ret))))

	stdin, stdout, stderr = ssh.exec_command(cmd_df)
	for line in stdout:
		df_ret.append(line.split())
	print(df_ret)

	ssh.close()

for i in range(len(host_ret)):
	conn(host_ret[i][0], host_ret[i][1])

db.close()
conn_db.close()
