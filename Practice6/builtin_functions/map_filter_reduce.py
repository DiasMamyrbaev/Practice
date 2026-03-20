from functools import reduce

nums = [1, 2, 3, 4, 5, 6]

# map: возводим в квадрат
squared = list(map(lambda x: x**2, nums)) # [1, 4, 9, 16, 25, 36]

# filter: только четные
evens = list(filter(lambda x: x % 2 == 0, nums)) # [2, 4, 6]

# reduce: сумма всех элементов
total_sum = reduce(lambda x, y: x + y, nums) # 21

print(f"Квадраты: {squared}, Четные: {evens}, Сумма: {total_sum}")