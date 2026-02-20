# Пример 1: filter с лямбдой для отбора чётных чисел
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# Пример 2: filter с лямбдой для отбора строк, длина которых больше 3
words = ["cat", "dog", "elephant", "ant", "butterfly"]
long_words = list(filter(lambda w: len(w) > 3, words))
print(long_words)

# Пример 3: filter с лямбдой для отбора положительных чисел
mixed = [-5, 3, -1, 0, 8, -2]
positive = list(filter(lambda x: x > 0, mixed))
print(positive)

# Пример 4: filter с лямбдой для отбора элементов, являющихся строками
data = [42, "hello", 3.14, "world", None, "python"]
strings = list(filter(lambda item: isinstance(item, str), data))
print(strings)

# Пример 5: filter с лямбдой для отбора чисел, кратных 3 и 5 одновременно
nums = list(range(1, 31))
special = list(filter(lambda x: x % 3 == 0 and x % 5 == 0, nums))
print(special)