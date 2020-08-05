import pymysql

conn_db = pymysql.connect(host='192.168.6.160', user='chk1417', password='8282op82@#', db='dchk')
curs = conn_db.cursor()

'''
+----------+-------------+------+-----+---------+-------+
| Field    | Type        | Null | Key | Default | Extra |
+----------+-------------+------+-----+---------+-------+
| n_num    | int(3)      | NO   |     | NULL    |       |
| ip       | varchar(30) | NO   | PRI | NULL    |       |
| port     | int(6)      | NO   |     | NULL    |       |
| id       | varchar(30) | NO   |     | NULL    |       |
| pw       | char(32)    | YES  |     | NULL    |       |
| class    | varchar(40) | NO   |     | NULL    |       |
| model    | varchar(50) | NO   |     | NULL    |       |
| hostname | varchar(30) | NO   |     | NULL    |       |
+----------+-------------+------+-----+---------+-------+
'''


curs.execute("insert into net values(31, 'x.x.x.1', 포트번호, '계정', HEX(AES_ENCRYPT('비번', 'x.x.x.1')), 'CISCO', 'WS-C2960X-24TS-LL', '호스트네임');")

conn_db.commit()
conn_db.close()
