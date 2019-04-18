from pwn import *

shell = ssh('chk1417', '192.168.6.222', port=24477, password='8282op82@#')
print(shell['ls'])

shell.close()
