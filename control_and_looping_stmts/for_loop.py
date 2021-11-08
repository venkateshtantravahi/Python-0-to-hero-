"""
The for loop is used to iterate over a sequence or iterable object such as lists, tuple, string
Iterating is also called as traversal

for val in sequence:
    body of for
"""
sum = 0
lst2 = list(map(int, input("Enter a number: ").strip().split()))
print(lst2)
for val in lst2:
    sum += val

print("The sum of elements in list: ", sum)

lst = list(range(2, 30, 3))
print("List created using range class was: ", lst)

for i in range(11):
    print(i)

for indx in range(len(lst)):
    print("Element was", lst[indx])

for i in lst:
    print(i)
else:
    print("No item left")

for i in lst:
    if i == 31:
        print("found")
else:
    print("Not found")


student_name = "John"
marks = {"John": 90, "Jules": 55, "Clark": 75}
for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print("No entry found with that name.")

string = "Python Programming"
for char in string:
    print("CHaracter in string is:", char)


# Given list of customers get the list of active customers 
# condition for active is atleast 5% of total customers 
customers = list(map(str, input("Please Enter sequence of customers: ").split()))
customer_trades_percentile = dict((customer, (customers.count(customer)/len(customers)*100)) for customer in customers)
res = []
for cust in customer_trades_percentile.items():
    if cust[1] >= 5.0:
        res.append(cust[0])
print("Active Customers: ", res)