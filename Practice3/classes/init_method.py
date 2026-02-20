# Пример 1: Простой __init__
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book = Book("1984", "George Orwell")
print(book.title, book.author)

# Пример 2: __init__ с параметрами по умолчанию
class Circle:
    def __init__(self, radius=1):
        self.radius = radius

c1 = Circle()
c2 = Circle(5)
print(c1.radius, c2.radius)

# Пример 3: __init__, принимающий различные типы данных
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

s = Student("Alice", [90, 85, 92])
print(s.name, s.grades)

# Пример 4: __init__ с проверкой и установкой атрибутов
class Temperature:
    def __init__(self, celsius):
        if celsius < -273.15:
            raise ValueError("Temperature below absolute zero")
        self.celsius = celsius

try:
    t = Temperature(-300)
except ValueError as e:
    print(e)

# Пример 5: __init__, вызывающий другие методы класса
class Counter:
    def __init__(self, start=0):
        self.value = start
        self.reset()
    def reset(self):
        self.value = 0

c = Counter(10)
print(c.value)
c.reset()
print(c.value)