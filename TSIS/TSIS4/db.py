import psycopg2

def get_config():
    return {
        "host": "localhost",
        "database": "diasmamyrbaev",
        "user": "postgres",          
        "password": "Versace1978.",
        "port": "5432"
    }

def get_connection():
    try:
        return psycopg2.connect(**get_config())
    except psycopg2.DatabaseError as error:
        print(f"Ошибка подключения к БД: {error}")
        return None

def init_db():
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS leaderboard (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) NOT NULL,
                    score INT NOT NULL,
                    time_survived REAL NOT NULL
                )
            ''')
            conn.commit()
            cursor.close()
        except Exception as e:
            print(f"Ошибка создания таблицы: {e}")
        finally:
            conn.close()

def save_score_db(username, score, time_survived):
    conn = get_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO leaderboard (username, score, time_survived) VALUES (%s, %s, %s)",
                (username, score, time_survived)
            )
            conn.commit()
            cursor.close()
        finally:
            conn.close()

def get_top_scores_db(limit=10):
    conn = get_connection()
    results = []
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT username, score, time_survived FROM leaderboard ORDER BY score DESC, time_survived ASC LIMIT %s", (limit,))
            results = cursor.fetchall()
            cursor.close()
        finally:
            conn.close()
    return results