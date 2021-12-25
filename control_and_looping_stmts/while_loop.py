"""
The while loop in python is used to iterate over a block of code 
as long as the test expression is true.We generally use this when we don't know the number of 
iterations beforehand.

While test_expression:
    Body of while loop

Python interprets any non-zero numbers as True. None and '0' are interpreted as false
"""
# program to sum n digits
n = int(input("Enter a number: "))
# initializing sum and counter
sum = 0
counter = 1

while counter <= n:
    sum += counter
    counter += 1  # updating a counter
    print("Counter is: ", counter)

print("The sum of " + str(n) + " numbers is ", sum)

# loops are always infinite
while counter == n:
    print("Equals")
    
print("Done")
