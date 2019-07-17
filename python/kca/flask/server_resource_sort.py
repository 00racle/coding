import pymongo
import urllib.parse
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

username = urllib.parse.quote_plus('root')
password = urllib.parse.quote_plus('8282op82@#')
conn = pymongo.MongoClient('mongodb://%s:%s@192.168.6.105:27017'%(username, password))
db = conn.get_database("dchk")
#collection = db.ubuntu
hosts = db.collection_names()
@app.route('/mem',methods=['POST', 'GET'])
def mem():
    mems = []
    size = len(hosts)
    for i in hosts:
        m = list(db[i].find({},{"_id":0, "mem":1}).sort("date", pymongo.DESCENDING).limit(1))
        mems.append(m[0]['mem'])
    
    ret = dict(zip(hosts, mems))
    ret_sort = sorted(ret.items(), key=lambda k : k[1], reverse=True)

    #return render_template('mem_test.html',data=ret)
    return render_template('mem_test.html',data=ret_sort)

conn.close()

if __name__=='__main__':
    app.run(host='0.0.0.0')

