n = int(input("정수 n입력: "))

def solution(n):
	s = str(n)
	sum = 0
	for i in s:
		sum += int(i)
	if n%sum == 0:
		return True
	else:
		return True
'''
프로그래머스 답
def solution(n):
	return n%sum([int(i) for i in str(n)]) == 0
'''
print(solution(n))
#solution(n)
