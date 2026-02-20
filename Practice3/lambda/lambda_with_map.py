# Пример 1: map с лямбдой для возведения чисел в квадрат
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)

# Пример 2: map с лямбдой для преобразования строк в верхний регистр
words = ["hello", "world", "python"]
uppered = list(map(lambda s: s.upper(), words))
print(uppered)

# Пример 3: map с лямбдой для двух списков (поэлементная сумма)
a = [1, 2, 3]
b = [4, 5, 6]
sums = list(map(lambda x, y: x + y, a, b))
print(sums)

# Пример 4: map с лямбдой для форматирования строк
names = ["Alice", "Bob", "Charlie"]
formatted = list(map(lambda name: f"Hello, {name}!", names))
print(formatted)

# Пример 5: map с лямбдой и условием (например, оставить числа больше 2, но заменить на булево)
nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x > 2, nums))
print(result)