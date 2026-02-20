class Pair():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self, other):
        new_a = self.a + other.a
        new_b = self.b + other.b
        return Pair(new_a, new_b)
    
try:
    n = list(map(int, input().split()))
    
    if len(n) == 4:
        p1 = Pair(n[0], n[1])
        p2 = Pair(n[2], n[3])

        result_pair = p1.add(p2)

        print(f"Result: {result_pair.a} {result_pair.b}")
except EOFError:
    pass
