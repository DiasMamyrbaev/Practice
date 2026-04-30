from connect import connect
import os
import csv
import json

def Run_SQL_files(filename):
    base_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(base_path, filename)
    conn = connect()
    if not conn: return
    try:
        cur = conn.cursor()
        with open(full_path, "r", encoding="utf-8") as f:
            cur.execute(f.read())
        conn.commit()
        print(f"Executed: {filename}, bro.")
    except Exception as error:
        print(f"Error in {filename}: {error}")
    finally:
        conn.close()



def Search_contacts():
    conn = connect()
    if not conn: return
    cur = conn.cursor()
    pattern = input("Enter name, email, or phone to search: ")
    cur.execute("SELECT * FROM search_contacts_extended(%s)", (pattern,))
    rows = cur.fetchall()
    for row in rows: print(row)
    cur.close()
    conn.close()

def Import_csv(filename="tsis.csv"):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(current_dir, filename)
    conn = connect()
    if not conn: return
    try:
        with open(full_path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            cur = conn.cursor()
            for row in reader:
                cur.execute("INSERT INTO groups (name) VALUES (%s) ON CONFLICT (name) DO NOTHING", (row.get('group', 'Other'),))
                cur.execute("SELECT id FROM groups WHERE name = %s", (row.get('group', 'Other'),))
                group_id = cur.fetchone()[0]

                cur.execute("""
                    INSERT INTO contacts (id, names, email, birthday, group_id) 
                    VALUES (%s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING
                """, (row['id'], row['names'], row.get('email'), row.get('birthday'), group_id))


             
                cur.execute("""
                    INSERT INTO phones (contact_id, phone, type) 
                    SELECT %s, %s, %s 
                    WHERE NOT EXISTS (
                        SELECT 1 FROM phones WHERE contact_id = %s AND phone = %s
                    )
                """, (row['id'], row['phone'], row.get('type', 'mobile'), row['id'], row['phone']))
            conn.commit()
            print("CSV Imported successfully.")
    except Exception as error:
        print(f"Mistake: {error}")
    finally:
        conn.close()




def Add_extra_phone():
    conn = connect()
    if not conn: return
    name = input("Enter contact name: ")
    phone = input("Enter new phone: ")
    p_type = input("Type (mobile/home/work): ")
    cur = conn.cursor()
    cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, p_type))
    conn.commit()
    print(f"Phone added to {name}.")
    cur.close()
    conn.close()


def Move_to_group():
    conn = connect()
    if not conn: return
    name = input("Enter contact name: ")
    group = input("Enter new group name: ")
    cur = conn.cursor()
    cur.execute("CALL move_to_group(%s, %s)", (name, group))
    conn.commit()
    print(f"Contact {name} moved to group {group}.")
    cur.close()
    conn.close()



