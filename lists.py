j = 1
k = 5
while j <= 5 and k >=1:
    #print(j * '*', ' ', k * '+')
    print(j * '*',  j * ' ', k * '*')
    j += 1
    k -= 1

list = [10,20,40,35,22]

print(list[2:8])

list.insert(-1, 55)
for i in list :
    print(i)
# number exist in the list or not ,verifying
print(19 in list, "====",40 in list)

# RANGE
numbers = range(10,15, 8)
for i2 in numbers :
    print(i2)


    # another way with while
# kk = len(list)
#
# while kk > 0 :
#     print(list[kk-1])
#     kk -= 1


print("Sort the list ")