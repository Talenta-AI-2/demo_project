import sqlite3
from fuzzywuzzy import process


# def create_user_table():
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id INTEGER PRIMARY KEY,
#             first_name TEXT,
#             last_name TEXT,
#             email TEXT UNIQUE,
#             password TEXT
#         )
#     """)
#     conn.commit()
#     conn.close()

# def add_user(first_name, last_name, email, password):
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     try:
#         cursor.execute("""
#             INSERT INTO users (first_name, last_name, email, password)
#             VALUES (?, ?, ?, ?)
#         """, (first_name, last_name, email, password))
#         conn.commit()
#         return True
#     except sqlite3.IntegrityError:
#         return False
#     finally:
#         conn.close()

# def verify_user(email, password):
#     conn = sqlite3.connect('database.db')
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
#     result = cursor.fetchone()
#     conn.close()
#     return result

def get_all_food_names():
    conn = sqlite3.connect('gizi_indo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT NAMA FROM indonesian_food_composition")
    food_names = [row[0] for row in cursor.fetchall()]
    conn.close()
    return food_names

def get_nutritional_info(food_name):
    all_food_names = get_all_food_names()
    best_match, score = process.extractOne(food_name, all_food_names)
    if score < 60:
        return None

    conn = sqlite3.connect('gizi_indo.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM indonesian_food_composition WHERE NAMA=?", (best_match,))
    result = cursor.fetchone()
    conn.close()
    return result
