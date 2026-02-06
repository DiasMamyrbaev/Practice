# Nested Loops (Multiplication Table for 2 and 3)
for i in range(2, 4):
    for j in range(1, 6):
        print(f"{i} * {j} = {i * j}")

# Dictionary search
user_data = {"name": "Dias", "role": "Student", "lab": 2}
for key, value in user_data.items():
    print(f"Place: {key}, Meaning: {value}")

# Using else in a for loop
for x in range(3):
    print(f"Step {x}")
else:
    print("The cycle has been completed!")