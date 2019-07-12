import paramiko
import time
import pymysql
import sys
from datetime import datetime
import pymongo
import urllib.parse

conn_db = pymysql.connect(host = '192.168.6.160', user='chk1417', password='8282op82@#', db='dchk')
curs = conn_db.cursor()

username = urllib.parse.quote_plus('root')
password = urllib.parse.quote_plus('8282op82@#')
conn = pymongo.MongoClient('mongodb://%s:%s@192.168.6.105:27017'%(username, password))
db = conn.get_database("dchk")

#sql = 'select ip, port, id, AES_DECRYPT(UNHEX(pw), ip) as pw, os, hostname from v_svr;'
sql = 'select ip, port, id, AES_DECRYPT(UNHEX(pw), ip) as pw, os, hostname from t_svr;'
#sql = 'select ip, port, id, AES_DECRYPT(UNHEX(pw), ip) as pw, os, hostname from t_svr where hostname="ubuntu-mongo";'
curs.execute(sql)

result = curs.fetchall()
conn_db.close()

cmd_mem = "free -m | awk '/Mem:/' | awk '{print $2, $3, $4}'"
cmd_df = "df -h | awk '{print $(NF-1), $(NF-0)}' | grep '%'"
cmd_cpu = "mpstat | awk '{print $NF}' | tail -1" 
cmd_uptime = "uptime | awk '{print $3}'"
now = datetime.now()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

def connection(svr):
	res_key = ["ip", "datetime", "uptime", "mem", "cpu", "disk"]
	res_values = []
	res_values.append(svr[0])
	df_ret = []
	res_values.append(str(now))
	#print("접속장비: "+svr[5])
	try:
		ssh.connect(svr[0], username=svr[2], port=svr[1], password=svr[3].decode('utf-8'))
		ssh.invoke_shell()

		stdin, stdout, stderr = ssh.exec_command(cmd_uptime)
		for line in stdout:
			res_values.append(int(line.rstrip('\n')))
		
		stdin, stdout, stderr = ssh.exec_command(cmd_mem)
		for line in stdout:
			a = line.rstrip('\n').split(' ')
			b = int(a[2])*100/int(a[0])
		res_values.append(int(b))

		stdin, stdout, stderr = ssh.exec_command(cmd_cpu)
		for line in stdout:
			c = (100-float(line.rstrip('n')))
			res_values.append(int(c))
	
		stdin, stdout, stderr = ssh.exec_command(cmd_df)
		for line in stdout:
			df_ret.append(line.split())
		res_values.append(df_ret)
		
		res = dict(zip(res_key, res_values))
		#print(res)
		db[svr[5]].insert(res)

	except paramiko.ssh_execption.NoValidConnectionsError as 접속불가:
		print("접속불가(포트에러)")
	
	except paramiko.ssh_execption.AuthenticationException as 접속불가:
		print("접속불가(인증에러)")
	
	ssh.close()


for svr in result:
	connection(svr)
