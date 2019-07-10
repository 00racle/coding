import pymongo
import json
import datetime
from pymongo import MongoClient

# json 타입의 문자열을 파이선 타입(딕셔너리)으로 변환해서 저장하는 예제

client = MongoClient("localhost", 27017)
db = client.nlu
db.logging

mydata = """
{"name": "yongjun", "age": 35}
"""

d = json.loads(mydata)
d['date'] = datetime.datetime.utcnow()

postid = db.logging.insert_one(d).inserted_id
