# Creating Tuple

empty_tuple = ()
print("Empty Tuple Declaration",empty_tuple)

str_tuple = ('entiretyn', 'python','programming')
print("Homogenious data in tuple",str_tuple)

print(type(str_tuple))

h_tuple = (1, 23, 34, 'string', 'guido', True)
print("Heterogenous data in tuple",h_tuple)

# Tuple Concatination
print(str_tuple + h_tuple)

# Nesting Tuples
tuple1 = (0,1,2,3,4,5)
tuple2 = ('hi','hello','holla')
tuple3 = (tuple1, tuple2)
print(tuple3)

# Repetition of items inside tuple
t = ('python','Programming') * 10
print(t)

# Tuples are immutable
#tuple1[0] = 45
#print(tuple1)

#slicing tuples 
tpl = (0,1,2,3,4,5)
print(tpl[1:])
print(tpl[2:4])
print(tpl[::-1])

#len of tuple 
print(len(tpl))

#converting list to tuple 
l = [6, 4,56,3,5]
print(tuple(l))
print(tuple('python'))

# deleting tuple
tup = ('math','physics', 'social')
del tup
#print(tup) '''We can't print the tuple once its deleted'''
