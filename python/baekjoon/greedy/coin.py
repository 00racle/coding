n, k = map(int, input().split())
lst = []
for i in range(n):
	lst.append(int(input()))
'''
n = 10
k = 4790
lst = [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]
'''
def solution(n, k, lst):
	answer = 0
	l = list(str(k))
	for i in l:
		answer += int(i)%5
		answer += int(i)//5

	return answer

print(solution(n, k, lst))
