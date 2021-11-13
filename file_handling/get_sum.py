# this file demonstrates opening and parsing file using re
import re

file_name = input("Please enter file name: ")
if len(file_name.split(".")) != 2:
    file_name = "regex_sum_1410638.txt"
try:
    file_handle = open(file_name)
except:
    print("No file found with that name")

res, total = [], 0
for line in file_handle:
    for cursor in re.findall("[0-9]+", line):
        total += int(cursor)


print(total)
