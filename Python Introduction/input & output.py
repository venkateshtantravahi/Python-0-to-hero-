#python input and output statements 
x=input("Enter First number:")
y=input("Enter Second Number:")
i=int(x)
j=int(y)
print("The Sum:", i+j)

#Or else even we can simplify the above program:
x=int(input("Enter First number:"))
y=int(input("Enter Second Number:"))
print("The Sum:", i+j)

#some other examples are given below 
eno=int(input("Enter the Emplyoyee number:"))
ename=input("Enter the Employee name:")
esal=float(input("Enter the employee salary:"))
eaddr=input("Enter the employee address:")
married=bool(input("Is employee married?[True|False]:"))

print("Please confimr your provided information")
print("Emplyoyee number:", eno)
print("Employee name:", ename)
print("Employee salary:", esal)
print(" Employee address:", eaddr)
print("Employee married?:", married)