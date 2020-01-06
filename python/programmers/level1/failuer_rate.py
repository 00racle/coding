n = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

def solution(n, stages):
	ret = {}
	ret1 = []
	length = len(stages)
	stages.sort()
	for i in range(1, n+1):
		su = stages.count(i)
		if(su == 0):
			ret[i] = 0
		else:
			ret[i] = su/length
		length = length - su

	l = sorted(ret.items(), key=lambda x: x[1], reverse=True)
	for i in l:
		ret1.append(i[0])
	return ret1

print(solution(n, stages))

