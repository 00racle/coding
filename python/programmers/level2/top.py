heights = [6, 9, 5, 7, 4]
         #[0, 1, 2, 3, 4]

def solution(heights):
	answer = []
	l = len(heights)
	print(heights)
	for i in reversed(range(l)):
		for j in reversed(range(i)):
			if heights[i]<heights[j]:
				print("i: %d(%d), j: %d(%d) \n"%(heights[i], i, heights[j], j))
				answer.append(j+1)
				break
			else:
				answer.append(0)
	return answer

print(solution(heights))
