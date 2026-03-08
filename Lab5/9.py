import re

s = input()
pattern = r'\b\w{3}\b'

x = re.findall(pattern, s)
print(len(x))