# Пример 1: Простое множественное наследование
class Flyer:
    def fly(self):
        print("Flying")

class Swimmer:
    def swim(self):
        print("Swimming")

class Duck(Flyer, Swimmer):
    pass

d = Duck()
d.fly()
d.swim()

# Пример 2: Конфликт имён - разрешается порядком наследования (MRO)
class A:
    def action(self):
        print("A")

class B:
    def action(self):
        print("B")

class C(A, B):
    pass

c = C()
c.action()

# Пример 3: Ромбовидное наследование и super()
class Base:
    def __init__(self):
        print("Base init")

class Left(Base):
    def __init__(self):
        super().__init__()
        print("Left init")

class Right(Base):
    def __init__(self):
        super().__init__()
        print("Right init")

class Bottom(Left, Right):
    def __init__(self):
        super().__init__()
        print("Bottom init")

b = Bottom()

# Пример 4: Использование mixins
class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class XmlMixin:
    def to_xml(self):
        return f"<data>{self.__dict__}</data>"

class Data(JsonMixin, XmlMixin):
    def __init__(self, value):
        self.value = value

d = Data(42)
print(d.to_json())
print(d.to_xml())

# Пример 5: Проверка MRO (метод разрешения порядка)
class X: pass
class Y: pass
class Z(X, Y): pass
print(Z.__mro__)
