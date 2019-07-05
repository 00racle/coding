import pymysql

conn_db = pymysql.connect(host='x.x.x.x', user='xxxxx', password='xxxxxx', db='dchk')
curs = conn_db.cursor()

'''
svr_list.txt 는 아래 형식

linux1 ansible_host=192.168.0.1 ansible_port=24477
linux2 ansible_host=192.168.0.2 ansible_port=22
linux3 ansible_host=192.168.0.3 ansible_port=24477
linux4 ansible_host=192.168.0.4 ansible_port=22
'''

f = open('svr_list.txt', 'r')

l = f.readlines()

for i in l:
	L = i.split(' ')
	L[1] = L[1].replace("ansible_host=", "")
	L[2] = int(L[2].replace("ansible_port=", "").replace("\n", ""))
	sql = "insert into v_svr(ip, port, id, pw, os, hostname)  values(%s, %s, 'chk1417', '8282op82@#', 'linux', %s);"
	curs.execute(sql, (L[1], L[2], L[0]))

conn_db.commit()
conn_db.close()
f.close()
