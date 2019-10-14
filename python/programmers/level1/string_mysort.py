#s = ["sun", "bed", "car"]
#s = ["abce", "abcd", "cdx"]
s = ["abcd", "cdx", "abc", "abcde"]

n = 2

def solution(s, n):
	cnt = 0
	a = [i[n] for i in s]
	if len(a) != len(set(a)):
		cnt += 1
	b = dict(zip(s, a))
	return sorted(b, key=lambda k : b[k]) if cnt == 0 else sorted(sorted(b, key=lambda k : b[k]))

print(solution(s, n))

