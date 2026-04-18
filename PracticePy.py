
print("Hello Python..");

num =100.001;
s21 = "Sathish";
boolFlag = True;
charValue = 'c';

print(num,"-->",s21,"\"===>",boolFlag,"--->",charValue);

if s21.__eq__("suresh"):
    print("It is a string..",s21)
elif( s21 == "Sathish"):
    print("true string equal....")
else:
    print("Not an string..",s21)
    print("Continuation of else part1..")
    print("Continuation of else part2..")


n=10;

for item in range(1,10):
    print("item..",item)        

while(n>0):
    print("while N--",n);
    n=n-1;    

list = ['suresh','Alekhya','sathis',124,True, 534.23232,'c','p','suresh']

Len = len(list);

for i in list:
    print(Len,"--List length..",i)

print("What is the data type of a list?---use type(list)------",type(list));

print(list[2]);

print("-1 refers to the last item, -2 refers to the second last item etc.");

print(list[-3]);

print(list[2:5]);

print(list[:2]); 

nums = [1, 2, 3, 4, 5, 6]
squares = [x**x for x in nums]
print (squares)

def add(a, b):
    return a + b

print(add(20, 30))
