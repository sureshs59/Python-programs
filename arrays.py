

# ---------ARRAYS-----------------------------

cars = ["Ford", "Volvo", "BMW"]

i=0
length = len(cars)
print("Cars array length..", length)
while length > 0 :
	print("Car ARRAys displaying using with While loop------->>",cars[i])
	i = i+1
	length = length - 1
	
cars.append("TATA")	
	
for x in cars :
	print("Car ARRAYs displaying using with For loop after Adds an element at the end of the list------->>",x)
	
cars.pop(2)
for x in cars :
	print("Car ARRAYs displaying using with For loop after Removes the element at the specified position------->>",x)	

cars.insert(1,"Maruti")
cars.insert(3,"Nissan")	

for x in cars :
	print("Car ARRAYs displaying using with Adds an element at the specified position------->>",x)
	
cars.sort()	
for x in cars :
	print("Car ARRAYs displaying using with For loop  ===SORT====------->>",x)

cars.reverse()
for x in cars :
	print("Car ARRAYs displaying using with For loop ==REVERSE===------->>",x)		
	
	
	