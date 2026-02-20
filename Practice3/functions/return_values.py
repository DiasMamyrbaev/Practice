# Пример 1: Возврат одного значения
def get_radius():
    return 10

r = get_radius()
print(r)

# Пример 2: Возврат нескольких значений (упакованных в кортеж)
def get_dimensions():
    width = 100
    height = 50
    return width, height

w, h = get_dimensions()
print(w, h)

# Пример 3: Возврат None (явно или неявно)
def do_nothing():
    pass

print(do_nothing())

# Пример 4: Возврат из функции в зависимости от условия
def absolute_value(x):
    if x < 0:
        return -x
    return x

print(absolute_value(-7))
print(absolute_value(5))

# Пример 5: Возврат функции (замыкание)
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

double = make_multiplier(2)
print(double(10))