# Finding the first matching number
i = 1
while i < 100:
    if i % 7 == 0 and i % 5 == 0:
        print(f"The first number that is a multiple of 7 and 5: {i}")
        break
    i += 1

# "Infinite" loop with exit condition
attempts = 0
while True:
    attempts += 1
    if attempts == 3:
        print("The maximum number of attempts has been reached.")
        break