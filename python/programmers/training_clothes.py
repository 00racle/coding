import time

start = time.time()
n = 5
lost = [2,4]
reserve = [1,3,5]

#lost = [2,4]
#reserve = [3]
'''
def solution(n, lost, reserve):
	cnt = n - len(lost)
	for i in reserve:
		if i-1 in lost:
			cnt += 1
			lost.remove(i-1)
		elif i+1 in lost:
			cnt += 1
			lost.remove(i+1)
'''
def solution(n, lost, reserve):
	cnt = n - len(lost)
	for i in reserve:
		if i-1 in lost:
			cnt += 1
			lost.pop()
		elif i+1 in lost:
			cnt += 1
			lost.pop()
	return cnt
print(solution(n, lost, reserve))

end = time.time()
print("Runtime: %.09f"%((start - end)/60))
