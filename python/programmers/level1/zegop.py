import math
import time

start_time = time.time()
#n = 428135971041
n = 122
#n = 1
'''
def solution(n):
	answer = 0
	l = math.ceil(len(str(n))/2)
	print("길이: %d"%l)
	print(10**l)
	print(10**(l-1))
	if n%10 not in [0, 1, 4, 5, 6, 9]:
		return -1
	else:
		for i in range(10**(l-1), 10**l):
			if i**2 == n:
				answer += i
	return (answer+1)**2
'''

def solution(n):
	#return (int(math.sqrt(n)) +1)**2 if n%10 in [0, 1, 4, 5, 6, 0] else -1

	return ((math.sqrt(n))+1)**2 if math.sqrt(n) == int(math.sqrt(n)) else -1

print(solution(n))

print("Runtime: %.02f"%(time.time() - start_time))
#solution(n)
