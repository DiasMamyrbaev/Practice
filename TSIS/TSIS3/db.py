import psycopg2
from config import get_config

def get_connection():
    try:
        return psycopg2.connect(**get_config())
    except psycopg2.DatabaseError as error:
        print(f"Ошибка подключения к базе данных: {error}")
        return None

def init_db():
    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS players (
                    id       SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL
                );
                CREATE TABLE IF NOT EXISTS game_sessions (
                    id            SERIAL PRIMARY KEY,
                    player_id     INTEGER REFERENCES players(id),
                    score         INTEGER   NOT NULL,
                    level_reached INTEGER   NOT NULL,
                    played_at     TIMESTAMP DEFAULT NOW()
                );
            """)
            conn.commit()
            cur.close()
        except Exception as e:
            print("Ошибка инициализации БД:", e)
        finally:
            conn.close()

def save_result(username, score, level):
    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO players (username) VALUES (%s) ON CONFLICT (username) DO NOTHING RETURNING id;", (username,))
            cur.execute("SELECT id FROM players WHERE username = %s;", (username,))
            player_id = cur.fetchone()[0]
            cur.execute("INSERT INTO game_sessions (player_id, score, level_reached) VALUES (%s, %s, %s);", (player_id, score, level))
            conn.commit()
            cur.close()
        except Exception as e:
            print("Ошибка сохранения:", e)
        finally:
            conn.close()

def get_top_10():
    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("""
                SELECT p.username, g.score, g.level_reached, g.played_at::date
                FROM game_sessions g
                JOIN players p ON g.player_id = p.id
                ORDER BY g.score DESC LIMIT 10;
            """)
            res = cur.fetchall()
            cur.close()
            return res
        finally:
            conn.close()
    return []

def get_personal_best(username):
    conn = get_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("""
                SELECT MAX(g.score) FROM game_sessions g
                JOIN players p ON g.player_id = p.id
                WHERE p.username = %s;
            """, (username,))
            res = cur.fetchone()
            cur.close()
            return res[0] if res and res[0] else 0
        finally:
            conn.close()
    return 0