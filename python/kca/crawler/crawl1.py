from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://192.168.6.93/NmConsole/kca_cpu_status.asp?usageAtLeast=50')
source = html.read()

soup = BeautifulSoup(source, "html.parser")

print(soup)

