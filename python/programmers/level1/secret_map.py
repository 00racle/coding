n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
'''
def solution(n, arr1, arr2):
	ret = []
	arr1 = [bin(i)[2:].rjust(n, '0') for i in arr1]
	arr2 = [bin(i)[2:].rjust(n, '0') for i in arr2]

	for i in range(n):
		sum = ''
		for j in range(n):
			if arr1[i][j] == '0' and arr2[i][j] == '0':
				sum += ' '
			else:
				sum += '#'
		ret.append(sum)


	return ret
'''
#다른 사람 코드

def solution(n, arr1, arr2):
	answer = []
	for i,j in zip(arr1, arr2):
		a12 = str(bin(i|j)[2:])
		print(a12)
		a12 = a12.rjust(n, '0')
		a12 = a12.replace('1', '#')
		a12 = a12.replace('0', ' ')
		answer.append(a12)
	return answer

print(solution(n, arr1, arr2))
