#s = ["sun", "bed", "car"]
s = ["abce", "abcd", "cdx"]
n = 1 
'''
def solution(s, n):
	ret = ""
	cnt = 0
	for i in s:
		if i[n] in ret:
			cnt += 1
		ret += i[n]
	a = dict(zip(s, ret))
	print(ret)
	#return sorted(sorted(a, key=lambda k : a[k])) if cnt == 1 else sorted(a, key=lambda k : a[k])
	return sorted(a, key=lambda k : a[k]) if cnt == 0 else sorted(sorted(a, key=lambda k : a[k]))
'''


def solution(s, n):
	cnt = 0
	a = [i[n] for i in s]
	if len(a) != len(set(a)):
		cnt += 1
	b = dict(zip(s, a))

	return sorted(b, key=lambda k : b[k]) if cnt == 0 else sorted(sorted(b, key=lambda k : b[k]))

print(solution(s, n))
