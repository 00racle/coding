#skill = "CBD"
skill = "DA"
#skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
skill_trees = ["ABCDE", "UCBADF", "ACEB", "BDA"]

# "BCD", "CBD", "CB", "BD"

def solution(skill, skill_trees):
	answer = 0
	for i in skill_trees:
		s = list(skill)
		for j in i:
			if j not in s:
				pass
			elif j in s and j == s[0]:
				s.remove(j)
			else:
				break
			if j == i[-1]:
				answer += 1
			
	return answer

print(solution(skill, skill_trees))
