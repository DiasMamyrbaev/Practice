# Создаем файл и записываем данные
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Привет, Python!\n")
    f.write("Это вторая строка.\n")

# Добавление данных ('a' - append)
with open("example.txt", "a", encoding="utf-8") as f:
    f.write("Добавленная строка.\n")