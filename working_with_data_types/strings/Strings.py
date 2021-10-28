import encodings

"""
1. capitalize() ==> COnverts first character to capital letter
2. casefold() ==> converts to case folded strings
3. center() ==> pads string with spcified character
4. count() ==> returns the occurrences of substrings inside string
5. encode() ==> returns encoded string
6. endswith() ==> checks if string ends with the specified suffix
7. expandtabs() ==> replaces tab character with spaces
8. find() ==> returns the index of first occurrence of substring
9. format() ==> formats the string with some nice output
10. string_index() ==> returns the index of sub-string
11. isalnum() ==> checks if all are alphanumeric characters
12. isalpha() ==>  checks if all characters are alphabets
13. islower() ==> checks whether the string is lower cased
14. isupper() ==> checks whether the string was upper
15.lower() ==> converts the string to lower
16.upper() ==> string to upper case.
17.join() ==> concatnates string.
18.split() ==> split th string.
19.strartswith() ==> string that starts with substring or not
20.swapcase() ==> lower to upper and viceversa
"""

s = 'PYTHON PROGRAMMING is Cool'
ns = '- Is An Operator'
print('old string: ', s)
print('Capitalizes_string:', s.capitalize())
print('Capitalizes_string:', ns.capitalize())

st = 'PYTHON PROGRAMMING'
print('Lowercased String: ', st.casefold())

if s.casefold() == st.casefold():
    print('The strings are equal.')
else:
    print('The strings are not equal.')

print('Centered String:', st.center(30, '*'))

msg = 'python is popular programming language'
print('No of times p occurred in string was: ', msg.count('p'))

sf = 'Python programming is cool, isn"t it?'
print('Count without start and end is: ', sf.count('i'))
print('Count with start and end is: ', sf.count('i', 9, 20))


string = 'Python!'
string1 = string.encode("ascii")
print('Without encoding:', string)
print('With encoding: ',string1)