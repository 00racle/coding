import time

start = time.time()

n = [3, 30, 34, 5, 9]		
#n = [6, 10, 2]

def solution(n):
	'''
================ 1번째 방법 ==================
	ret = []
	sn = sorted(n)
	for j in range(len(sn)):
		Max = 0
		for i in sn:
			if int(str(i)[0]) > int(str(Max)[0]):
				Max = i
			elif int(str(i)[0]) == int(str(Max)[0]):
				if int(str(i)[1]) > int(str(Max)[0]):
					Max = i
		ret.append(str(Max))
		sn.remove(Max)
	
	print(ret)
	return ''.join(ret)
	'''
	ret = ''
	for j in range(len(n)):
		Max = 0
		for i in sorted(n):
			if int(str(i)[0]) > int(str(Max)[0]):
				Max = i
			elif int(str(i)[0]) == int(str(Max)[0]):
				if int(str(i)[1]) > int(str(Max)[0]):
					Max = i
		ret += str(Max)
		n.remove(Max)

	return ret


print(solution(n))
end = time.time()

print("Runtime: %0.6f"%(start - end))
