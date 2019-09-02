import time

start = time.time()
#n = 3
#lost = [1,2]
#reserve = [2,3]
# 답 2
n = 24
lost = [12, 13, 16, 17, 19, 20, 21, 22]
reserve = [1, 22, 16, 18, 9, 10]
# 답 19

def solution(n, lost, reserve):
	'''
	cnt = n - len(lost)
	for i in reserve:
		if i-1 in lost:
			cnt += 1
			lost.remove(i-1)
		elif i+1 in lost:
			cnt += 1
			lost.remove(i+1)
	return cnt
	'''

print(solution(n, lost, reserve))

end = time.time()
print("Runtime: %.09f"%((start - end)/60))
