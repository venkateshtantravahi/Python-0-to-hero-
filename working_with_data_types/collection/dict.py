#Creating Dictionaries

'''
d = {
    <key> : <value>,
    <key> : <value>,
    .
    .
    .
}
'''

dic = {
    'Programming' : ['C', 'C++', 'Java', "Python"],
    'Subjects' : 'English',
    'IsPerson' : True,
    'Age' : 34
}

print(dic)

dic1 = dict([
    ('Programming',['C', 'C++', 'Java', "Python"]),
    ('Subject', 'Maths'),
    ('Seattle', 'Marines')
])

print(dic1)

dic2 = dict(
    India = 'Delhi',
    Telangana = 'Hyderabad'
)

print(dic2)

d = {0:'a', 1:'b', 2:'c', 4:'d'}
print(d)

print(type(dic2))

#Access Dictionary Values
print(dic['Programming'])
print(dic2['India'])
print(dic1['Seattle'])

#adding items inside dictionary
dic2['Maharastra'] = 'Mumbai'
print(dic2)


#delete items inside a dictionary
del dic['Age']
print(dic)

#declare dictionary dynamically
person = {}
name = input('Enter input for name:')
language_known = input('Enter language known:')
age = int(input('Enter age:'))

person[name] = [language_known, age]

print(person)

#There is no restriction for declaring key names in dictionary

fo = {34 : 'sfkng', 45.67 : 'sngfdog', True : [1,2,3,5,6]}
print(fo)

f = {int : 'dsibg', float : 45656, bool : 4543}
print(f)

d = {(1,1): 'sdjb', (2,3): 'sdfjb'}
print(d)

#built-in methods in dictionaries

"""1.clear()"""
d.clear()
print(d)

"""2. get()"""
print(fo.get(34))
print(fo.get('a'))

"""3. items()"""
print(list(fo.items()))
print(list(fo.items())[1])

"""4. keys()"""
print(list(fo.keys()))

"""5. values()"""
print(list(fo.values()))

"""6. Pop()"""
fo.pop(34)
print(fo)

"""7. popitem()"""
fo.popitem()
print(fo)

"""8. extend()"""
d1 = {'a': 20, 'b':40,'c':80}
print(d1)
d2 = {'d': 56, 'e':True}
print(d2)
d1.update(d2)
print(d1)