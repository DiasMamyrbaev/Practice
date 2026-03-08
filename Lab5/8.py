import re

s = input()
cut = input()

x = re.split(cut, s)
print(",".join(x))