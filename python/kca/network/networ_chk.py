from netmiko inport ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException
import pymysql
import time
from datetime import datetime

# 수행시간 기록
start_time = time.time()

# DB 접속
conn_db = pymysql.connect(host = 'IP', user='ID', password='PW',db = 'DB명')
curs = conn_db.cursor()

# sql 실행
sql = "select * from net;"
curs.execute(sql)

# sql 실행결과 result 변수에 리스트로 저장
result = curs.fetchall()
conn_db.close()

#d[0]=ip, d[1]=port, d[2]=id, d[3]=pw, d[4]=class, d[5]=model, d[6]=hostname

def cisco(d):
	print("접속 장비: %s [%s]"%(d[6], d[0]))
	cisco = {
		'device_type' : 'cisco_ios',
		'ip' : d[0],
		'username' : d[2],
		'password' : d[3],
		'port' : d[1],
	}
	try:
		net_connect = ConnectHandler(**cisco)
		net_connect.send_command("enable"+'\n', expect_string=r'Password:')
		net_connect.send_command(d[3], expect_string=r'#')
		utput = net_connect.send_command("show start | in hostname")
		print(output)
	except NetMikoTimeoutException:
		print("장비 접속 불가(타임아웃)")
	except NetMikoAuthenticationException:
		print("장비 접속 불가(인증에러)")

def alcatel(d):
	print("접속 장비: %s [%s]"%(d[6], d[0]))
	alcatel = { 
		'device_type' : 'alcatel_aos',
		'ip' : d[0],
		'username' : d[2],
		'password' : d[3],
		'port' : d[1],
	}   
	try:
		net_connect = ConnectHandler(**alcatel)
		# delay_factor=20 이 없으면 명령어 실행결과값 중간에 잘림
		output = net_connect.send_command("show configuration snapshot", delay_factor=20)
		print(output)


for d in result:
	if d[5] == 'CISCO':
		cisco(d)
	if d[5] == 'ALCATEL-LUCENT':
		alcatel(d)

print("Runtime: %.02f"%(time.time() - start_time))
