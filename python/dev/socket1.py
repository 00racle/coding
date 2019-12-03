from socket import *

s = socket(AF_INET, SOCK_STREA)
s.connect('localhost', 4444)
