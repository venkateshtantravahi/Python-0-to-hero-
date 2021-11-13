"""
Function is a block or chunk of code which is used for fulfilling a particular task 

Functions are three types:
Built-in functions
User-defined functions
Anonymous Functions

every function is declared or defined using a keyword called "def"
"""
from functools import reduce

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
# define a function plus()
def plus(a, b):  # a,b are parameters
    sum = a + b
    return sum


# Create a sum method
class Summation(object):
    def sum(self, a, b):
        self.contents = a + b
        return self.contents


sum = plus(num1, num2)  # num1, num2 are arguments

sumInstance = Summation()
add = sumInstance.sum(num1, num2)

print("Function Call: ", sum)
print("Method call: ", add)


def hello():
    name = str(input("Enter your name: "))
    if name:
        pr = "Hello " + str(name)
    else:
        pr = "Hello world!"
    return pr


def hello_noreturn():
    print("Hello World!")


ret = hello()
print(ret * 5)

# hello_noreturn()*5 "we can't perform any further operations outside our function as we are not returning anything"


def run():
    for i in range(10):
        if i == 2:
            return
    print("Run!")


run()


def mul(
    a, b
):  # required aurguments --> arguments to be passed to function for function call
    mul = a * b
    return (a, b, mul)


a, b, m = mul(num1, num2)
print(a, b, m)
print(a * 5)


def hello1():
    """Prints "Hello World"

    Returns:
        None    
    """
    print("Hello World")
    return


hello1()

# function for modulus
def mod(
    a, b=2
):  # default arguments --> aurgumnts may or may not passed to function for execution
    return a % b


t = mod(a=4)
g = mod(a=1, b=3)
print(t, g)


def minimum(*args):
    return min(args)


d = minimum(4, 5, 6, 7, 45, 3, 6, 34, 56, 43)
print(d)

name = "venkat"


def multiplication(*args):
    total = 1
    for i in args:
        total *= i
    return total


y = multiplication(1, 2, 34, 56, 4, 3, 5, 67, 5, 4, 3)
print(y)

print("Printing global variable: ", name)

double = lambda x: x * 2
print(double(5))

adding = lambda x, y: x + y
print(adding(12, 13))

my_list = list(range(1, 11))
print(my_list)

filtered_list = list(filter(lambda x: (x * 2 > 10), my_list))
print(filtered_list)

mapped_list = list(map(lambda x: x * 2, my_list))
print(mapped_list)

reduced_list = reduce(lambda x, y: x + y, my_list)
print(reduced_list)

# function to get the most repetitive word from a string 
def get_repetitive_word(paragraph: str) -> str:
    """
    returns a string or word that is most repeated in the 
    given string or paragraph.
    """
    words = paragraph.split()
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    max_value = max(word_count.values())
    for key, value in word_count.items():
        if value == max_value:
            max_key = key
    return max_key, max_value

max_repeated_string, repetition_count = get_repetitive_word(input("Please Enter a string: "))
print('The maximum repeated string in paragraph entered by you is {} and repeated for {} times.'.format(max_repeated_string, repetition_count))

def get_max_repeated(paragraph: str) -> str:
    """
    returns list of max repated strings and repetition count in a pragraph.
    """
    words = paragraph.split()
    word_count, res = {}, []
    for word in words:
        word_count[word] = word_count.get(word ,0) + 1
    max_value = max(word_count.values())
    for key, value in word_count.items():
        if value == max_value:
            res.append(key)
    
    return res, max_value

max_keys , max_value = get_max_repeated(input('Please Enter a string: '))
print('The maximum repeatition of word is {} times and repeated words are: {}'.format(max_value, max_keys))

def greet(f_name, *argv):
    """demo function for *args """
    print("Hello {}".format(f_name))
    for arg in argv:
        print("Hello {}".format(arg))

greet('Venkat','Python', 'World', 'Students')

def greet_diff(**kwargs):
    """demo function for **kwargs"""
    for key, value in kwargs.items():
        print("{0} {1}".format(key, value))

greet_diff(Hello = "Python", Hola = "Programming", Welcome = "PC")