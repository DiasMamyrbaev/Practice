# Пример 1: Обычный метод экземпляра
class Car:
    def __init__(self, model):
        self.model = model
    def drive(self):
        print(f"{self.model} is driving.")

my_car = Car("Toyota")
my_car.drive()

# Пример 2: Статический метод (@staticmethod)
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y

print(MathUtils.add(3, 4))

# Пример 3: Метод класса (@classmethod)
class Employee:
    company = "ABC Corp"
    def __init__(self, name):
        self.name = name
    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

print(Employee.company)
Employee.change_company("XYZ Inc")
print(Employee.company)

# Пример 4: Магический метод __str__
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Point({self.x}, {self.y})"

p = Point(2, 3)
print(p)

# Пример 5: Свойство (property) для управляемого доступа
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

person = Person("John", "Doe")
print(person.full_name)