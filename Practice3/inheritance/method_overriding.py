# Пример 1: Простое переопределение метода
class Animal:
    def sound(self):
        return "Some sound"

class Cat(Animal):
    def sound(self):
        return "Meow"

animal = Animal()
cat = Cat()
print(animal.sound())
print(cat.sound())

# Пример 2: Переопределение с вызовом родительского метода через super()
class Vehicle:
    def start(self):
        return "Vehicle started"

class Car(Vehicle):
    def start(self):
        original = super().start()
        return f"{original} and Car engine started"

c = Car()
print(c.start())

# Пример 3: Переопределение __init__
class Product:
    def __init__(self, name):
        self.name = name

class DiscountedProduct(Product):
    def __init__(self, name, discount):
        super().__init__(name)
        self.discount = discount

p = DiscountedProduct("Laptop", 10)
print(p.name, p.discount)

# Пример 4: Переопределение магических методов
class Book:
    def __init__(self, title):
        self.title = title
    def __str__(self):
        return f"Book: {self.title}"

class EBook(Book):
    def __str__(self):
        return f"E-Book: {self.title}"

b = Book("Paper")
e = EBook("Digital")
print(b)
print(e)

# Пример 5: Переопределение метода класса (@classmethod)
class Parent:
    @classmethod
    def identify(cls):
        return "Parent"

class Child(Parent):
    @classmethod
    def identify(cls):
        return "Child"

print(Parent.identify())
print(Child.identify())