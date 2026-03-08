import re

s = input()
pattern = r"[\w.-]+@[\w.-]+\.\w+"

match = re.search(pattern, s)
if match:
    print(match.group())
else:
    print("No email")