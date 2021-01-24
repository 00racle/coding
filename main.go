package main

import(
	"fmt"
	"encoding/json"
	//"io/ioutil"
	"log"
	"net/http"
	"github.com/gorilla/mux"
)

type member struct{
	No			string `json:"No"`
	Name		string `json:"Name"`
	ID			string `json:"ID"`
	Rank		string `json:"Rank"`
	Job			string `json:"Job"`
	Location	string `json:"Location"`
}

type allMembers []member

var members = allMembers{
	{
		No:					"1",
		Name:				"송태진",
		ID:					"2008001",
		Rank:				"부장",
		Job:				"팀장",
		Location:			"(0,0)",
	},
	{
		No:					"2",
		Name:				"황인환",
		ID:					"2009001",
		Rank:				"차장",
		Job:				"정보보안",
		Location:			"(1,0)",
	},
	{
		No:					"3",
		Name:				"한승",
		ID:					"2010001",
		Rank:				"과장",
		Job:				"기획",
		Location:			"(1,1)",
	},
	{
		No:					"4",
		Name:				"김대호",
		ID:					"2010001",
		Rank:				"과장",
		Job:				"개인정보보호",
		Location:			"(2,0)",
	},
	{
		No:					"5",
		Name:				"이창민",
		ID:					"2010001",
		Rank:				"과장",
		Job:				"기획",
		Location:			"(2,1)",
	},
	{
		No:					"6",
		Name:				"우지만",
		ID:					"2010001",
		Rank:				"과장",
		Job:				"소망",
		Location:			"(3,0)",
	},
	{
		No:					"7",
		Name:				"박향연",
		ID:					"2010001",
		Rank:				"과장",
		Job:				"정보보안",
		Location:			"(3,1)",
	},
	{
		No:					"8",
		Name:				"임정미",
		ID:					"2010001",
		Rank:				"과장",
		Job:				"EA",
		Location:			"(3,2)",
	},
	{
		No:					"9",
		Name:				"문경준",
		ID:					"2019001",
		Rank:				"조사관",
		Job:				"기획",
		Location:			"(1,2)",
	},
	{
		No:					"10",
		Name:				"박정기",
		ID:					"2018001",
		Rank:				"실무관",
		Job:				"통합유지보수",
		Location:			"(1,3)",
	},
	{
		No:					"11",
		Name:				"황인환",
		ID:					"2018001",
		Rank:				"실무관",
		Job:				"홈페이지",
		Location:			"(2,4)",
	},
	{
		No:					"11",
		Name:				"문경호",
		ID:					"2018001",
		Rank:				"실무관",
		Job:				"VDI",
		Location:			"(3,3)",
	},
	{
		No:					"12",
		Name:				"한성용",
		ID:					"2018001",
		Rank:				"실무관",
		Job:				"기획",
		Location:			"(2,2)",
	},
	{
		No:					"13",
		Name:				"설진남",
		ID:					"2018001",
		Rank:				"실무관",
		Job:				"소비넷",
		Location:			"(2,3)",
	},
	{
		No:					"14",
		Name:				"이승진",
		ID:					"2018001",
		Rank:				"실무관",
		Job:				"소망",
		Location:			"(1,4)",
	},
	{
		No:					"15",
		Name:				"최용준",
		ID:					"2018080",
		Rank:				"실무관",
		Job:				"네트워크",
		Location:			"(4,4)",
	},
}
func getAllMembers(w http.ResponseWriter, r *http.Request){
	//json.NewEncoder(w).Encode(members)
	for _, singleMember := range members{
		json.NewEncoder(w).Encode(singleMember)
	}
}

func getOneMember(w http.ResponseWriter, r *http.Request){
	memberNo := mux.Vars(r)["No"]

	for _, singleMember := range members {
		if singleMember.No == memberNo {
			json.NewEncoder(w).Encode(singleMember)
		}
	}
}

func getMembername(w http.ResponseWriter, r *http.Request){
	memberName := mux.Vars(r)["Name"]

	for _, singleMember := range members {
		if singleMember.Name == memberName {
			json.NewEncoder(w).Encode(singleMember)
		}
	}
}

func homeLink(w http.ResponseWriter, r *http.Request){
	fmt.Fprintf(w, "Welcom home!")
}

func main(){
	router := mux.NewRouter().StrictSlash(true)
	router.HandleFunc("/", homeLink)
	router.HandleFunc("/members", getAllMembers).Methods("GET")
	router.HandleFunc("/members/number/{No}", getOneMember).Methods("GET")
	router.HandleFunc("/members/name/{Name}", getMembername).Methods("GET")
	log.Fatal(http.ListenAndServe(":8080", router))
}
