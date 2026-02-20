mapping = {
    "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
    "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9"
}

expression = input()

math_expr = expression
for word, digit in mapping.items():
    math_expr = math_expr.replace(word, digit)


if "+" in math_expr:
    parts = math_expr.split("+")
    result = int(parts[0]) + int(parts[1])
elif "-" in math_expr:
    parts = math_expr.split("-")
    result = int(parts[0]) - int(parts[1])
elif "*" in math_expr:
    parts = math_expr.split("*")
    result = int(parts[0]) * int(parts[1])

reverse_mapping = {v: k for k, v in mapping.items()}

final_output = ""
for digit in str(result):
    if digit == "-":
        final_output += "-"
    else:
        final_output += reverse_mapping[digit]

print(final_output)