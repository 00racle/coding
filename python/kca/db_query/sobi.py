import paramiko
import cx_Oracle
from datetime import datetime

host = '192.168.6.101'
port = 24477
cmd = "ps aux | awk '$3 > 60.0 {print $2, $3, $11}'"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ret = []
f = open('/root/crawler/test/test/db_query/result/result_pid_sobi.txt', 'a')
def conn(host, port, cmd):
	pid = []
	ssh.connect(host, username='chk1417', port=port, password='8282op82@#')
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
	conn_db = cx_Oracle.connect('CPBNET/cpbnethit@192.168.6.101:1521/CPB11')
	db = conn_db.cursor()
	for i in spid:
		#db.execute("SELECT c.sql_text, a.* FROM v$session a, v$process b, v$sql c WHERE a.paddr = b.addr AND a.sql_address = c.address AND b.spid = :pid", pid=i)
		db.execute("select a.sql_text from v$sql a where 1=1 and address = (select sql_address from v$session where paddr = (select addr from v$process where spid = :pid))", pid=i)
		for line in db:
			f.write("PID: "+i+str(line))
	f.write("쿼리시각:"+str(datetime.now())+"\n")
	db.close()
	conn_db.close()

query()
f.close()
