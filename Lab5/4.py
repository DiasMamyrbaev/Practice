import re

txt = input()
pattern = re.findall(r"\d", txt)
print(" ".join(pattern))