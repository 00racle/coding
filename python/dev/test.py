<<<<<<< HEAD
def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

x = {'name': '홍길동', 'age': 30, 'address' : '서울시 용산구 이촌동'}

personal_info(**x)
=======
import math

class Point2D:
	def __init__(self, x, y):
		self.x = x
		self.y = y

length = 0.0

p = [Point2D(), Point2D(), Point2D(), Point2D()]

p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())
>>>>>>> 577b642234dec9fda8c71fd904a9e8ba3f6dc119
