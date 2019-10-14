n = 4
'''
def solution(n):
	if n%2 == 0:
		return "수박"*(n//2)
	else:
		return "수박"*(n//2)+"수"
'''
'''
내가 짜본 짧은 코딩
def solution(n):
	return "수박"*(n//2) if n%2 ==0 else "수박"*(n//2)+"수"
'''

# 다른사람이 쓴 짧은 코딩

def solution(n):
	s = "수박"*n
	return s[:n]
print(solution(n))
