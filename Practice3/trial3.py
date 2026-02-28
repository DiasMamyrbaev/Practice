"""

class Animal():
    def __init__(self,name):
        self.name = name
    def sound(self):
        return "AAA"
class cat(Animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color = color
    def sound():
        return "OMG"

my_cat = cat("sosiska","rarity")
print(my_cat.name)
print(my_cat.sound())

"""