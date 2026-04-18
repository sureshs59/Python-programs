# If else condition

def arbitrary( a, b, c ):
	print("Passed values..",a ,"--",b,"---",c)
	
	
	if( a> b):
		print(a," A is greater than B ",b)
	elif(b > c):
		print(b, " B is greater than C ", c)
	else :
		print( c," C is greater than A ",a)

arbitrary( 15 , 19 , 20)


print("############One line if else statement:#########################")

a =505
b = 509

print("A") if a>b else print("B")

print("############not:######################")

if not a > b:
  print("a is NOT greater than b")


print("############One line if else statement, with 3 conditions:######################")

print("A") if a>b else print("EQUAL") if a == b else print("B")



x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
	
print("############PASS:######################")	
print("The pass Statement")
if not a > b:
  pass
  
