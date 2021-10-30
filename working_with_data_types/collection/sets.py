# Sets are unordered collection of objects

# Creating Sets
sets = {1, 2, 3, 4, 5}
print(sets)
print(type(sets))

hs = {1, 1.0, "Hello", True, (1, 2, 3)}
print(hs)

# We can't add duplicate elements in sets
s = {1, 2, 3, 4, 2, 43, 2, 3, 4, 1}
print(s)

# create an empty set
se = set()
print(type(se))

# We can't declare empty set using curly braces
se1 = {}
print(type(se1))

# Adding some data into sets
"""1. add()"""
m_set = {1, 3, 4, 5}
print("set before adding", m_set)

m_set.add(6)
print("After adding single element", m_set)

"""2. Update()"""
m_set.update([2, 7, 8])
print("Updated using list", m_set)

m_set.update({9, 10, 11})
print("Updated using set", m_set)

# Deleting items from set
"""1. discard()"""
m_set.discard(10)
print(m_set)
"""2.remove()"""
m_set.remove(2)
print(m_set)
"""3.pop()"""
m_set.pop()
print(m_set)
"""4.clear()"""
m_set.clear()
print(m_set)

# Operations in sets
A = {1, 2, 3, 4, 5}
B = {6, 7, 8, 9, 0, 4, 1, 3}

print("Set-A declaration", A)
print("Set-B declaration", B)

"""1. Set Union"""
print("union of A,B", A | B)
print("union of A,B", B.union(A))

"""2. Intersection"""
print("Intersection of A,B", A & B)
print("Intersection of A,B", A.intersection(B))

"""3. Difference"""
print("Difference btw A,B", A - B)
print("Difference btw A,B", A.difference(B))

"""4. Symmetric Difference"""
print("Symmetric-Difference btw A,B", A ^ B)
print("Symmetric-Difference btw A,B", A.symmetric_difference(B))

"""
5. isdisjoint(value)
Determines whether or not two sets have any elements in common
returns True if x1 and x2 have no items in common
"""
x1 = {'foo', 'bar','baz'}
x2 = {'baz', 'qux', 'cux'}

print(x1.isdisjoint(x2))
print(x1.isdisjoint(x2-{'baz'}))

"""
6. x1.issubset(x2) / x1 <= x2
returns True if x1 is usbset of x2 and viceversa
"""
num1 = {2,3,4}
print(num1.issubset({1,2,3,4,5,6,7,8,9}))
print(num1 <= {2,3,4})
print(num1 < {2,3,4})

"""
7. issuperset() 
superset is reverse of subset 
returns true if x1 is superset of x2
"""
print(x1.issuperset({'foo'}))
print(x1 >= {'foo'})
print(x1 > {'foo','bar','baz'})

"""
8. intersection_update() or &=
updates the current set with common elements btw both of them 
"""
x1.intersection_update(x2)
print(x1)

"""
9. difference_update() or -=
modify set by difference
"""
x1.difference_update(x2)
print(x1)

"""
10. symmetric_difference_update() or ^=
update x1, retining elements found in either x1 or x2 but not in both 
"""
x1.symmetric_difference_update(x2)
print(x1)

