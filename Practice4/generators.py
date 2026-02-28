# Iterator and generator exercises

# Итератор для чисел от 0 до n-1
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current

# Генератор Фибоначчи
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

# Генератор выражение
squares = (x*x for x in range(10))

# Демонстрация работы
if __name__ == "__main__":
    it = iter([1,2,3])
    print(next(it))
    
    for num in CountDown(5):
        print(num)
    
    for f in fibonacci(100):
        print(f)
    
    print(list(squares))