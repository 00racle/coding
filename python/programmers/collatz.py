n = int(input("정수 입력: "))

'''
def solution(n):
	cnt = 0
	while n != 1:
		if n%2 == 0:
			n = n/2
			cnt += 1
		else:
			n = n*3+1
			cnt += 1
		if cnt >= 500:
			break

	return -1 if cnt >= 500 else cnt
'''
# =================== 다른사람 풀이 ==================

def solution(n):
	for i in range(500):
		n = n/2 if n%2 == 0 else n*3+1
		if n == 1:
			return i + 1
	return -1



print(solution(n))

