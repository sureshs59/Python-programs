print("########### ARMStrong Program #########")
n = 153
actual = 153
arms=0
while n>0 :
    i = int(n%10)
    arms = arms + (i * i * i)
    n = int(n/10)
if actual == arms :
    print("Armstrong number is ", arms)
else :
    print("Not a armstrong number", arms)


print("########### Strong Program #########")
Strong = 145
x   = 145
tot = 1
ss = 0
while x>0 :
    f = int(x % 10)
    tot  = 1

    while f>0 :
        tot = int(tot * f)
        f = int(f-1)
    ss = int(ss + tot)
    x = int(x/10)

if ss == Strong :
    print (ss, " is a STRONG NUMBER ")
else :
    print ("Not a Strong number",ss)

