import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('X', type=int, help="what is the first number?")
	parser.add_argument('Y', type=int, help="what is the second number?")

	args = parser.parse_args()
	X = args.X
	Y = args.Y
	print("%d + %d = %d"%(X, Y, X+Y))

if __name__=="__main__":
	main()
