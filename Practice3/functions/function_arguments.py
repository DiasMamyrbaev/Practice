# Пример 1: Позиционные аргументы
def power(base, exp):
    return base ** exp

print(power(2, 3))

# Пример 2: Именованные аргументы (ключевые слова)
def describe_pet(name, animal_type):
    print(f"{name} is a {animal_type}.")

describe_pet(animal_type="dog", name="Rex")

# Пример 3: Аргументы со значениями по умолчанию
def repeat(text, times=2):
    return text * times

print(repeat("Ha"))
print(repeat("Ha", 4))

# Пример 4: Произвольное количество позиционных аргументов (*args)
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))

# Пример 5: Произвольное количество именованных аргументов (**kwargs)
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")