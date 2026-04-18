# Python Programs for Practice

<!-- Feature Image -->
| ![space-1.jpg](https://dyclassroom.com/image/topic/python/logo.png) | 
|:--:| 
| Image Credits [DY Classroom](https://dyclassroom.com/python/python-introduction) |

<!-- Content-->

## 1. Converting an Integer into Decimals

```python
import decimal
integer = 10
print(decimal.Decimal(integer))
print(type(decimal.Decimal(integer)))

> 10
> <class 'decimal.Decimal'>

```

---

## 2. Converting an String of Integers into Decimals

```python
import decimal
string = '12345'
print(decimal.Decimal(string))
print(type(decimal.Decimal(string)))

> 12345
> <class 'decimal.Decimal'>

---

## 3. Reversing a String using an Extended Slicing Technique

```python
string = "Python Programming"
print(string[::-1])

> gnimmargorP nohtyP

```


## 4. Counting Vowels in a Given Word

```python
vowel = ['a', 'e', 'i', 'o', 'u']
word = "programming"
count = 0
for character in word:
    if character in vowel:
        count += 1
print(count)

> 3
```

## 5. Counting Consonants in a Given Word

```python
vowel = ['a', 'e', 'i', 'o', 'u']
word = "programming"
count = 0
for character in word:
    if character not in vowel:
        count += 1
print(count)

> 8
```


## 6. Counting the Number of Occurances of a Character in a String

```python
word = "python"
character = "p"
count = 0
for letter in word:
    if letter == character:
        count += 1
print(count)

> 1

---

## 7. Writing Fibonacci Series

```python
fib = [0,1]
# Range starts from 0 by default
for i in range(5):  
    fib.append(fib[-1] + fib[-2]) 

# Converting the list of integers to string
print(', '.join(str(e) for e in fib))

> 0, 1, 1, 2, 3, 5, 8

```

## 8. Finding the Maximum Number in a List

```python
numberList = [15, 85, 35, 89, 125]

maxNum = numberList[0]
for num in numberList:
    if maxNum < num:
        maxNum = num
print(maxNum)

> 125

```

## 9. Finding the Minimum Number in a List

```python
numberList = [15, 85, 35, 89, 125, 2]

minNum = numberList[0]
for num in numberList:
    if minNum > num:
        minNum = num
print(minNum)

> 2

```


## 10. Finding the Middle Element in a List

```python
numList = [1, 2, 3, 4, 5]
midElement = int((len(numList)/2)) 

print(numList[midElement])

> 3
```


## 11. Converting a List into a String

```python
lst = ["P", "Y", "T", "H", "O", "N"]
string = ''.join(lst)

print(string)
print(type(string))

> PYTHON
> <class 'str'>
```


## 12. Adding Two List Elements Together

```python
lst1 = [1, 2, 3]
lst2 = [4, 5, 6] 

res_lst = [] 
for i in range(0, len(lst1)):
    res_lst.append(lst1[i] + lst2[i]) 
print(res_lst)

> [5, 7, 9]

```

## 13. Comparing Two Strings for Anagrams

```python
str1 = "Listen"
str2 = "Silent"

str1 = list(str1.upper())
str2 = list(str2.upper())
str1.sort(), str2.sort()

if(str1 == str2):
    print("True")
else:
    print("False")

> True

```

## 14. Checking for Palindrome Using Extended Slicing Technique

```python
str1 = "Kayak".lower()
str2 = "kayak".lower()

if(str1 == str2[::-1]):
    print("True")
else:
    print("False")
    
> True

```

## 15. Counting the White Spaces in a String

```python
string = "P r ogramm in g "
print(string.count(' '))
    
> 5
```

## 16. Counting Digits, Letters, and Spaces in a String

```python
# Importing Regular Expressions Library
import re

name = 'Python is 1'

digitCount = re.sub("[^0-9]", "", name)
letterCount = re.sub("[^a-zA-Z]", "", name)
spaceCount = re.findall("[ \n]", name)

print(len(digitCount))
print(len(letterCount))
print(len(spaceCount))
    
> 1
> 8
> 2
```

## 17. Counting Special Characters in a String

```python
# Importing Regular Expressions Library
import re
spChar = "!@#$%^&*()"

count = re.sub('[\w]+', '', spChar)
print(len(count))
    
> 10
```


## 18. Removing All Whitespace in a String

```python
import re

string = "C O D E"
spaces = re.compile(r'\s+')
result = re.sub(spaces, '', string)
print(result)

> CODE

```


## 19. Building a Pyramid in Python

```python
floors = 3
h = 2*floors-1
for i in range(1, 2*floors, 2):
    print('{:^{}}'.format('*'*i, h))

>  *  
  *** 
 *****

```

## 20. Randomizing the Items of a List in Python

```python

from random import shuffle

lst = ['Python', 'is', 'Easy']
shuffle(lst)
print(lst)

> ['Easy', 'is', 'Python']


```


<br>
<br>

























