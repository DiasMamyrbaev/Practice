import re

s = input()
pattern = re.compile("^\d+$")
x = pattern.match(s)

if x:
    print("Match")
else:
    print("No match")