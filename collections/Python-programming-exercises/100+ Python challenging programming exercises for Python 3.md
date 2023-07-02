# 100+ Python challenging programming exercises for Python 3
----

### Question 51
Define a class named American and its subclass NewYorker. 

Hints:

Use class Subclass(ParentClass) to define a subclass.

Solution:
```python
class American(object):
    pass

class NewYorker(American):
    pass

anAmerican = American()
aNewYorker = NewYorker()
print(anAmerican)
print(aNewYorker)
```

### Question 52
Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area. 

Hints:

Use def methodName(self) to define a method.

Solution:
```python
class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14

aCircle = Circle(2)
print aCircle.area()
```

### Question 53
Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 

Hints:

Use def methodName(self) to define a method.

Solution:
```python
class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

aRectangle = Rectangle(2,10)
print(aRectangle.area())
```

### Question 54
Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

Hints:

To override a method in super class, we can define a method with the same name in the super class.

Solution:
```python
class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length*self.length

aSquare= Square(3)
print(aSquare.area())
```

### Question 55
Please raise a RuntimeError exception.

Hints:

Use raise() to raise an exception.

Solution:

```python
raise RuntimeError('something wrong')
```

### Question 56
Write a function to compute 5/0 and use try/except to catch the exceptions.

Hints:

Use try/except to catch exceptions.

Solution:
```python
def throws():
    return 5/0

try:
    throws()
except ZeroDivisionError:
    print("division by zero!")
except Exception, err:
    print('Caught an exception')
finally:
    print('In finally block for cleanup')
```

### Question 57
Define a custom exception class which takes a string message as attribute.

Hints:

To define a custom exception, we need to define a class inherited from Exception.

Solution:
```python
class MyError(Exception):
    """My own exception class

    Attributes:
        msg  -- explanation of the error
    """
    
    def __init__(self, msg):
        self.msg = msg

error = MyError("something wrong")
```

### Question 58
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

john

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

Use \w to match letters.

Solution:
```python
import re
emailAddress = raw_input()
pat2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(pat2,emailAddress)
print(r2.group(1))
```

### Question 59
Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

Example:
If the following email address is given as input to the program:

john@google.com

Then, the output of the program should be:

google

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

Use \w to match letters.

Solution:
```python
import re
emailAddress = raw_input()
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2,emailAddress)
print(r2.group(2))
```

### Question 60
Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

Example:
If the following words is given as input to the program:

2 cats and 3 dogs.

Then, the output of the program should be:

['2', '3']

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:

Use re.findall() to find all substring using regex.

Solution:
```python
import re
s = raw_input()
print(re.findall("\d+",s))
```

### Question 61
Print a unicode string "hello world".

Hints:

Use u'strings' format to define unicode string.

Solution:
```python
unicodeString = u"hello world!"
print(unicodeString)
```

### Question 62
Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

Hints:

Use unicode() function to convert.

Solution:
```python
s = input()
u = unicode( s ,"utf-8")
print(u)
```

### Question 63

Write a special comment to indicate a Python source code file is in unicode.

Hints:

Solution:
```python

# -*- coding: utf-8 -*-

#----------------------------------------#
```

### Question 64

Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

3.55

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:
Use float() to convert an integer to a float

Solution:
```python
n=int(input())
sum=0.0
for i in range(1,n+1):
    sum += float(float(i)/(i+1))
print(sum)
```

### Question 65

Write a program to compute:

f(n)=f(n-1)+100 when n>0
and f(0)=1

