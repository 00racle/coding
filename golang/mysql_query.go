package main

import(
	"database/sql"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
)

func main(){
	// mysql 접속
	db, err := sql.Open("mysql", "username:password@tcp(ip:3306)/dbname")
	if err != nil{
		fmt.Println(err)		// or 'panic(err.Error())'
	}
	defer db.Close()			// 지연하여 닫기

	// db query, 1행
	var name string
	db.QueryRow("SELECT ip, hostname FROM v_svr where ip='1.1.1.1'").Scan(&name)

	// where절 변수 받아서 query
	type server struct{
		Hostname	string `json:"Hostname"`
		OS			string `json:"OS"`
		IP			string `json:"IP"`
		Port		string `json:"Port"`
	}
	var svr server
	serverIP := "10.10.10.10"
	err = db.QueryRow("SELECT hostname, os, ip, port FROM v_svr where ip = ?", serverIP).Scan(&svr.Hostname, &svr.OS, &svr.IP, &svr.Port)


	// db query, 여러행
	var ip string
	var hostname string
	rows, err := db.Query("SELECT ip, hostname FROM v_svr limit 5")
	if err != nil{
		fmt.Println(err)
	}
	defer rows.Close()

	for rows.Next(){
		// ip, hostname 변수에 할당
		err := rows.Scan(&ip, &hostname)
		if err := nil{
			fmt.Println(err)
		}
		fmt.Println(ip, hostname)
	}
	
	// INSERT data
	var1 := 1234
	var2 := "test"
	var3 := 4567

	_, err = db.Exec("INSERT INTO tablename(col1, col2, col3) VALUES(?, ?, ?)",var1, var2, var3)
	if err != nil {
		panic(err.Error())
	}
}
