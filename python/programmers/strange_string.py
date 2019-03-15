s = "try hello world"

def solution(s):
	'''
	l = list(s)
	for i in range(len(l)):
		if i%2 == 0:
			l[i] = l[i].upper()
	
	return ''.join(l)
	'''
	'''
	answer = ''
	for i in range(len(s)):
		if i%2 == 0:
			answer += chr(ord(s[i])-32)
		else:
			answer += s[i]
	'''
	
solution(s)
#print(solution(s))
