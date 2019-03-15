#1. 1,2,3,4,5,1,2,3,4,5
#2. 2,1,2,3,2,4,2,5,2,1,2,3,2,4,2,5
#3. 3,3,1,1,2,2,4,4,5,5,3,3,1,1,2,2,4,4,5,5

answers = [1,2,3,4,5]
#answers = [1,3,2,4,2]

def solution(answers):
	answer = []
	cnt = 0
	st = [[1,2,3,4,5],[2,1,2,3,2],[3,3,1,1,2]]
	for i in range(3):
		for j in range(5):
			if st[i][j] == answers[j]:
				cnt += 1
		answer.append(cnt)
		cnt = 0	
	M = max(answer)
	
	

solution(answers)

