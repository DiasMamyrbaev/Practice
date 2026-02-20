# Пример 1: Функция без параметров
def greet():
    print("Hello, world!")

greet()

# Пример 2: Функция с одним параметром
def square(x):
    return x ** 2

print(square(5))

# Пример 3: Функция с несколькими параметрами
def add(a, b):
    return a + b

print(add(3, 7))

# Пример 4: Функция, которая ничего не возвращает (None)
def show_message(msg):
    print(msg)

result = show_message("Hi")
print(result)

# Пример 5: Функция с документирующей строкой (docstring)
def multiply(x, y):
    """Возвращает произведение двух чисел."""
    return x * y

print(multiply(4, 5))
print(multiply.__doc__)