import re

s = input()
x = re.match(r"^[A-Za-z]*[0-9]$", s)
if x:
    print("Yes")
else:
    print("No")