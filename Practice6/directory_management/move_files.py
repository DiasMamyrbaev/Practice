import os
import shutil

# Убедимся, что директории существуют
os.makedirs('source_folder', exist_ok=True)
os.makedirs('destination_folder', exist_ok=True)

# Создадим тестовый файл в source_folder
source_file_path = os.path.join('source_folder', 'movable_file.txt')
with open(source_file_path, 'w', encoding='utf-8') as f:
    f.write("Этот файл будет перемещен.")

print(f"1. Создан файл: {source_file_path}")

# 1. Перемещение файла
destination_file_path = os.path.join('destination_folder', 'movable_file.txt')
print(f"\n2. Перемещаем файл в {destination_file_path}...")
shutil.move(source_file_path, destination_file_path)
print("Файл перемещен.")

# Проверка
if os.path.exists(source_file_path):
    print(f"  ОШИБКА: Файл все еще в {source_file_path}")
else:
    print(f"  Успех: Файл больше не в исходной папке.")
if os.path.exists(destination_file_path):
    print(f"  Успех: Файл найден в папке назначения.")

# 2. Копирование файла
copy_file_path = os.path.join('destination_folder', 'copied_file.txt')
print(f"\n3. Копируем файл в {copy_file_path}...")
shutil.copy2(destination_file_path, copy_file_path)
print("Файл скопирован.")

# Финальная проверка
print(f"\nСодержимое 'destination_folder': {os.listdir('destination_folder')}")