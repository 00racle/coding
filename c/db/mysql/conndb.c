#include <stdio.h>
#include "/usr/include/mysql/mysql.h"
#include <string.h>

#define DB_HOST	"127.0.0.1"
#define DB_USER	"user"
#define	DB_PASS	"password"
#define	DB_NAME	"dbname"

int main(void)
{

	MYSQL		*connection=NULL, conn;
	MYSQL_RES	*sql_result;
	MYSQL_ROW	sql_row;
	int			query_stat;

	mysql_init(&conn);

	connection = mysql_real_connect(&conn, DB_HOST, DB_USER, DB_PASS, DB_NAME, 3306, (char*)NULL, 0);

	if(connection == NULL)
	{
		printf("연결 실패\n");
	}
	else
	{
		printf("연결 성공\n");
	}

	query_stat = mysql_query(connection, "select ip, port, hostname from net");
	if(query_stat != 0)
	{
		fprintf(stderr, "Mysql query error: %s\n", mysql_error(&conn));
		return 1;
	}
	sql_result = mysql_store_result(connection);
	printf("%s %s %s\n", "아이피", "포트", "호스트네임");
	while((sql_row = mysql_fetch_row(sql_result)) != NULL)
	{
		printf("%s %s %s\n", sql_row[0], sql_row[1], sql_row[2]);
	}

	return 0;
}
