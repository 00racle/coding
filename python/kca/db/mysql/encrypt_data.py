import pymysql
'''
패스워드 AES 로 암호화 하여 저장, 키값은 IP
'''

conn_db = pymysql.connect(host='x.x.x.x', user='chk1417', password='xxxxxxx', db='dchk')
curs = conn_db.cursor()

result = curs.fetchall()

for i in result:
	curs.execute("update net set pw=HEX(AES_ENCRYPT(%s, %s)) where ip=%s;", (i[4], i[1], i[1]))

conn_db.commit()
conn_db.close()
