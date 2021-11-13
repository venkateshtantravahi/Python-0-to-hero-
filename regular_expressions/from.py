# this file uses 'mbox.txt' and gets the mail address from that file
import re

file_name = input("Please enter file nane: ")

try:
    file_handle = open(file_name)
except:
    print("No such file found")


def example1(fh):
    for line in fh:
        line = line.rstrip()
        x = re.findall('\S+@\S+', line)
        if len(x) > 0:
            print(x)



example1(file_handle)

