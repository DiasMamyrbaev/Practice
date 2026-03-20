with open("example.txt", "r", encoding="utf-8") as f:
    print("--- Читаем всё сразу ---")
    print(f.read())

with open("example.txt", "r", encoding="utf-8") as f:
    print("--- Построчное чтение в список ---")
    lines = f.readlines()
    for i, line in enumerate(lines):
        print(f"Строка {i}: {line.strip()}")