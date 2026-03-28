import psycopg2

hostname = 'localhost'
database = 'demo'     
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
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            phone VARCHAR(50) NOT NULL
        )
    """
    
    cur.execute(sql_script)
    
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