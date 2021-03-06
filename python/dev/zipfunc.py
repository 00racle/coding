import zipfile
import threading
import time

start_time = time.time()

fin = True

pwlist = []
for i in range(1000000):
	pwlist.append(str(i))

def Extract(zFile, pwstr):
	try:
		global fin
		zFile.extractall(pwd = pwstr.encode())
		print("Found Password : {0} ".format(pwstr))
		fin = False
	except:
		print("Wrong Password: {0} ".format(pwstr))
		pass

def main():
	Filename = input("zipfile name: ")
	zFile = zipfile.ZipFile(Filename, 'r')

	print("Extraction Start -------------------- \n")
	for i in pwlist:
		Extract(zFile, i)
		if fin == False:
			break

if __name__=='__main__':
	main()

end_time = time.time()

print("Runtime : %0.6f"%(end_time - start_time))
