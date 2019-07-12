import pymongo
import urllib.parse

#conn = pymongo.MongoClient("192.168.6.105", 27017)
username = urllib.parse.quote_plus('root')
password = urllib.parse.quote_plus('8282op82@#')
conn = pymongo.MongoClient('mongodb://%s:%s@192.168.6.105:27017'%(username, password))
db = conn.get_database("dchk")
collection = db.get_collection("ubuntu")

collection_list = db.collection_names()
print(collection_list)
