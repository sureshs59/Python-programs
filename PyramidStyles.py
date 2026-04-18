
# Fully Pyramid
print("Fully Pyramid")
n=5
for i in range(1, n+1):
  print(" "*(n-i)+"* "*i)

# Right Angle Triangle
print("Right Angle Triangle")
n=6
for i in range(1, n+1):
  print("* "*i)

# Inverted Right Triangle
print("Inverted Right Triangle")
n=5
for i in range(n,0,-1):
  print(i,"* "*i)

# DIAMOND PATTERN
print("DIAMOND PATTERN")
n=5
for i in range(1, n+1):
  print(" "*(n-i)+"* "*i)
for i in range(n-1,0,-1):
  print(" "*(n-i)+"* "*i)  

# HOLLOW SQUARE
print("HOLLOW SQUARE")
n=5
for i in range(n):
  for j in range(n):
    if i == 0 or i == n-1 or j ==0 or j == n-1:
      print("*",end=" ")
    else:
      print(" ",end=" ")
  print()

#SQUARE PATTERN
print("SQUARE PATTERN")
n=5
for i in range(n):
  for j in range(n):
    print("*", end=" ") 
  print("")  

#NUMBER TRIANGLE
print("NUMBER TRIANGLE")
n=8
for i in range(1, n+1):
  for j in range(1, i+1):
    print(i, end=" ")
  print()         

#FLOYD"S TRIANLGE
print("FLOYD'S TRIANLGE")
n =5
num =1 
for i in range(1, n+1):
    for j in range(i):
        print(num, end=" ")
        num +=1
    print()

#INVERTED PYRAMID
print("INVERTED PYRAMID")
n=5
for i in range(n,0,-1):
    print(" "* (n-1)+"* " *i)

#SAME NUMBER TRIANGLE
print("SAME NUMBER TRIANGLE")
n = 5
for i in range(1, n+1):
    print((str(i) + " ") *i)        

#BINARY PATTERN
print("BINARY PATTERN")
n =6
for i in range(n):
    for j in range(i+1):
        print((i + j)%2, end=" ")
    print()

#REVERSE NUMBER TRIANGLE
print("REVERSE NUMBER TRIANGLE")
n = 5
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end="")
    print()        