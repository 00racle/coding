#arr = [5,9,7,10]
#d = 5
arr = [3,2,6]
divisor = 10
'''
def solution(arr, d):
	answer = []
	for i in arr:
		if i%d == 0:
			answer.append(i)
	answer.sort()
	if answer == []:
		return [-1]
	else:
		return answer
'''
def solution(arr, divisor):
	arr = [x for x in arr if x%divisor ==0]
	arr.sort()
	return arr if len(arr) != 0 else [-1]
print(solution(arr, divisor))
