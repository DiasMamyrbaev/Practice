import os

# 1. Создание вложенных каталогов
print("1. Создание вложенных каталогов 'parent/child/grandchild'...")
os.makedirs('parent/child/grandchild', exist_ok=True)
print("Каталоги созданы (или уже существовали).")

# Создадим несколько пустых файлов внутри для наглядности
with open('parent/child/file1.txt', 'w') as f: f.write("test1")
with open('parent/child/grandchild/file2.log', 'w') as f: f.write("test2")
with open('parent/child/grandchild/file3.txt', 'w') as f: f.write("test3")

# 2. Список файлов и папок в текущем каталоге
print(f"\n2. Содержимое текущей директории '{os.getcwd()}':")
items = os.listdir('.')
for item in items:
    print(f"  - {item}")

# 3. Найти файлы по расширению (например, все .txt в 'parent' и подпапках)
print("\n3. Поиск всех файлов .txt в каталоге 'parent':")
found_files = []
for root, dirs, files in os.walk('parent'):
    for file in files:
        if file.endswith('.txt'):
            full_path = os.path.join(root, file)
            found_files.append(full_path)
            print(f"  Найден: {full_path}")

# 4. Изменение текущей рабочей директории
print(f"\n4. Текущая директория: {os.getcwd()}")
print("Переходим в 'parent/child'...")
os.chdir('parent/child')
print(f"Теперь текущая директория: {os.getcwd()}")

# Возвращаемся обратно (важно для дальнейших примеров)
os.chdir('../..')
print(f"Вернулись в исходную: {os.getcwd()}")