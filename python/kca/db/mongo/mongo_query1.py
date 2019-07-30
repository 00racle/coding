import pymongo
import urllib.parse
import traceback

username = urllib.parse.quote_plus('root')
password = urllib.parse.quote_plus('8282op82@#')

def main():
	try:
		conn = pymongo.MongoClient('mongodb://%s:%s@192.168.6.105:28017'%(username, password))
		db = conn['dchk']				# db명
		print("MongoDB Connected. ")
		cursor = db.ntp.find()		# 
		print(list(cursor))

	except Exception as e:
		print(traceback.format_exc())
	finally:
		conn.close()
		print("MongoDB Closed. ")

if __name__ == "__main__":
	main()
