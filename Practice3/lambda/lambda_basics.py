# Пример 1: Простая лямбда-функция
add = lambda x, y: x + y
print(add(5, 3))

# Пример 2: Лямбда без аргументов
greet = lambda: "Hello!"
print(greet())

# Пример 3: Лямбда с одним аргументом
square = lambda x: x ** 2
print(square(7))

# Пример 4: Лямбда с условным выражением
max_of_two = lambda a, b: a if a > b else b
print(max_of_two(10, 20))

# Пример 5: Лямбда, возвращающая другую лямбду (замыкание)
multiply_by = lambda n: lambda x: x * n
times_3 = multiply_by(3)
print(times_3(9))