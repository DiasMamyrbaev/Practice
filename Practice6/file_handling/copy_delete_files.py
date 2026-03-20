import os
import shutil

# Создадим файл для демонстрации, если его нет
with open('my_data.txt', 'a', encoding='utf-8'):
    pass

source_file = 'my_data.txt'
backup_file = 'my_data_backup.txt'
copied_file = 'my_data_copy.txt'
directory_for_copy = 'backups'

print(f"Исходный файл: {source_file}")

# 1. Копирование и резервное копирование с помощью shutil
print("\n1. Создание резервной копии...")
shutil.copy2(source_file, backup_file)
print(f"Резервная копия создана: {backup_file}")

# 2. Копирование файла в другую директорию (с созданием директории)
print("\n2. Копирование в другую директорию...")
os.makedirs(directory_for_copy, exist_ok=True)
destination_path = os.path.join(directory_for_copy, 'my_data_moved_copy.txt')
shutil.copy2(source_file, destination_path)
print(f"Файл скопирован в: {destination_path}")

# 3. Безопасное удаление файлов (с проверкой существования)
print("\n3. Безопасное удаление временных файлов...")
files_to_delete = [backup_file, copied_file]

for file in files_to_delete:
    if os.path.exists(file):
        os.remove(file)
        print(f"Файл '{file}' удален.")
    else:
        print(f"Файл '{file}' не найден, удаление не требуется.")

# Удаление файла в поддиректории (будьте осторожны с этой операцией!)
if os.path.exists(destination_path):
    os.remove(destination_path)
    print(f"Файл '{destination_path}' удален.")