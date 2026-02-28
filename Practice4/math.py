# Math and random operations
import math
import random

# built functions
numbers = [1.5, 2.7, -3.9, 4.2]
print(max(numbers))
print(min(numbers))
print(abs(-5))
print(round(2.675, 2))
print(pow(2, 10))

# math
print(math.sqrt(16))
print(math.pi)
print(math.sin(math.radians(30)))
print(math.ceil(4.1))
print(math.floor(4.9))

# random
print(random.randint(1, 10))
fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))
random.shuffle(fruits)
print(fruits)