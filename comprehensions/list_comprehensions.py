"""
Easier way of declaring a list or defining a list is called list comprehension

[expression for item in list]
"""
from math import pi

letters = []

for char in "String":
    letters.append(char)
print("Traditional List declaration", letters)

h_letters = [char for char in "String"]
print("Comprehensed List: ", h_letters)

even_numbers = [x for x in range(20) if x % 2 == 0]
print("List of even numbers: ", even_numbers)

lis = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(lis)

even_or_odd = ["even" if i % 2 == 0 else "odd" for i in range(50)]
print("Even or Odd: ", even_or_odd)

transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 7]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)

transposed_matrix = [[row[i] for row in transposed] for i in range(2)]
print(transposed_matrix)

cubes = [x ** 3 for x in range(10)]
print("The cubes list is: {}".format(cubes))

squares = list(map(lambda x: x ** 2, range(10)))
print("The sqaures list is: {}".format(squares))

# tuples in list with and without comprehension
combs = []
for comb_x in [1, 2, 3]:
    for comb_y in [4, 5, 6, 2]:
        if comb_x != comb_y:
            combs.append((comb_x, comb_y))
print("The combinations are: {}".format(combs))

combination = [
    (combi_x, combi_y)
    for combi_x in [1, 2, 3]
    for combi_y in [4, 5, 6]
    if combi_x != combi_y
]
print("Combinations using comprehension are: {}".format(combination))

vec = [-4, -2, 0, 2, 4]
# Create a new list with vec
print("Fourth multiple of each element: {}".format([x * 4 for x in vec]))
# filtering list vec
print("Negative values in vec are: {}".format([x for x in vec if x < 0]))
# calling methods on each item
print("The abs of vec is: {}".format([abs(x) for x in vec]))
# Creating tuples as items inside list
print("The modified ves is: {}".format([(x, x ** 2) for x in vec]))

# making deep list flat
deep_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Normal List : {}".format([num for item in deep_list for num in item]))

com_list = [str(round(pi, i)) for i in range(1, 6)]
print(com_list)


# matrix comprehensions
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print("The matrix is : {}".format(matrix))

# without comprehension
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print("The transposed matrix is: {}".format(transposed))

# With comprehension
transpose = [[row[i] for row in matrix] for i in range(4)]
print("Transpose of matrix is : {}".format(transpose))

zip_list = list(zip(*matrix))
print("Using zip function : {}".format(zip_list))
