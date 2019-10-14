s = "pPoooyY"
#s = "Pyy"

'''
def solution(s):
	pcnt = 0
	ycnt = 0
	for i in list(s):
		if i in ("Y","y"):
			ycnt += 1
		if i in ("p", "P"):
			pcnt += 1
	return 'true' if pcnt == ycnt else 'false' 
'''

#================= 다른사람 풀이 ==================

def solution(s):
	return s.lower().count('p') == s.lower().count('y')


print(solution(s))
