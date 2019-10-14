n = [1,5,3,6,7,6,5]

def solution(n):
	ret = [0]
	for i in range(1, len(n)):
		for j in reversed(range(i)):
			if n[i] < n[j]:
				ret.append(j+1)
				break
			elif j == 0:
				ret.append(0)
	print(ret)


solution(n)
