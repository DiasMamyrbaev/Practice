# Пример 1: sorted с лямбдой для сортировки строк по длине
words = ["apple", "kiwi", "banana", "cherry", "grape"]
sorted_by_len = sorted(words, key=lambda s: len(s))
print(sorted_by_len)

# Пример 2: sorted с лямбдой для сортировки списка кортежей по второму элементу
pairs = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print(sorted_pairs)

# Пример 3: sorted с лямбдой для сортировки словаря по значениям
d = {'a': 10, 'b': 5, 'c': 20, 'd': 15}
sorted_by_value = sorted(d.items(), key=lambda item: item[1])
print(sorted_by_value)

# Пример 4: sorted с лямбдой для сортировки по убыванию (reverse=True)
numbers = [5, 2, 8, 1, 9]
desc = sorted(numbers, key=lambda x: x, reverse=True)
print(desc)

# Пример 5: sorted с лямбдой для сложного критерия (например, сначала чётные, потом нечётные)
nums = [3, 1, 4, 2, 5, 6]
custom_sort = sorted(nums, key=lambda x: (x % 2, x))
print(custom_sort)