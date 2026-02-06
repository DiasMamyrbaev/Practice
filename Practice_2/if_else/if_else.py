# Checking if a number is even
number = 13
if number % 2 == 0:
    print(f"{number} — is even.")
else:
    print(f"{number} — is odd.")

# Simulate login
is_logged_in = False
if is_logged_in:
    print("Welcome to your personal account!")
else:
    print("Please log in.")

# Checking for an empty list
tasks = []
if tasks:
    print(f"You have {len(tasks)} unfulfilled tasks.")
else:
    print("The to-do list is empty. Relax!!")