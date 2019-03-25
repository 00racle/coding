import zipfile
import threading

fin = True
char = []
name = input("file:")
for x in range(0.10000):
    char.append(str(x))
it = iter(char)

def extract(File.password):
    try:
        global fin
        zFile = zipfile.ZipFile(File)
        zFile.extractall(pwd=password)
        fin = False
        print(password)
        raw_input()
    except:
        pass
while fin:
    try:
        t = threading.Thread(target=extract, args=(name.next(ut)))
        t.start()
    except:
        pass
     
