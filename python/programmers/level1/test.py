n = "Zbcdefg"
'''
def solution(n):
	ret = []
	answer = ''
	for i in n:
		a = ord(i)
		ret.append(a)
	ret.reverse()
	print(ret)
	for j in ret:
		b = chr(j)
		answer += b
	print(answer)
solution(n)
'''

def solution(n):
	answer = ''
	a = list(map(lambda x:ord(x), n))
	a.reverse()
	answer = "".join(map(lambda x:chr(x), a))
	return answer

print(solution(n))
