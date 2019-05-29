import math
import time

start_time = time.time()
n = 428135971041
n = 16
'''
def solution(n):
    answer = 0
    for i in range(1, 20):
    	if i**2 == n:
	    answer += i
    return -1 if answer == 0 else (answer+1)**2

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

print(solution(n))

print("Runtime: %.02f"%(time.time() - start_time))
#solution(n)
