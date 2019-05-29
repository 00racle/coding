arr = [1,1,3,3,0,1,1]
#arr = [4,4,4,3,3]
#arr = [0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3]

def solution(arr):
    answer = []
    temp = 10
    for i in arr:
        if i != temp:
            temp = i
            answer.append(i)
    return answer

print(solution(arr))

'''
# 다른사람 코드
# 1.
def solution(arr):
	answer = []
	for i in arr:
		if answer[-1:] == [i]: continue
		answer.append(i)
	return answer

# 3.
def solution(arr):
	return [arr[i] for i in range(len(arr)) if s[i] != arr[i+1:i+2]]

print(solution(arr))
