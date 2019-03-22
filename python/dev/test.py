import math

class Point2D:
	def __init__(self, x, y):
		self.x = x
		self.y = y

length = 0.0

p = [Point2D(), Point2D(), Point2D(), Point2D()]

p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())
