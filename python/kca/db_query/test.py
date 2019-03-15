from datetime import datetime

f = open('/root/crawler/test/test/db_query/test.txt', 'a')
f.write("현재시각: "+str(datetime.now())+"\n")
f.close()
