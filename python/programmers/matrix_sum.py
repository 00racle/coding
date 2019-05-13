arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

#arr1 = [[1],[2]]
#arr2 = [[3],[4]]

#arr1 = [[1,2,3],[4,5,6],[7,8,9]]
#arr2 = [[1,2,3],[4,5,6],[7,8,9]]
'''
def solution(arr1, arr2):
	m = []
	for i in range(len(arr1)):
		t = []
		for j in range(len(arr1[0])):
			t.append(arr1[i][j]+arr2[i][j])
		m.append(t)


	print(m)
'''

#================== 다른사람 풀이 ==================

def solution(arr1, arr2):
	answer = [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]
	print(answer)


solution(arr1, arr2)
