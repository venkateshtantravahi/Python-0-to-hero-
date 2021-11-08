"""
map reduce and filter functions belong to functional programming part of python, that means computing here is done by
imperative programming. In functional programming there are two kinds of functions 
-> usual function : that define a body or set of statements to perform some task.
-> higher-order function : take function as a param and return function as result.
Reduce(), map(), and filter() are three of Python’s most useful higher-order functions. 
They can be used to do complex operations when paired with simpler functions.
"""

# Higher order functions
def greet(name):
    return "Hello, {}!".format(name)

def print_greeting(f, n):
    print(f(n))

# 1. map() function 
"""
The map() function is a higher-order function. As previously stated, this function accepts
another function and a sequence of ‘iterables’ as parameters and provides output 
after applying the function to each iterable in the sequence. It has the following syntax:

SYNTAX: map(function, iterables)
"""
# example1
def function(a: int) -> int:
    return a*a
x= map(function, (1,2,3,4))
print(set(x)) # here x is the map object returned

# example2
tup= (5, 7, 22, 97, 54, 62, 77, 23, 73, 61)
newtuple = tuple(map(lambda x: x+3 , tup)) 
print(newtuple)

# example3
def multiply(x: int) -> int:
    return (x*x)
def add(x: int) -> int:
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)

# 2. filter() 
"""
The filter() function is used to generate an output list of values that return true 
when the function is called. It has the following syntax:

SYNTAX: filter (function, iterables)
"""
#example1
def func(x: int) -> int:
    if x >= 3:
        return x
y = filter(func, (3,4,1,2,10))
print(list(y))

#example2
y = filter(lambda x: (x>=3), (1,2,3,4))
print(list(y))

#example3
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# 3. reduce()
"""
Reduce is a really useful function for performing some computation on a list and 
returning the result. It applies a rolling computation to sequential pairs of values in a list.
It has the following syntax:

SYNTAX: reduce(function, iterables)
"""

#example1
from functools import reduce
red = reduce(lambda x,y : x + y, [23,49,44,97])

#example2
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])