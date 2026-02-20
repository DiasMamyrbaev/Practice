# Пример 1: Простейшее определение класса
class Dog:
    pass

my_dog = Dog()
print(type(my_dog))

# Пример 2: Класс с атрибутами класса
class Animal:
    kingdom = "Animalia"

print(Animal.kingdom)

# Пример 3: Класс с методами
class Cat:
    def meow(self):
        print("Meow!")

cat = Cat()
cat.meow()

# Пример 4: Класс с атрибутами экземпляра, добавляемыми вручную
class Person:
    pass

p = Person()
p.name = "John"
p.age = 30
print(p.name, p.age)

# Пример 5: Класс с методами, использующими self
class Rectangle:
    def set_dimensions(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

rect = Rectangle()
rect.set_dimensions(5, 10)
print(rect.area())