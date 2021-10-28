"""
A regular expression(REgEx) is a sequence f characters that defines a search pattern
MetaCHaracters : [] . ^ $ * ? {} () \ | 
[] -> set of characters
. -> any single character except '\n'
^ -> checks if string starts with certain pattern or character
$ -> checks if strings ends with certain character
* -> used for counting occurrences of patterns
+, ? -> matches one or more occurrences towards the pattern left
{x,y}, [x-y] -> its used for matching number of characters where x is lower limit and y is upper limit
| -> it acts like a or operator
() ->grouping in pattern 
"""
import re

pattern = "^a...s$"
test_string = "abyss"
result = re.match(pattern=pattern, string=test_string)

if result:
    print("Search Successful")
else:
    print("Search unsuccessful")
