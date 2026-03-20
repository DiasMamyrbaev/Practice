names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

# zip для парной итерации
for name, score in zip(names, scores):
    print(f"Студент {name} получил {score}")

# enumerate для индексов
for index, name in enumerate(names, start=1):
    print(f"{index}. {name}")