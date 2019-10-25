a = 10
b = 8

def gcd(a, b):
	while(b>0):
		temp = b
		b = a%b
		a = temp
	return a

print(gcd(a, b))
