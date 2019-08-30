import pymongo
import urllib.parse

username = urllib.parse.quote_plus('root')
password = urllib.parse.quote_plus('8282op82@#')
conn = pymongo.MongoClient('mongodb://%s:%s@192.168.6.105:28017'%(username, password))

db = connection.AAA										# AAA 라는 이름의 DB생성
collection = db.test									# test라는 이름의 컬랙션(테이블) 생성
db = conn.get_database("dchk")							# db 선택
collection = db.get_collection('컬랙션명') 				# 컬랙션(테이블) 선택
collection_list = db.collection_names()					# 선택된 DB의 collection 목록을 출력, return type = list




# 예시
db = conn.get_database("dchk")
collection = db.get_collection("ntp")
result = collection.find()
