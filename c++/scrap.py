# Python code to demonstrate
# call by value


def test(x):
	x+=10
	print("Inside Function:",x)
x=5
test(x)
print("Outside Function:",x)

