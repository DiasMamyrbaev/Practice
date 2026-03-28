import csv
from connect import get_connection

def create_tables():
    commands = """
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        phone VARCHAR(50) NOT NULL
    )
    """
    conn = get_connection()
    if conn is not None:
        try:
            with conn.cursor() as cur:
                cur.execute(commands)
            conn.commit()
            print("Таблица 'contacts' создана.")
        except Exception as e:
            print(f"Ошибка при создании таблицы: {e}")
        finally:
            conn.close()

import os

def import_csv(filename="contacts.csv"):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    full_path = os.path.join(current_dir, filename)
    
    conn = get_connection()
    if conn is not None:
        try:
            with open(full_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                with conn.cursor() as cur:
                    for row in reader:
                        cur.execute(
                            "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                            (row['name'], row['phone'])
                        )
                conn.commit()
                print(f"Данные из {full_path} импортированы.")
        except FileNotFoundError:
            print(f"Файл НЕ НАЙДЕН по пути: {full_path}")
            print("Убедитесь, что contacts.csv лежит в той же папке, что и phonebook.py")
        except Exception as e:
            print(f"Ошибка импорта: {e}")
        finally:
            conn.close()

def add_contact(name, phone):
    """Добавляет новый контакт введенный с консоли."""
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO contacts (name, phone) VALUES (%s, %s)",
                    (name, phone)
                )
            conn.commit()
            print(f"Контакт {name} добавлен.")
        finally:
            conn.close()

def update_contact(contact_id, new_name=None, new_phone=None):
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                if new_name:
                    cur.execute("UPDATE contacts SET name = %s WHERE id = %s", (new_name, contact_id))
                if new_phone:
                    cur.execute("UPDATE contacts SET phone = %s WHERE id = %s", (new_phone, contact_id))
            conn.commit()
            print(f"Контакт ID {contact_id} обновлен.")
        finally:
            conn.close()

def get_contacts(filter_by=None, value=None):
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                if filter_by == 'name':
                    cur.execute("SELECT * FROM contacts WHERE name ILIKE %s", (f"%{value}%",))
                elif filter_by == 'phone':
                    cur.execute("SELECT * FROM contacts WHERE phone LIKE %s", (f"{value}%",))
                else:
                    cur.execute("SELECT * FROM contacts ORDER BY id")
                
                rows = cur.fetchall()
                print("\n--- Список контактов ---")
                if not rows:
                    print("Пусто.")
                for row in rows:
                    print(f"ID: {row[0]} | Имя: {row[1]} | Телефон: {row[2]}")
                print("------------------------\n")
        finally:
            conn.close()

def delete_contact(delete_by, value):
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cur:
                if delete_by == 'name':
                    cur.execute("DELETE FROM contacts WHERE name = %s", (value,))
                elif delete_by == 'phone':
                    cur.execute("DELETE FROM contacts WHERE phone = %s", (value,))
            conn.commit()
            print(f"Контакт с {delete_by} = {value} удален (если он существовал).")
        finally:
            conn.close()

def main_menu():
    create_tables()
    
    while True:
        print("\n ТЕЛЕФОННАЯ КНИГА ")
        print("1. Импортировать данные из CSV")
        print("2. Добавить контакт (вручную)")
        print("3. Обновить контакт")
        print("4. Найти/Показать контакты")
        print("5. Удалить контакт")
        print("0. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            import_csv()
            
        elif choice == '2':
            name = input("Введите имя: ")
            phone = input("Введите телефон: ")
            add_contact(name, phone)
            
        elif choice == '3':
            get_contacts()
            try:
                c_id = int(input("Введите ID контакта для обновления: "))
                n_name = input("Введите новое имя (или нажмите Enter, чтобы пропустить): ")
                n_phone = input("Введите новый телефон (или нажмите Enter, чтобы пропустить): ")
                update_contact(c_id, n_name if n_name else None, n_phone if n_phone else None)
            except ValueError:
                print("ID должен быть числом.")
                
        elif choice == '4':
            print("Фильтры: 1 - Все, 2 - По имени, 3 - По началу номера телефона")
            f_choice = input("Выбор фильтра: ")
            if f_choice == '2':
                val = input("Введите часть имени: ")
                get_contacts('name', val)
            elif f_choice == '3':
                val = input("Введите код/начало номера: ")
                get_contacts('phone', val)
            else:
                get_contacts()
                
        elif choice == '5':
            print("Удалить по: 1 - Имени, 2 - Телефону")
            d_choice = input("Выбор: ")
            val = input("Введите точное значение для удаления: ")
            if d_choice == '1':
                delete_contact('name', val)
            elif d_choice == '2':
                delete_contact('phone', val)
            else:
                print("Неверный выбор.")
                
        elif choice == '0':
            print("Выход из программы.")
            break
        else:
            print("Неизвестная команда. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()