# Short hand if 
a = 50
b = 10
if a > b: print("a more than b")

# Short hand if-else    (Тернарный оператор)
status = "success" if a > 20 else "error"
print(status)

# Use in print
age = 17
print("Access allowed") if age >= 18 else print("Access denied")

# Choosing the minimum
x, y = 10, 20
min_val = x if x < y else y
print(f"Minimum number: {min_val}")