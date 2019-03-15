import paramiko
import cx_Oracle

conn_db = cx_Oracle.connect('espresso/8282082@192.168.6.206:1521/cpberp11')
db = conn_db.cursor()


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


ssh.connect('192.168.6.206', username='chk1417', port='24477', password='8282op82@#')
ssh.invoke_shell()
stdin, stdout, stderr = ssh.exec_command("ps aux | grep oracleCPBERP11 | sed -n '1p' | awk '{print $2}'")
for line in stdout:
	s = int(line)
	print(s)

ssh.close()


db.execute("SELECT c.sql_text, a.username FROM v$session a, v$process b, v$sql c WHERE a.paddr = b.addr AND a.sql_address = c.address AND b.spid = :pid", pid=s)

for line in db:
	print(line)

db.close()
conn_db.close()
