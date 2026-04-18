def avoid_duplicate(lst):
    return list(dict.fromkeys(lst))

charList =  ["a", "b", "a", "c", "c"]

print("duplicate remove of characters::",avoid_duplicate(charList));

numList = [1,5,7,1,2,7,3,9,2]
print("duplicate remove of numbers::",avoid_duplicate(numList))

strList = ["Suresh","Alekhya","Sathish","Mahesh","Suresh","Alekhya"]

print("duplicate remove of Strings::", avoid_duplicate(strList))

