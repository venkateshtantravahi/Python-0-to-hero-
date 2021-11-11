"""
Python has a built-in module that you can use to make random numbers.
To get the list of methods that are derived from random module all you need to do is open python 
interpretor and type the following :
>>> import random
>>> random.__dir__()
want more help on random , again open python interpretor 
>>> help()
help> random
"""

import random 

# seed()
"""
The seed is used to initialize the random number generator. It acts as a start for number generator
when we use it for first time.
If we don't use this initializer the default initializer would be clocks time seconds. 
Repeated usage of seed function results in the same generation .
SYNTAX : random.seed(a, version)
where a = is optional , the seed value to generate the random value 
version = an int specifying how to convert a to int , default is 2.
"""
random.seed(10)
print(random.random())

# sample 
"""
This method used for generating sample items from a list or range of items, without changing 
original sequence
SYNTAX : random.sample(sequence, k)
where sequence = list,set, range etc.
k = the sample size
"""

print(random.sample(range(99),k=2)) 
print(random.sample(range(20),k=18))

# getstate() and setstate()
"""
Python's default generator is a Mersenne Twister with a state space that is 19937 bits, 
much larger than what you think of as the seed.

You can think of it conceptually as three functions:

f(seed) -> state0
g(statei) -> statei+1
h(statei) -> outcomei
When you start with a seed value using random.seed(), 
it generates a full state value of 19937 bits one time using function f(). 
Each time you use the generator, it advances to the next 19937 bit state using g() 
and returns the output found by collapsing the updated state down a single integer using h().

Normally you don't actually see the internal state which is at the core of the generator. 
getstate() bypasses the collapsing function h(), 
and setstate() bypasses the seeding function f(), 
so that you can reproduce your sequence from any point without having to go 
all the way back to the beginning and reproduce the entire sequence to that point.
"""
random.seed(42)

print(random.sample(range(20),k=10))

st = random.getstate()  # remeber this state 

print(random.sample(range(20),k=20)) # print 20

random.setstate(st)     # restore state

print(random.sample(range(20),k=10)) #print same first 10

# getrandbits()
"""
The getrandbits() method returns an integer in the specified size (in bits).
SYNTAX : random.getrandbits(n)
where n is length of bits you want 
"""
print(random.getrandbits(8))

# randrange()
"""
The randrange() method returns a randomly selected element from the specified range.
SYNTAX : random.randrange(start, stop, step)
here start is optional if not given default will be 0.
end is required .
step is optional and default = 1.
"""
print(random.randrange(3,10))
print(random.randrange(10,100,5))

# randint()
"""
The randint() method returns an integer number selected element from the specified range.
SYNTAX : random.randint(start, stop)
"""
print(random.randint(5,20))

# choice()
"""
The choice() method returns a randomly selected element from the specified sequence.

The sequence can be a string, a range, a list, a tuple or any other kind of sequence.

SYNTAX : random.choice(sequence)
"""
mylist = ["apple", "banana", "cherry"]
print(random.choice(mylist))

x = "WELCOME"
print(random.choice(x))

# choices
"""
The choices() method returns a list with the randomly selected element from the 
specified sequence.
You can weigh the possibility of each result with the weights parameter or the 
cum_weights parameter.
The sequence can be a string, a range, a list, a tuple or any other kind of sequence.
SYNTAX  : random.choices(sequence, weights=None, cum_weights=None, k=1)
where
A sequence like a list, a tuple, a range of numbers etc.
A list were you can weigh the possibility for each value.
Default None
A list were you can weigh the possibility for each value, 
only this time the possibility is accumulated.
An integer defining the length of the returned list
"""
mychoices = ["python", 'c++','Sql']
print(random.choices(mylist, weights = [10, 5, 4], k = 14))

# shuffle()
"""
The shuffle() method takes a sequence, like a list, and reorganize the order of the items.
SYNTAX : random.shuffle(sequence, function)
where 
function =  name of a function that returns a number between 0.0 and 1.0.
If not specified, the function random() will be used
"""
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist)