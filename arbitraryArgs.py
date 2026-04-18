# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:

def arbitrary( *args ):
	print("Passed values..",args[0] ,"--",args[1],"---", args[2])
	if( args[0]> args[1]):
		print(args[0]," A is greater than B ",args[1])
	elif(args[1] > args[2]):
		print(args[1]," B is greater than C ", args[2])
	else :
		print(args[2], " C is greater than A ",args[0])

arbitrary( 15 , 19 , 12)
