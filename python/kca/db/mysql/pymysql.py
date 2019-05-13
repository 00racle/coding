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
