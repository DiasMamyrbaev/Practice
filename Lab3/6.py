class Shape():
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
try:
    n, m = map(int,input().split())
    rn = Rectangle(n,m)

    print(rn.area())
except:
    pass