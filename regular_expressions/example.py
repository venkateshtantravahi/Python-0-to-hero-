# this file finds the pattern and returns the from mails
#  along with count of each mail
import re

file_name = input("Please enter file nane: ")

try:
    file_handle = open(file_name)
except:
    print("No such file found")

mails = dict()


def example2(fh):
    for line in fh:
        line = line.rstrip()
        if re.search(pattern="^From:", string=line):
            line = line.split()
            mail = line[1]
            mails[mail] = mails.get(mail, 0) + 1

    print(mails)


example2(file_handle)
