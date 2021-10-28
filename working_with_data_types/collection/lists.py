# Python Program to demonstrate lists

#Creating lists
b_list = []
print("Blank list", b_list)

n_list = [10,200,5000]
print("\nList of numbers ", n_list)

s_list = ['Typing', 'Python', 'Lists']
print('\nList of strings', s_list)

d_list = ['John Deo', 32, 'London',23.5678]
print('\nList with different data types', d_list)

m_list = [['Multi', 'Dimensional'], ['Lists']]
print('\nMulti-dimensional Lists', m_list)

# to get length of lists we use function len()
print(len(d_list))

# append() which is used to add elements inside lists

n_list.append(1)
n_list.append(3)
n_list.append(5)
print('\nList after appending data is', n_list)

for i in range(100,105):
    s_list.append(i)

print('\ns_list after adding ', s_list)

l = [12,13]
m_list.append(l)
print('\nm_list ', m_list)

#extend is used for appending to a list
d_list.extend(s_list)

print('List after extending ', d_list)

#insert is used for inserting elements in lists at particular node
n_list.insert(1, 100)
print('n_list after inserting ', n_list)

#Accessing List Elements
print(n_list[1])
print(n_list[6])
print(n_list[1:5])


fruits = ['orange', 'banana', 'pinapple','watermelon','banana','sapota','banana']
print("Fruits list {}".format(fruits))
#get count of item from list
count = fruits.count('banana')
print('Fruit {} is repeated for {} times'.format('banana', count))

# get index of item from list
ind = fruits.index('watermelon')
print('Index of {} in list is {}'.format('watermelon', ind))

# reversing string
print("First wasy : {}".format(fruits[::-1]))
reverse = fruits.reverse()
print("Reversed list ",fruits)
# sorting list 
sort = fruits.sort()
print("Sorted list",fruits)

# pop element from list 
print("The popped element from list is {}".format(fruits.pop()))

