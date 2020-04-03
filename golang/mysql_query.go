package main

import(
	"database/sql"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
)

func main(){
	db, err := sql.Open("mysql", "username:password@tcp(ip:3306)/dbname")
	if err != nil{
		fmt.Println(err)
	}
	defer db.Close()		// 지연하여 닫기

	var ip string
	var hostname string
	rows, err := db.Query("SELECT ip, hostname FROM v_svr limit 5")
	if err != nil{
		fmt.Println(err)
	}
	defer rows.Close()

	for rows.Next(){
		err := rows.Scan(&ip, &hostname)
		if err := nil{
			fmt.Println(err)
		}
		fmt.Println(ip, hostname)
	}
}
