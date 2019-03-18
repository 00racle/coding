import paramiko
import cx_Oracle

conn_db = cx_Oracle.connect('db 계정')
db = conn_db.cursor()


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())


ssh.connect('ip', username='id', port='port', password='pw')
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
