import re

s = input()
pattern = r"[A-Z]"

x = re.findall(pattern, s)
print(len(x))