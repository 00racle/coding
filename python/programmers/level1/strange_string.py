#s = "try  hello world "
#s = "try hello world strys try"
s = "sp  ace"

def solution(s):
    answer = ""
	cnt = 0
	for i in list(s):
		if i != " ":
			if cnt%2 == 0:
				answer += i.upper()
				cnt += 1
			else:
				answer += i.lower()
				cnt += 1
		else:
			answer += " "
			cnt = 0

	return answer
            
print(solution(s))
