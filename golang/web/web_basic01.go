package main

import(
	"fmt"
	"net/http"
	"log"
)

func Mpage(w http.ResponseWriter, r *http.Request){
	if r.Method != "POST"{
		fmt.Fprint(w, "Hello, world!")
		fmt.Println("IP주소: ", r.RemoteAddr)
		fmt.Println("프로토콜: ", r.Proto)
		fmt.Println("메소드: ", r.Method)
		fmt.Println("헤더: ", r.Header)
		fmt.Println("호스트: ", r.Host)
		fmt.Println("TLS: ", r.TLS)
	}
}

func main(){
	// 기본 URL 핸들러 메소드 지정
	http.HandleFunc("/", Mpage)

	// 서버 시작
	err := http.ListenAndServe(":8632", nil)

	// 예외 처리
	if err != nil{
		log.Fatal("ListenAndServe: ", err)
	}else{
		fmt.Println("ListenAndServe Started! -> Port(8632)")
	}
}
