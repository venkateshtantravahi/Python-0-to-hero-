"""
In python, break and continue stmts can alter the flow of loop

Loops iterate over a block of code until the test expression is flase, but sometimes we want
to terminate the current iteration or even whole loop that's when break and continue come into picture
"""

for char in "Python":
    if char == "h":
        break
    print("Breaked char was: ", char)

for char in "Python":
    if char == "h":
        continue
    print(char)

sequence = {"p", "y", "t", "h", "o", "n"}
for val in sequence:
    pass
