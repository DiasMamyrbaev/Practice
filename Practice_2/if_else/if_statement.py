# Checking if an item is in a list
users = ["admin", "student", "teacher"]
current_user = "admin"

if current_user in users:
    print("Access granted: user found in the system.")

# Checking string length
password = "my_secure_password123"
if len(password) > 8:
    print("The password meets security requirements.")

# Nested if (checking two conditions)
age = 20
has_id = True
if age >= 18:
    if has_id:
        print("Passage allowed.")