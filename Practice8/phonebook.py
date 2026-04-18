from connect import connect
import os
import csv


def create_tables():
    commands = """
    CREATE TABLE IF NOT EXISTS Contacts (
        id INT PRIMARY KEY,
        names TEXT NOT NULL,
        phone TEXT
    );
    """
    conn = connect()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute(commands)
            conn.commit()
            cur.close()
            print("Table 'Contacts' is ready, bro.")
        except Exception as e:
            print(f"Error creating table: {e}")
        finally:
            conn.close()



def Search_contacts():
    conn = connect()
    if not conn: 
        return
    
    cur = conn.cursor()

    pattern = input("What do you want: ")

    cur.execute(
        "SELECT * FROM Search_contacts(%s)",
        (pattern,)
        )
    rows = cur.fetchall()

    for i in rows: 
        print(i)

    cur.close()
    conn.close()





def Pagination():
    conn = connect()

    if not conn: 
        return
    
    cur = conn.cursor()

    limit = int(input("Limit: "))
    offset = int(input("Skip: "))

    cur.execute(
        "SELECT * FROM get_contacts(%s, %s)",
        (limit, offset)
        )

    rows = cur.fetchall()

    for i in rows: 
        print(i)

    cur.close()
    conn.close()




def Add_Update_contacts():
    conn = connect()
    if not conn: 
        return
    
    cur = conn.cursor()

    contact_id = input("Contact ID: ")
    name = input("Contact name: ")
    phone = input("Phone: ")

    cur.execute(
        "CALL upsert_contacts(%s, %s, %s)", 
        (contact_id, name, phone)
        )


    conn.commit()
    cur.close()
    conn.close()




def Insert_many_contacts():
    conn = connect()
    if not conn: 
        return
    
    cur = conn.cursor()

    contact_ids = [id.strip() for id in input("IDs (|): ").split("|")]
    names = [n.strip() for n in input("Names (|): ").split("|")]
    phones = [p.strip() for p in input("Phones (|): ").split("|")]

    cur.execute(
        "CALL insert_many_contacts(%s, %s, %s)", 
        (contact_ids, names, phones)
        )
    
    conn.commit()
    cur.close()
    conn.close()




def Delete_contacts():
    conn = connect()
    if not conn: 
        return
    
    cur = conn.cursor()

    some_info = input("ID, Name, or Phone to delete: ")
    cur.execute(
        "CALL delete_contacts(%s)", 
        (some_info,)
        )
    
    conn.commit()
    cur.close()
    conn.close()





def Run_SQL_files(filename):
    base_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_path, filename)

    conn = connect()
    if not conn: 
        return
    
    try:
        cur = conn.cursor()
        with open(full_path, "r", encoding="utf-8") as f:
            cur.execute(f.read())
        conn.commit()
        print(f"Executed: {filename}")
    except Exception as error:
        print(f"Error in {filename}: {error}")
    finally:
        conn.close()

def Import_csv(filename="new_contacts.csv"):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(current_dir, filename)

    conn = connect()

    if conn:
        try:
            with open(full_path, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                cur = conn.cursor()
                for row in reader:
                    cur.execute("INSERT INTO Contacts (id, names, phone) VALUES (%s, %s, %s)", 
                                (row['id'], row['names'], row['phone']))
                conn.commit()
                print("CSV Imported.")
        except Exception as error:
            print(f"Mistake: {error}")
        finally:
            conn.close()





if __name__ == "__main__":
    
    create_tables()

    while True:
        print("1.Search Contacts")
        print("2.Import data from CSV")
        print("3.Add or Update Contacts")
        print("4.Run SQL life")
        print("5.Delete Contacts")
        print("6.Pagination")
        print("7.Insert many Contacts")
        print("8.Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            Search_contacts()
        elif choice == "2":
            Import_csv()
        elif choice == "3":
            Add_Update_contacts()
        elif choice == "4":
            Run_SQL_files("functions.sql")
            Run_SQL_files("procedures.sql")
        elif choice == "5":
            Delete_contacts()
        elif choice == "6":
            Pagination()
        elif choice == "7":
            Insert_many_contacts()
        elif choice == "8":
            break
        else:
            print("No choice")
