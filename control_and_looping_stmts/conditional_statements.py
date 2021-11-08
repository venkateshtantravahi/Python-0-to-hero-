"""
When Decision making is required we use the "if..elif..else" in python

if test_expression:
    statements of code

if test_expression:
    if block code
else:
    Body of else/ else block code

if test_expression:
    if block code
elif test_expression:
    elif block code
else:
    else block code

"""

num = int(input("PLease enter a number: "))
if num > 0:
    print(num, " is a positive number.")

print("------------------------------------------------------")

if num >= 0:
    print(num, " is a positive number.")
else:
    print(num, " is a negative number.")

print("------------------------------------------------------")

if num > 0:
    print(num, " is a positive number.")
elif num == 0:
    print(num, "Zero.")
else:
    print(num, "is a negative number.")

"""
Writing one if under other is nesting 
"""
print("------------------------------------------------------")
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive Integer")
else:
    print("Negative Integer")

print("////////////////////////////////////////////////////////////////")

age = int(input("Please enter your age: "))

if age >= 21:
    isGraduated = True
else:
    isGraduated = False

if age >= 18:
    hasLicense = True
else:
    hasLicense = False

if isGraduated:
    print("He is graduated and has license.")
elif hasLicense and not isGraduated:
    print('He"s not graduated but has license')
else:
    print('He"s neither graduated nor licensed')

# Comapring numbers 
a, b, c = int(input().split())
if a >= b and a >= c :
    print("a is greatest of three")
elif b>= a and b>=c:
    print("b is the largest of three")
else:
    print("c is the largest of three")