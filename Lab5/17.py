import re

s = input()

pattern = r"\d{2}/\d{2}/\d{4}" 
x = re.findall(pattern, s)

print(len(x))