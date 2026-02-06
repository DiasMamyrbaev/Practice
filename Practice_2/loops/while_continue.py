# Print only odd numbers
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue
    print(f"Odd number: {n}")

# Skipping certain values
i = 0
while i < 5:
    i += 1
    if i == 3:
        print("We're skipping the three...")
        continue
    print(f"Current value: {i}")