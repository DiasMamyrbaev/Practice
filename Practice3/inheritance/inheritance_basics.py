# Пример 1: Простое наследование
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Woof!")

d = Dog()
d.speak()
d.bark()

# Пример 2: Наследование с инициализацией родителя
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, job):
        Person.__init__(self, name)
        self.job = job

e = Employee("Anna", "Engineer")
print(e.name, e.job)

# Пример 3: Проверка принадлежности к классу (isinstance, issubclass)
print(isinstance(e, Person))
print(issubclass(Employee, Person))

# Пример 4: Наследование атрибутов класса
class Vehicle:
    category = "land"

class Car(Vehicle):
    pass

print(Car.category)

# Пример 5: Множественное наследование (просто)
class A:
    def method(self):
        print("A")

class B:
    def method(self):
        print("B")

class C(A, B):
    pass

c = C()
c.method()