print("########LAMBDA single parameter############")

x = lambda a: a+10

print(x(5))

print("########LAMBDA multiple parameters 2############")
multiply = lambda a , b : b * a

print(multiply(9,8))

print("########LAMBDA multiple parameters 3############")

factorial = lambda f1, f2, f3 : f1 * f2 * f3

print(factorial(5, 15, 20))



def myfunc(n):
	return lambda a : a *n
	
str = myfunc(1000)

print("String..", str(55))

