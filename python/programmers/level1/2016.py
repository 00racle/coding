a = int(input("월입력: "))
b = int(input("일입력: "))

def solution(a, b):
	month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
	'''
	a = sum(month[:a])+b
	b = a%7
	return week[b]
	'''
	return week[(sum(month[:a])+b)%7]


print(solution(a, b))
