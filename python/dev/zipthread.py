import zipfile
import threading
import time

start_time = time.time()

pwlist = []
for i in range(10000):
	pwlist.append(str(i))

def Extract(zFile, pwstr):
	try:
		global fin
		zFile.extractall(pwd = pwstr.encode())
		print("Found Password : {0} ".format(pwstr))
	except:
		#print("Wrong Password : {0} ".format(pwstr))
		pass

def main():
	Filename = input("zipfile name: ")
	zFile = zipfile.ZipFile(Filename, 'r')

	print("Extraction Start -------------------- \n")
	for i in pwlist:
		t = threading.Thread(target=Extract, args=(zFile, i))
		t.start()

if __name__ == '__main__':
	main()

end_time = time.time()
print("Runtime : %0.6f"%(end_time - start_time))
