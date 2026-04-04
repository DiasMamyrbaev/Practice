import psycopg2

hostname = 'localhost'
database = 'template1'     
username = 'postgres'
pwd = 'admin'
port_id = 5432

cur = None 
conn = None

try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    
    cur = conn.cursor()
    
    sql_script = """
        CREATE TABLE IF NOT EXISTS students (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            phone VARCHAR(50) NOT NULL
        )
    """
    
    cur.execute(sql_script)
    cur.execute("UPDATE contacts SET name = %s WHERE id = %s", (new_name, new_id))
    cur.execute("DELETE FROM students WHERE name = %s", (value,))
    cur.execute("SELECT * FROM contacts WHERE name ILIKE %s", (f"{value}%",))
    cur.execute("INSET INTO contacts (name,phone) VALUES (%s,%s)"(row['name'],row['phone']))
    conn.commit()
    print("Таблица 'contacts' создана!")

except Exception as error:
    if conn is not None:
        conn.rollback()
    print(f"Ошибка при работе с PostgreSQL: {error}")

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
    print("Соединение с PostgreSQL закрыто.")