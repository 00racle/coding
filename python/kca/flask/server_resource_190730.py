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

'''
@app.route('/mem',methods=['POST', 'GET'])
def mem():
    mems = []
    for i in hosts:
        m = list(db[i].find({},{"_id":0, "mem":1}).sort("date", pymongo.DESCENDING).limit(1))
        mems.append(m[0]['mem'])
    
    mem_ret = dict(zip(hosts, mems))
    mem_ret_sort = sorted(mem_ret.items(), key=lambda k : k[1], reverse=True)

    return render_template('mem_graph_0726_v1.html',data=mem_ret_sort)

@app.route('/cpu',methods=['POST', 'GET'])
def cpu():
    cpus = []
    for i in hosts:
        c = list(db[i].find({},{"_id":0, "cpu":1}).sort("date", pymongo.DESCENDING).limit(1))
        cpus.append(c[0]['cpu'])

    cpu_ret = dict(zip(hosts, cpus))
    cpu_ret_sort = sorted(cpu_ret.items(), key=lambda k : k[1], reverse=True)
    return render_template('cpu_table.html',data=cpu_ret_sort)
'''
@app.route('/resource',methods=['POST', 'GET'])
def resource():
    mems = []
    cpus = []
    disks = []
    for i in hosts:
        m = list(db[i].find({},{"_id":0, "mem":1}).sort("date", pymongo.DESCENDING).limit(1))
        c = list(db[i].find({},{"_id":0, "cpu":1}).sort("date", pymongo.DESCENDING).limit(1))
        d = list(db[i].find({},{"_id":0, "disk":1}).sort("date", pymongo.DESCENDING).limit(1))
        mems.append(m[0]['mem'])
        cpus.append(c[0]['cpu'])
        d2 = d[0]['disk']
        d3 = []
        for j in d2:
            j[0] = j[0].replace("%", "")
            if int(j[0]) >= 85:
                d3.append(j)
        disks.append(d3)

    
    mem_ret = dict(zip(hosts, mems))
    cpu_ret = dict(zip(hosts, cpus))
    disk_ret = dict(zip(hosts, disks))
    mem_ret_sort = sorted(mem_ret.items(), key=lambda k : k[1], reverse=True)
    cpu_ret_sort = sorted(cpu_ret.items(), key=lambda k : k[1], reverse=True)
    disk_ret_sort = sorted(disk_ret.items(), key=lambda k : k[1], reverse=True)

    return render_template('resource_graph_0730_v1.html',mem_data=mem_ret_sort, cpu_data=cpu_ret_sort, disk_data=disk_ret_sort)

'''
@app.route('/disk',methods=['POST', 'GET'])
def disk():
    disks = []
    for i in hosts:
        d = list(db[i].find({},{"_id":0, "disk":1}).sort("date", pymongo.DESCENDING).limit(1))
        d2 = d[0]['disk']
        d3 = []
        for j in d2:
            j[0] = j[0].replace("%", "")
            if int(j[0]) >= 80:
                d3.append(j)

            
        #disks.append(d[0]['disk'])

        disks.append(d3)
    disk_ret = dict(zip(hosts, disks))
    disk_ret_sort = sorted(disk_ret.items(), key=lambda k : k[1], reverse=True)
    return render_template('disk_table_0730_v1.html', data=disk_ret_sort)
    #return render_template('disk_table_0725_v1.html', data=disk_ret_sort)
'''
conn.close()

if __name__=='__main__':
    app.run(host='0.0.0.0')
