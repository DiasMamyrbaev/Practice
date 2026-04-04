import csv
from connect import connect

def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            studentId TEXT,
            studentName TEXT,
            phone TEXT
        );
    """)

    conn.commit()
    cur.close()
    conn.close()


def insert_from_csv():
    conn = connect()
    cur = conn.cursor()

    with open("students.csv", "r") as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            cur.execute(
                "INSERT INTO students (studentId, studentName, phone) VALUES (%s,%s,%s)",
                (row[0], row[1], row[2])
            )

    conn.commit()
    cur.close()
    conn.close()


def insert_from_console():
    conn = connect()
    cur = conn.cursor()

    studentId = input("Student ID: ")
    studentName = input("Student Name: ")
    phone = input("Phone: ")

    cur.execute(
        "INSERT INTO students (studentId, studentName, phone)VALUES (%s,%s,%s)",
        (studentId, studentName, phone)
    )

    conn.commit()
    cur.close()
    conn.close()


def update_student():
    conn = connect()
    cur = conn.cursor()

    studentId = input("Enter student ID to update: ")
    newName = input("New name: ")
    newPhone = input("New phone: ")

    cur.execute(
        """
        UPDATE students
        SET studentName=%s, phone=%s
        WHERE studentId=%s
        """,
        (newName, newPhone, studentId)
    )

    conn.commit()
    cur.close()
    conn.close()


def query_students():
    conn = connect()
    cur = conn.cursor()

    prefix = input("Phone prefix: ")

    cur.execute(
        "SELECT * FROM students WHERE phone LIKE %s",
        (prefix + "%",)
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def delete_student():
    conn = connect()
    cur = conn.cursor()

    name = input("Student name to delete: ")

    cur.execute(
        "DELETE FROM students WHERE studentName=%s",
        (name,)
    )

    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_table()
    while True:
        print("1. Insert from CSV")
        print("2. Insert from Console")
        print("3. Update Student")
        print("4. Query Students")
        print("5. Delete Student")
        print("6. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            insert_from_csv()
        elif choice == 2:
            insert_from_console()
        elif choice == 3:
            update_student()
        elif choice == 4:
            query_students()
        elif choice == 5:
            delete_student()
        elif choice == 6:
            break
        else:
            print("Invalid choice")
