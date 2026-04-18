
print("------------ ARMSTRONG NUMBER 1* + 5*5*5 + 3*3*3 ---------------")
original = 153
n=153
sum = 0

while n>0:
	i = int(n % 10)
	print("I--->",i)
	sum = int(sum + (i * i * i))
	print("sum...",sum)
	n = int(n /10)
	print("n-->",n)
	
if sum == original:
	print("its a ARMSTRONG Number...", sum)
else :
	print("Not a ARMSTRONG number...", sum)
	
	
print("------------ STRONG NUMBER 1* + 4*3*2*1 + 5*4*3*2*1 ---------------")
	
str = 145
num = 145
sumStrong = 0


def factorial(a):
	z=1
	while a > 0:
		z = int(z * a)
		a = int(a-1)
	print("factorial value...",z)	
	return z


while num > 0:
	x = int(num % 10)
	sumStrong = int(sumStrong + factorial(x))
	print("sumStrong...",sumStrong)
	num = int(num/10)
	print("num-->",num)
	

if sumStrong == str:
	print("Strong number...", sumStrong)
else :
	print("Not a Strong number...", sumStrong)
	
print("###########END#############")	