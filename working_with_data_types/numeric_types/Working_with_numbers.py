import math

#Numerical Conversions

dec = input('Please Enter a decimal number: ')

print("The decimal value is ", dec)
print(bin(int(dec)), "in binary")
print(oct(int(dec)), "in octal")
print(hex(int(dec)), "in hexadecimal")

# Inbuilt-constants in math module
print('Rturns the value of pi', math.pi)
print('Returns the value fo natural base', math.e)
print('Returns the value of tau', math.tau)
print('Returns the infinite', math.inf)
print('Returns not a number type', math.nan)


#Numerical Functions
"""
1.ceil(x) "provides the greatest rounded integer to the decimal/ float value given by user
2.copysign(x,y) " copies the sign of one variable to other
3.fabs(x) " returns the absolute value given by user
4.factorial(x) " which returns factorial of number(5! = 5*4*3*2*1)
5.floor(x) "returning the smallest rounding integer
6.fsum(iterable_object) "which sums up the items in iterable object
7.gcd(x,y) "greatest common divisor of two numbers
8.isfinite(x) "checks whether the number is finite or not
9.isinf(x) " chcks the numbers is infinite or not
10.isnan(x) " returns if data is not a number
11.remainder(x,y) "gives the remainder of division
"""

x = float(input('Input some float or decimal value: '))
y = float(input('Input some float or decimal value: '))
print('The Floor and Ceiling value of' + str(x) + 'are :' + str(math.floor(x)) + ', ' + str(math.ceil(x)))
print('The value of A after copying the sign of B is: ' + str(math.copysign(20, -35)))
lis = [13, 4.56, 90, -7.3, -54, 6.3, 98]
print('Sum of elements of list :' + str(math.fsum(lis)))
print('The GCD of 24 and 56 is : ' + str(math.gcd(24, 56)))
d = float('nan')
if math.isnan(d):
    print('It is not a number')
v = float('inf')
z = 58
if math.isinf(v):
    print('It is infinite')
print(math.isfinite(v))
print(math.isfinite(z))

# Loarithmic Functions

"""
pow(x,y) ==> returns the power value
sqrt(x) ==> returns the square root of number
exp(x) ==> x^e where e=2.71
log(x[,base]) ==> returns the logarithm where base given
log2(x) ==> returns the log of x to base 2
log10(x) ==> returns log of x to base 10
"""
print('The value of 10^8: ' + str(math.pow(10,8)))
print('The sqrt value of 25: ' + str(math.sqrt(25)))
print('The exponential value of 4^e: ', str(math.exp(4)))
print('The value of log(169): '+ str(math.log(169,13)))
print('The value of log2(1024): '+ str(math.log2(1024)))
print('The value of log10(1024): '+ str(math.log10(1024)))

#Tringonometric & Angular_Conversion Functions
"""
sin(x) : returns the sin value of x
cos(x) : returns the cosine value of x
tan(x) : returns the tangent value of x
asin(x) : reverse or inverse operation of sin 
degrees(x) : angle x in radians to degrees
radians(x) : angle x in degrees to radians
"""

print('The value of Sin(60):' + str(math.sin(math.radians(60))))
print('The value of cos(pi): ' + str(math.cos(math.pi)))
print('The value of tan(90) :' + str(math.tan(math.pi/2)))