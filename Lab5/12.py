import re

s = input()

x = re.findall(r"\d{2,}", s)
print(*x)