with a given n input by console (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

500

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:
We can define recursive function in Python.

Solution:
```python
def f(n):
    if n==0:
        return 0
    else:
        return f(n-1)+100

n=int(input())
print(f(n))
```

### Question 66
The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program to compute the value of f(n) with a given n input by console.

Example:
If the following n is given as input to the program:

7

Then, the output of the program should be:

13

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:
We can define recursive function in Python.


Solution:
```python
def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
print(f(n))
```

### Question 67
The Fibonacci Sequence is computed based on the following formula:

f(n)=0 if n=0
f(n)=1 if n=1
f(n)=f(n-1)+f(n-2) if n>1

Please write a program using list comprehension to print the Fibonacci Sequence in comma separated form with a given n input by console.

Example:
If the following n is given as input to the program:

7

Then, the output of the program should be:

0,1,1,2,3,5,8,13


Hints:
We can define recursive function in Python.
Use list comprehension to generate a list from an existing list.
Use string.join() to join a list of strings.

In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
```python
def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
values = [str(f(x)) for x in range(0, n+1)]
print(",".join(values))
```

### Question 68

Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

10

Then, the output of the program should be:

0,2,4,6,8,10

Hints:
Use yield to produce the next value in generator.

In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
```python
def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1


n=int(input())
values = []
for i in EvenGenerator(n):
    values.append(str(i))

print(",".join(values))
```

### Question 69
Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

Example:
If the following n is given as input to the program:

100

Then, the output of the program should be:

0,35,70

Hints:
Use yield to produce the next value in generator.

In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
```python
def NumGenerator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i

n=int(input())
values = []
for i in NumGenerator(n):
    values.append(str(i))

print(",".join(values))
```

### Question 70
Please write assert statements to verify that every number in the list [2,4,6,8] is even.

Hints:
Use "assert expression" to make assertion.

Solution:
```python
li = [2,4,6,8]
for i in li:
    assert i%2==0
```

### Question 71
Please write a program which accepts basic mathematic expression from console and print the evaluation result.

Example:
If the following string is given as input to the program:

35+3

Then, the output of the program should be:

38

Hints:
Use eval() to evaluate an expression.


Solution:
```python
expression = raw_input()
print(eval(expression))
```

### Question 72
Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

Hints:
Use if/elif to deal with conditions.

Solution:
```python
import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print(bin_search(li,11))
print(bin_search(li,12))
```

### Question 73
Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

Hints:
Use if/elif to deal with conditions.

Solution:
```python
import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print(bin_search(li,11))
print(bin_search(li,12))
```

### Question 74
Please generate a random float where the value is between 10 and 100 using Python math module.

Hints:
Use random.random() to generate a random float in [0,1].

Solution:
```python
import random
print(random.random()*100)
```

### Question 75
Please generate a random float where the value is between 5 and 95 using Python math module.

Hints:
Use random.random() to generate a random float in [0,1].

Solution:
```python
import random
print(random.random()*100-5)
```

### Question 76
Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

Hints:
Use random.choice() to a random element from a list.

Solution:
```python
import random
print(random.choice([i for i in range(11) if i%2==0]))
```

### Question 77
Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.

Hints:
Use random.choice() to a random element from a list.

Solution:
```python
import random
print(random.choice([i for i in range(201) if i%5==0 and i%7==0]))
```

### Question 78
Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

Hints:
Use random.sample() to generate a list of random values.

Solution:
```python
import random
print(random.sample(range(100), 5))
```

### Question 79
Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

Hints:
Use random.sample() to generate a list of random values.

Solution:
```python
import random
print(random.sample([i for i in range(100,201) if i%2==0], 5))
```

### Question 80
Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

Hints:
Use random.sample() to generate a list of random values.

Solution:
```python
import random
print(random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 5))
```

### Question 81
Please write a program to randomly print a integer number between 7 and 15 inclusive.

Hints:
Use random.randrange() to a random integer in a given range.

Solution:
```python
import random
print(random.randrange(7,16))
```

### Question 82
Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

Hints:
Use zlib.compress() and zlib.decompress() to compress and decompress a string.

Solution:
```python
import zlib
s = b'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print(t)
print(zlib.decompress(t))
```

### Question 83
Please write a program to print the running time of execution of "1+1" for 100 times.

Hints:
Use timeit() function to measure the running time.

Solution:
```python
from timeit import Timer
t = Timer("for i in range(100):1+1")
print(t.timeit())
```

### Question 84
Please write a program to shuffle and print the list [3,6,7,8].

Hints:
Use shuffle() function to shuffle a list.

Solution:
```python
from random import shuffle
li = [3,6,7,8]
shuffle(li)
print(li)
```

### Question 85
Please write a program to shuffle and print the list [3,6,7,8].

Hints:
Use shuffle() function to shuffle a list.

Solution:
```python
from random import shuffle
li = [3,6,7,8]
shuffle(li)
print(li)
```

### Question 86
Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

Hints:
Use list[index] notation to get a element from a list.

Solution:
```python
subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
for i in range(len(subjects)):
    for j in range(len(verbs)):
        for k in range(len(objects)):
            sentence = "%s %s %s." % (subjects[i], verbs[j], objects[k])
            print(sentence)
```

### Question 87
Please write a program to print the list after removing delete even numbers in [5,6,77,45,22,12,24].

Hints:
Use list comprehension to delete a bunch of element from a list.

Solution:
```
li = [5,6,77,45,22,12,24]
li = [x for x in li if x%2!=0]
print(li)
```

### Question 88
By using list comprehension, please write a program to print the list after removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.

Solution:
```
li = [12,24,35,70,88,120,155]
li = [x for x in li if x%5!=0 and x%7!=0]
print(li)
```

### Question 89
By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.

Solution:
```python
li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i%2!=0]
print(li)
```

### Question 90
By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

Hints:
Use list comprehension to make an array.

Solution:
```
array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)
```

### Question 91
By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].

