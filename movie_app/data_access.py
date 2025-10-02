import mysql.connector as mysql
import hashlib

mysql_db = mysql.connect(host="localhost", user="root", password="", db="movies_db")

def get_db_connection():
    mysql_db = mysql.connect(host="localhost", user="root", password="", db="movies_db")

    return mysql_db

def db_register_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    password_hash = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute("SELECT id FROM person WHERE username = %s", (username,))
    if cursor.fetchone():
        return "User with this username already exists"

    sql = "INSERT INTO person (username, password_hash) VALUES (%s, %s)"
    val = (username, password_hash)
    cursor.execute(sql, val)

    conn.commit()

    return ""

def db_login_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    password = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT * FROM person WHERE username = %s AND password_hash = %s", (username, password))

    user = cursor.fetchone()
    
    if user:
        idx, username, password_hash = user
        return {"username": username}
    else:
        return "Login details are incorrect"


def db_add_movie(title, director, year):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO movie (title, director, year) VALUES (%s, %s, %s)", (title, director, year))
    conn.commit()

def db_remove_movie(idx):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movie WHERE id = %s", (idx,))
    conn.commit()

def db_search_movie(query):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    like = f"%{query}%"
    cursor.execute(
        "SELECT id, title, director, year FROM movie WHERE title LIKE %s OR director LIKE %s ORDER BY id",
        (like, like)
    )
    results = cursor.fetchall()

    return results

def db_get_movies():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, title, director, year FROM movie ORDER BY id")
    movies_data = cursor.fetchall()

    return movies_data

def main():
    print(mysql_db)

    mysql_cursor = mysql_db.cursor()
    mysql_cursor.execute(
        "CREATE TABLE IF NOT EXISTS movie (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), director VARCHAR(255), year INT)")
    
    mysql_cursor.execute(
        "CREATE TABLE IF NOT EXISTS person (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password_hash VARCHAR(255))"
    )
    
    mysql_db.commit()

    print(mysql_cursor.rowcount, "record inserted.")

if __name__ == "__main__":
    main()