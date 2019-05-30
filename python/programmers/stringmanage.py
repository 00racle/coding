s = "e1"
#s = "1aa234"
'''
def solution(s):
	for i in s:
		if ord(i) not in range(48, 57):
			return False
		else:
		 	return True

'''
def solution(s):
	if len(s) != (4 or 6):
		return False
	else:
	 	return True
print(solution(s))
