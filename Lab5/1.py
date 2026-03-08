import re

s = input()

x = re.match("^Hello", s)

if x:
    print("Yes")
else:
    print("No")