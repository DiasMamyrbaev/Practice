# Filtering a list (skipping negative numbers)
data = [10, -5, 20, -1, 30]
for num in data:
    if num < 0:
        continue
    print(f"Handling a positive number: {num}")

# Skipping characters in a string
word = "Python3"
for char in word:
    if char.isdigit():
        continue
    print(f"letter: {char}")