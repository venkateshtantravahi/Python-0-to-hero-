import array as arr

#Creating array
sample_array = arr.array('d', [1.1, 4.5,6.7,8.9])
print(sample_array)

# Accessing data from array
print('First Element in arr: {}'.format(sample_array[0]))


#converting list to array
numbered_list = [1,34,56,3,45,43,24,62,78]
numbered_array = arr.array('i', numbered_list)
#slicing array 
print(numbered_array[3:6])
#Change elements
print('Array before changing {}'.format(numbered_array)) 
numbered_array[1] = 90
print('Array After 1st changing {}'.format(numbered_array))
numbered_array[4:7] = arr.array('i', [2,34,56])
print('Array after changing slice {}'.format(numbered_array))

#Add elements to array
numbered_array.append(9)
print("Array after appending {}".format(numbered_array))
numbered_array.extend([2,58,45])
print("Array after extending is {}".format(numbered_array))


# Concatenating arrays
odd_array = arr.array('i', [3,5,7])
even_array = arr.array('i',[2,4,6,8])

numbers = arr.array('i')
numbers = odd_array + even_array

print(numbers)

# Removing elements from array
del numbers[2]
print('After deleting {}'.format(numbers))

del numbers

numbered_array.remove(3)

numbered_array.pop(2)

print("Numbered array after deletion is {}".format(numbered_array))