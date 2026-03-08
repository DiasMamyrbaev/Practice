import re

s = input()

pattern = re.compile("\w+")

x = pattern.findall(s)

print(len(x))