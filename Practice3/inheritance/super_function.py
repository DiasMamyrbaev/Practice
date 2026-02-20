# Пример 1: Использование super() для вызова метода родителя
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()
        print("Hello from Child")

c = Child()
c.greet()

# Пример 2: super() с __init__
class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

circle = Circle("red", 5)
print(circle.color, circle.radius)

# Пример 3: super() в контексте множественного наследования (MRO)
class Base:
    def __init__(self):
        print("Base init")

class A(Base):
    def __init__(self):
        super().__init__()
        print("A init")

class B(Base):
    def __init__(self):
        super().__init__()
        print("B init")

class C(A, B):
    def __init__(self):
        super().__init__()
        print("C init")

c = C()

# Пример 4: super() с аргументами (редко используется)
class OldStyleMixin:
    def method(self):
        print("Mixin method")

class MyClass(OldStyleMixin):
    def method(self):
        super(MyClass, self).method()
        print("MyClass method")

obj = MyClass()
obj.method()

# Пример 5: super() для доступа к атрибутам родителя (не только методам)
class Parent:
    class_attr = "parent"

class Child(Parent):
    def print_attr(self):
        print(super().class_attr)

ch = Child()
ch.print_attr()