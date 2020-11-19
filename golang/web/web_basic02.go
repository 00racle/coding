package main

import(
	"fmt"
	"net/http"
	"log"
	//"github.com/gorilla/mux"
)

func Mpage(w http.ResponseWriter, r *http.Request){
	// html 웹 페이지 작성
	html :=`
	<h1>Hello, World!</h1>
	`
	// html 헤더 설정
	// w.Header().Set("Content-Type", "text/html")
	fmt.Fprintln(w, html)
}

//var router = mux.NewRouter()

func main(){
	//router.HandleFunc("/", Mpage)
	//http.Handle("/", router)
	//http.ListenAndServe(":8632", nil)

	http.HandleFunc("/", Mpage)
	err := http.ListenAndServe(":8632", nil)

	if err != nil{
		log.Fatal("ListenAndServe: ", err)
	}else{
		fmt.Println("ListenAndServe Started! -> Port(8632)")
	}
}
