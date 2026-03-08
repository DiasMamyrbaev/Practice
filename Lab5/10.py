import re

s = input()

pattern = r'cat|dog'

x = re.search(pattern, s)

if x:
    print("Yes")
else:
    print("No")