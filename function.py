
def multiply( x , y) :
	z = x * y
	return z

c = multiply(60,2)
print("function calling...", c)

print("############function call with parameters pass values:######################")


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

print("############function call with direct string values to pass:######################")


def my_function(food):
  #for x in food:
    #print("Using For loop ..".x)
	
  i = 1
  while food !=null :
	print("using while ..",food[i])
	i=i+1

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
