#Operators are some special symbols that are used for carrying out some mathematical operations or logic

"""
1. Arithmetic operators
+ -> addition
- -> substraction
* -> multiplication
/ -> division
// -> integer division
% -> modulus
** -> exponent/ power
"""

x = int(input('Please enter a number: '))
y = int(input('Please enter a number: '))

print('X + Y = ' + str((x+y)))
print('X - Y = ' + str((x-y)))
print('X * Y = ' + str((x*y)))
print('X / Y = ' + str((x/y)))
print('X // Y = ' + str((x//y)))
print('X % Y = ' + str((x%y)))
print('X ** Y = ' + str((x**y)))

"""
2.COmparison Operators
> -> greater than
< -> less than
>= -> greater than or equal to 
<= -> less than or equal to 
== -> if both sides are equal
!= -> not equal
"""

print('X > Y is ', x>y)
print('X >= Y is ', x>=y)
print('X < Y is ', x<y)
print('X <= Y is ', x<=y)
print('X == Y is ', x==y)
print('X != Y is ', x!=y)

"""
3. Logical Operator
and 
|True|True|True
|True|False|False
|False|True|False
|False|False|False
or
|True|True|True
|True|False|True
|False|True|True
|False|False|False
not
True -> False and viceversa
"""
a = True
b = False
print('A and B is ', a and b)
print('A or B is ', a or b)
print('not A is', not a)

"""
4. Bitwise Operators
& -> bitwise and
| -> bitwise or
~ -> bitwise not
^ -> bitwise xor
>> -> bitwise left-shift
<< -> bitwise right-shift
"""
c = int(input('Please enter a number: '))
j = int(input('Please enter a number: '))
print('Bitwise and of c and j is: ' + str(c & j))
print('Bitwise or of c and j is: ' + str(c | j))
print('Bitwise not/compliment of c is: ' + str(~c))
print('Bitwise xor of c and j is: ' + str(c ^ j))
print('Bitwise and of c is: ' + str(c >> 3))
print('Bitwise and of j is: ' + str(j << 3))
"""
Assignment Operators
 = -> assignment
 += -> adding with assignment
 -= -> substracting with assignment
 *= -> multiplication with assignment
 /= -> division with assignment
 // -> integer divsion with assignment
 %= -> modulus with assignment
 **= ->exponent with assignment
 ^= -> bitwise xor with assignment
 |= -> or with assignment
 >>= -> right shift with assignment
 <<= -> left shift with assignmenyt
 &= -> and with assignment
"""
x+=10
print('Assignment with addition' + str(x))
x -= 4
print('substracting with assignment' + str(x))
x /= 2
print('dividing with assignment' + str(x))
x //= 3
print('integer division with assignment' + str(x))
x %= 5
print('modulus with assignment' + str(x))
x **= 2
print('exponent with assignment' + str(x))

"""
Identity Operators
is 
is not
"""
x1,y1 = 5,6
x2,y2 = [1,2,3],[1,2,3]

print('X2 is Y2', x2 is y2)
print('X1 is not Y1', x1 is not y1)

"""
membership operators
in 
not in
"""
h = {1: 'a', 2:'b',3:'c'}

print('1 in h ', 1 in h)
print('4 not in h',4 not in h)
print('5 in h', 5 in h)
