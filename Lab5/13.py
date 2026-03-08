import re

s = input()

matches = re.findall(r"\w+", s)

print(len(matches))