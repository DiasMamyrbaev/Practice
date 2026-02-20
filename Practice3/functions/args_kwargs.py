# Пример 1: Использование *args для передачи произвольного числа аргументов
def concatenate(*args):
    return '-'.join(args)

print(concatenate("a", "b", "c"))

# Пример 2: Использование **kwargs для передачи произвольного числа именованных аргументов
def build_profile(**kwargs):
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

print(build_profile(name="John", age=25, city="London"))

# Пример 3: Комбинация *args и **kwargs
def func_with_both(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

func_with_both(1, 2, 3, name="Anna", age=22)

# Пример 4: Распаковка последовательности в *args при вызове функции
numbers = [2, 4, 6]
def multiply_three(a, b, c):
    return a * b * c

print(multiply_three(*numbers))

# Пример 5: Распаковка словаря в **kwargs при вызове функции
def show_details(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")

data = {"name": "Mike", "age": 28, "city": "Paris"}
show_details(**data)