#  Classic counter
count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1

# Interactive input (loop to a specific value)
user_input = ""
while user_input.lower() != "exit":
    user_input = input("Type something (or 'exit' to exit): ")
    print(f"You entered: {user_input}")

# Filling a list using while
numbers = []
while len(numbers) < 3:
    numbers.append(len(numbers) * 10)
print(f"Generated list: {numbers}")