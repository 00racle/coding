import pwn

p = pwn.process(['telnet', '192.168.6.111'])

print(p.recvuntil('kali login: '))
p.sendline('test1')     #userid

print(p.recvuntil('Password: '))
p.sendline('1234')

print(p.recvuntil('$'))
p.sendline('echo 1234')

print(p.recvline())
