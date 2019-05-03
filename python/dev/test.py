a = [[1,2],[3,4]]
b = [[4,3],[2,1]]

def solution(a, b):
	p = []
	for i in range(2):
		m = []
		for j in range(2):
			m.append(a[i][j] + b[i][j])
		p.append(m)


	print(p)

solution(a, b)
