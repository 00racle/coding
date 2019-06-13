import pymysql

# Connect to the database
connection = pymysql.connect(host = 'x.x.x.x', user = 'user', password = 'password', db = 'db_name', charset = 'utf8mb4', cursorclass = pymysql.cursor.DictCursor)


try:
	with connection.cursor() as cursor:
		# Create a new record
		sql = "INSERT INTO 'users' ('email', 'password') VALUES (%s, %s)"
		cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

	# connection in not autocommit by default. So you must commit to save
	connection.commit()

	with connection.cursor() as cursor:
		# Read a single record
		sql = "SELECT 'id', 'password' FROM 'users' WHERE 'email'=%s"
		cursor.execute(sql, ('webmaster@python.org',))
		result = cursor.fetchone()			# or fetchall(), fetchmany(n)
		print(result)
finally:
	connection.close()

'''
예제) 리스트 에서 db insert

데이터 형식
L = ['pc-off', '192.168.6.158', 24477]
L = ['logcenter', '192.168.7.101', 24477]

for i in l:
	L = i.split(' ')
	L[1] = L[1].replace("ansible_host=", "")
	L[2] = int(L[2].replace("ansible_port=", "").replace("\n", ""))
	sql = "insert into v_svr(ip, port, id, pw, os, hostname)  values(%s, %s, 'chk1417', '8282op82@#', 'linux', %s);"
	curs.execute(sql, (L[1], L[2], L[0]))

conn_db.commit()
conn_db.close()