Hints:
Use list comprehension to delete a bunch of element from a list.
Use enumerate() to get (index, value) tuple.

Solution:
```python
li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
print(li)
```

### Question 92
By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

Hints:
Use list's remove method to delete a value.

Solution:
```python
li = [12,24,35,24,88,120,155]
li = [x for x in li if x!=24]
print(li)
```

### Question 93
With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

Hints:
Use set() and "&=" to do set intersection operation.

Solution:
```python
set1=set([1,3,6,78,35,55])
set2=set([12,24,35,24,88,120,155])
set1 &= set2
li=list(set1)
print(li)
```

### Question 94
With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

Hints:
Use set() to store a number of values without duplicate.

Solution:
```python
def removeDuplicate( li ):
    newli=[]
    seen = set()
    for item in li:
        if item not in seen:
            seen.add( item )
            newli.append(item)

    return newli

li=[12,24,35,24,88,120,155,88,120,155]
print(removeDuplicate(li))
```

### Question 95
Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

Hints:
Use Subclass(Parentclass) to define a child class.

Solution:
```python
class Person(object):
    def getGender( self ):
        return "Unknown"

class Male( Person ):
    def getGender( self ):
        return "Male"

class Female( Person ):
    def getGender( self ):
        return "Female"

aMale = Male()
aFemale= Female()
print(aMale.getGender())
print(aFemale.getGender())
```

### Question 96
Please write a program which count and print the numbers of each character in a string input by console.

Example:
If the following string is given as input to the program:

abcdefgabc

Then, the output of the program should be:

a,2
c,2
b,2
e,1
d,1
g,1
f,1

Hints:
Use dict to store key/value pairs.
Use dict.get() method to lookup a key with default value.

Solution:
```python
dic = {}
s=raw_input()
for s in s:
    dic[s] = dic.get(s,0)+1
print('\n'.join(['%s,%s' % (k, v) for k, v in dic.items()]))
```

### Question 97
Please write a program which accepts a string from console and print it in reverse order.

Example:
If the following string is given as input to the program:

rise to vote sir

Then, the output of the program should be:

ris etov ot esir

Hints:
Use list[::-1] to iterate a list in a reverse order.

Solution:
```python
s=raw_input()
s = s[::-1]
print(s)
```

### Question 98
Please write a program which accepts a string from console and print the characters that have even indexes.

Example:
If the following string is given as input to the program:

H1e2l3l4o5w6o7r8l9d

Then, the output of the program should be:

Helloworld

Hints:
Use list[::2] to iterate a list by step 2.

Solution:
```python
s=raw_input()
s = s[::2]
print(s)
```

### Question 99
Please write a program which prints all permutations of [1,2,3]

Hints:
Use itertools.permutations() to get permutations of list.

Solution:
```python
import itertools
print(list(itertools.permutations([1,2,3])))
```

### Question 100
Write a program to solve a classic ancient Chinese puzzle: 
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

Hint:
Use for loop to iterate all possible solutions.

Solution:
```python
def solve(numheads,numlegs):
    ns='No solutions!'
    for i in range(numheads+1):
        j=numheads-i
        if 2*i+4*j==numlegs:
            return i,j
    return ns,ns

numheads=35
numlegs=94
solutions=solve(numheads,numlegs)
print(solutions)
```

