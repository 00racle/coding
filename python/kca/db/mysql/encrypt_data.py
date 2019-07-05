import pymysql
'''
패스워드 AES 로 암호화 하여 저장, 키값은 IP
'''

conn_db = pymysql.connect(host='x.x.x.x', user='chk1417', password='xxxxxxx', db='dchk')
curs = conn_db.cursor()

result = curs.fetchall()

for i in result:
	curs.execute("update t_svr set pw=HEX(AES_ENCRYPT(%s, %s)) where ip=%s;", (i[4], i[1], i[1]))

conn_db.commit()
conn_db.close()


'''
암호화된 값 복호화하여 읽어올떄
'''

conn_db = pymysql.connect(host='192.168.6.160', user='chk1417', password='8282op82@#', db='dchk')
curs = conn_db.cursor()

sql = "select ip, port, id, AES_DECRYPT(UNHEX(pw), ip) as pw from t_svr;"
curs.execute(sql)

result = curs.fetchall()

for i in result:
	print(i[3].decode('utf-8'))		# b'문자열' 이런식으로 binary 형태로 출력, utf-8로 디코딩 필요

