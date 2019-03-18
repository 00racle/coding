import paramiko
import cx_Oracle
from datetime import datetime

host = 'ip'
port = port
cmd = "ps aux | awk '$3 > 90.0 {print $2, $3, $11}'"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ret = []
f = open('/root/crawler/test/test/db_query/result/result_pid_somang.txt', 'a')
def conn(host, port, cmd):
	pid = []
	ssh.connect(host, username='id', port=port, password='pw')
	ssh.invoke_shell()
	stdin, stdout, stderr = ssh.exec_command(cmd)
	for line in stdout:
		f.write(line)
		a = line.rstrip('\n').split(' ')
		ret.append(a)
	for i in range(len(ret)):
		pid.append(ret[i][0])
	return pid
	ssh.close()

def query():
	spid = conn(host, port, cmd)
	conn_db = cx_Oracle.connect('oracle id')
	db = conn_db.cursor()
	for i in spid:
		db.execute("SELECT c.sql_text, a.* FROM v$session a, v$process b, v$sql c WHERE a.paddr = b.addr AND a.sql_address = c.address AND b.spid = :pid", pid=i)
		for line in db:
			f.write("PID: "+i+str(line))
	f.write("쿼리시각:"+str(datetime.now())+"\n")
	db.close()
	conn_db.close()

query()
f.close()
