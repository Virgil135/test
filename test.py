def func(x,y):
	z = x+y
	return z

a = func(5,10)
print(a)

def func(a,m):
	z= a * m
	return z
n = func(a,3)
print(n)


x = lambda a,m : a*m
print(x(a,3))