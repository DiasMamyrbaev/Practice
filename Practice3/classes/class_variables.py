# Пример 1: Переменная класса, общая для всех экземпляров
class Student:
    school = "Greenwood High"
    def __init__(self, name):
        self.name = name

s1 = Student("Alice")
s2 = Student("Bob")
print(s1.school)
print(s2.school)

# Пример 2: Изменение переменной класса через класс
Student.school = "New School"
print(s1.school)

# Пример 3: Переменная экземпляра перекрывает переменную класса
s1.school = "Individual School"
print(s1.school)
print(s2.school)

# Пример 4: Переменная класса для подсчёта экземпляров
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

a = Counter()
b = Counter()
c = Counter()
print(Counter.count)

# Пример 5: Константы класса
class Constants:
    PI = 3.14159
    GRAVITY = 9.8

print(Constants.PI)
print(Constants.GRAVITY)