import requests
from bs4 import BeautifulSoup

req = requests.get('http://192.168.6.93/NmConsole/kca_cpu_status.asp?usageAtLeast=95')
#req.encoding = None
req.encoding = 'euc-kr'
html = req.text

soup = BeautifulSoup(html, "html.parser")

s = str(soup)
l = s.split("\n")

print("="*100)
for i in l:
	print(i)
print("="*100)


ret1 = []
ret2 = []
for i in l[:-1]:
	I = i.split('\t')
	if "DB" in I[0]:
		ret1.append(I[0])
		ret2.append(I[3])
			
print(ret1, ret2)
print(dict(zip(ret1, ret2)))






