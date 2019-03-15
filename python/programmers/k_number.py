n = [1,5,2,6,3,7,4]
cmd = [[2,5,3],[4,4,1],[1,7,3]]

'''
def solution(n, cmd):
	ret = []
	for i in cmd:
		a = n[i[0]-1:i[1]]
		a.sort()
		ret.append(a[i[2]-1])
	return ret
'''
'''
def solution(n, cmd):
	return list(map(lambda x:sorted(n[x[0]-1:x[1]])[x[2]-1], cmd))
'''
def solution(n, cmd):
	return list(map(lambda x:sorted(n[x[0]-1:x[1]]), cmd))
print(solution(n, cmd))
