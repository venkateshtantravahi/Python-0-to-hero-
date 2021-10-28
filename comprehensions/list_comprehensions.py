"""
Easier way of declaring a list or defining a list is called list comprehension

[expression for item in list]
"""

letters = []

for char in 'String':
    letters.append(char)
print("Traditional List declaration",letters)

h_letters = [char for char in 'String']
print("Comprehensed List: ", h_letters)

even_numbers = [x for x in range(20) if x % 2 == 0]
print("List of even numbers: ", even_numbers)

lis = [y for y in range(100) if y%2==0 if y%5==0]
print(lis)

even_or_odd = ["even" if i%2==0 else "odd" for i in range(50)]
print("Even or Odd: ", even_or_odd)

transposed = []
matrix = [[1,2,3,4],[4,5,6,7]]

for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)

transposed_matrix = [[row[i] for row in transposed] for i in range(2)]
print(transposed_matrix)