def Add_Update_contacts():
    conn = connect()
    if not conn: return
    cur = conn.cursor()
    try:
        contact_id = int(input("Contact ID (Numbers only): ")) # Исправлено на int
        name = input("Contact name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        p_type = input("Phone type (mobile/home/work): ")
        cur.execute("CALL upsert_contacts_v2(%s, %s, %s, %s, %s)", (contact_id, name, email, phone, p_type))
        conn.commit()
        print("Contact Added/Updated.")
    except ValueError:
        print("Error: ID must be a number!")
    finally:
        cur.close()
        conn.close()



def Delete_contacts():
    conn = connect()
    if not conn: return
    cur = conn.cursor()
    some_info = input("ID or Name to delete: ")
    cur.execute("CALL delete_contacts_v2(%s)", (some_info,))
    conn.commit()
    print("Deleted successfully.")
    cur.close()
    conn.close()



def Pagination():
    conn = connect()
    if not conn: return
    cur = conn.cursor()
    limit = int(input("Limit per page: ") or 3)
    offset = 0
    while True:
        print(f"\n--- Page {(offset//limit) + 1} ---")
        cur.execute("SELECT id, names, email FROM contacts ORDER BY id LIMIT %s OFFSET %s", (limit, offset))
        rows = cur.fetchall()
        if not rows and offset > 0:
            print("No more records.")
            offset -= limit
            continue
        for row in rows: print(row)
        cmd = input("\nCommands: [n]ext, [p]rev, [q]quit: ").strip().lower()
        if cmd == 'n': offset += limit
        elif cmd == 'p': offset = max(0, offset - limit)
        elif cmd == 'q': break
    cur.close()
    conn.close()

def Insert_many_contacts():
    conn = connect()
    if not conn: return
    cur = conn.cursor()
    contact_ids = [int(id.strip()) for id in input("IDs (|): ").split("|")]
    names = [n.strip() for n in input("Names (|): ").split("|")]
    phones = [p.strip() for p in input("Phones (|): ").split("|")]

    cur.execute("CALL insert_many_contacts_v2(%s, %s, %s)", (contact_ids, names, phones))
    conn.commit()
    print("Contacts inserted.")
    cur.close()
    conn.close()



def Sort_and_Filter():
    conn = connect()
    if not conn: return
    cur = conn.cursor()
    print("1. Filter by Group | 2. Sort by Name | 3. Sort by Birthday")
    sub = input("Choice: ")
    
    if sub == "1":
        grp = input("Enter group name: ")
        cur.execute("SELECT c.names, c.email FROM contacts c JOIN groups g ON c.group_id = g.id WHERE g.name = %s", (grp,))
    elif sub == "2":
        cur.execute("SELECT names, email, birthday FROM contacts ORDER BY names ASC")
    elif sub == "3":
        cur.execute("SELECT names, email, birthday FROM contacts ORDER BY birthday ASC")
        
    for row in cur.fetchall(): print(row)
    cur.close()
    conn.close()



def Export_JSON(filename="contacts_export.json"):
    conn = connect()
    if not conn: return
    cur = conn.cursor()
    cur.execute("""
        SELECT c.id, c.names, c.email, TO_CHAR(c.birthday, 'YYYY-MM-DD'), g.name
        FROM contacts c LEFT JOIN groups g ON c.group_id = g.id
    """)
    contacts = []
    for row in cur.fetchall():
        c_dict = {"id": row[0], "name": row[1], "email": row[2], "birthday": row[3], "group": row[4], "phones": []}
        cur.execute("SELECT phone, type FROM phones WHERE contact_id = %s", (row[0],))
        c_dict["phones"] = [{"phone": p[0], "type": p[1]} for p in cur.fetchall()]
        contacts.append(c_dict)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(contacts, f, indent=4)
    print("Exported to JSON.")
    cur.close()
    conn.close()


def Import_JSON(filename="contacts_export.json"):
    if not os.path.exists(filename):
        print("File not found!")
        return
    conn = connect()
    if not conn: return
    cur = conn.cursor()
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for item in data:
        cur.execute("SELECT id FROM contacts WHERE names = %s", (item['name'],))
        exists = cur.fetchone()
        if exists:
            choice = input(f"Contact {item['name']} exists. [s]kip or [o]verwrite? ").strip().lower()
            if choice == 's': continue
            if choice == 'o':
                cur.execute("UPDATE contacts SET email = %s WHERE id = %s", (item['email'], exists[0]))
                c_id = exists[0]
        else:
            cur.execute("INSERT INTO contacts (id, names, email, birthday) VALUES (%s, %s, %s, %s) RETURNING id",
                        (item['id'], item['name'], item['email'], item.get('birthday')))
            c_id = item['id']
            
        for phone in item['phones']:
            cur.execute("INSERT INTO phones (contact_id, phone, type) VALUES (%s, %s, %s)", 
                        (c_id, phone['phone'], phone['type']))
    conn.commit()
    print("Imported from JSON.")
    cur.close()
    conn.close()

if __name__ == "__main__":
    while True:
        print("\n >>>> PHONEBOOK SYSTEM <<<<")
        print("1. Search Contacts")
        print("2. Import data from CSV")
        print("3. Add or Update Contacts")
        print("4. Run SQL files (Schema/Procedures)")
        print("5. Delete Contacts")
        print("6. Pagination")
        print("7. Insert many Contacts")
        print("8. Sort & Filter")
        print("9. Export to JSON")
        print("10. Import from JSON")
        print("11. EXIT")
        print("12. Add extra phone to contact")
        print("13. Move contact to group")
        
        choice = input("Enter choice: ")
        
        if choice == "1": Search_contacts()
        elif choice == "2": Import_csv()
        elif choice == "3": Add_Update_contacts()
        elif choice == "4": 
            Run_SQL_files("schema.sql")
            Run_SQL_files("procedures.sql")
        elif choice == "5": Delete_contacts()
        elif choice == "6": Pagination()
        elif choice == "7": Insert_many_contacts()
        elif choice == "8": Sort_and_Filter()
        elif choice == "9": Export_JSON()
        elif choice == "10": Import_JSON()
        elif choice == "12": Add_extra_phone()
        elif choice == "13": Move_to_group()
        elif choice == "11": break
        else: print("no choice")
