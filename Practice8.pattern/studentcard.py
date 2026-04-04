from connect_pattern import connect
import os

def search_students():
    conn = connect()
    cur = conn.cursor()

    pattern = input("Enter search pattern: ")

    cur.execute("SELECT * FROM search_students(%s)", (pattern,))
    rows = cur.fetchall()

    for r in rows:
        print(r)

    cur.close()
    conn.close()


def pagination():
    conn = connect()
    cur = conn.cursor()

    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    cur.execute("SELECT * FROM get_students_page(%s,%s)", (limit, offset))

    rows = cur.fetchall()

    for r in rows:
        print(r)

    cur.close()
    conn.close()


def insert_or_update():
    conn = connect()
    cur = conn.cursor()

    student_id = input("Student ID: ")
    name = input("Student name: ")
    phone = input("Phone: ")

    cur.execute("CALL upsert_student(%s,%s,%s)", (student_id, name, phone))

    conn.commit()

    cur.close()
    conn.close()

def insert_many_students():
    conn = connect()
    cur = conn.cursor()

    student_ids = input("Enter student IDs separated by comma: ").split(",")
    names = input("Enter student names separated by comma: ").split(",")
    phones = input("Enter phones separated by comma: ").split(",")

    student_ids = [id.strip() for id in student_ids]
    names = [n.strip() for n in names]
    phones = [p.strip() for p in phones]
    cur.execute(
        "CALL insert_many_students(%s, %s, %s)",
        (student_ids, names, phones)
    )

    conn.commit()
    for notice in conn.notices:
        print(notice)

    print("Students processed successfully")

    cur.close()
    conn.close()

def delete_student():
    conn = connect()
    cur = conn.cursor()

    value = input("Name or phone to delete: ")

    cur.execute("CALL delete_student(%s)", (value,))

    conn.commit()

    cur.close()
    conn.close()

import os

def run_sql_file(filename):
    base_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_path, filename)
    
    conn = connect()
    if conn is None:
        return

    try:
        cur = conn.cursor()
        with open(full_path, "r", encoding="utf-8") as f:
            cur.execute(f.read())
        conn.commit()
        print(f"Successfully executed: {filename}")
        cur.close()
    except Exception as e:
        print(f"Error running {filename}: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    while True:
        print("1. Search students")
        print("2. Pagination")
        print("3. Insert or update student")
        print("4. Insert many students")
        print("5. Delete student")
        print("6. Run SQL file")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            search_students()   
        elif choice == "2":
            pagination()
        elif choice == "3":
            insert_or_update()
        elif choice == "4":
            insert_many_students()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            run_sql_file("functions.sql")
            run_sql_file("procedures.sql")
        elif choice == "7":
            break
        else:
            print("Invalid choice")
