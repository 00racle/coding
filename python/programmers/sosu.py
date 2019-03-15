import time

start = time.time()
n = 10

def solution(n):
	out = []
	for i in range(1, n+1):
		ret = []
		for j in range(1, i+1):
			if i%j == 0:
				ret.append(j)
		if len(ret) == 2:
			out.append(i)
			

	print(len(out))
	print(out)
				

solution(n)
end = time.time()
print("Runtime: %.06f"%(start - end))
