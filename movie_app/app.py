from flask import Flask, render_template, url_for, redirect, request, Response, jsonify, session
import mysql.connector as mysql

MOVIES_FILEPATH = 'movies.txt'

app = Flask(__name__)
app.secret_key = 'dev'

mysql_db = mysql.connect(host="localhost", user="root", passwd="", db="movies_db")

@app.route("/api/add_movie", methods=["POST"])
def add_movie():
    title = (request.form.get("title") or "").strip().title()
    director = (request.form.get("director") or "").strip().title()
    year = (request.form.get("year") or "").strip()
    if not title or not director or not year:
        return redirect(url_for('home'))
    
    mysql_cursor = mysql_db.cursor()
    mysql_cursor.execute("INSERT INTO movie (title, director, year) VALUES (%s, %s, %s)", (title, director, year))
    mysql_db.commit()
    
    return redirect(url_for('home'))

@app.route("/api/remove_movie/<int:index>", methods=["POST", "DELETE"])
def remove_movie(index):
    
    mysql_cursor = mysql_db.cursor()
    mysql_cursor.execute("DELETE FROM movie WHERE id = %s", (index,))
    mysql_db.commit()
    
    return redirect(url_for('home'))

@app.route("/api/search_movie", methods=["GET"])
def search_movie():
    query = (request.args.get("query") or "").strip()
    
    mysql_cursor = mysql_db.cursor(dictionary=True)
    like = f"%{query}%"
    mysql_cursor.execute(
        "SELECT id, title, director, year FROM movie WHERE title LIKE %s OR director LIKE %s ORDER BY id",
        (like, like)
    )
    results = mysql_cursor.fetchall()
    session['search_query'] = query
    session['search_results'] = results
    return redirect(url_for('home'))
   
@app.route("/")
def home():
    mysql_cursor = mysql_db.cursor(dictionary=True)
    mysql_cursor.execute("SELECT id, title, director, year FROM movie ORDER BY id")
    movies_data = mysql_cursor.fetchall()

    query = session.pop('search_query', '')
    search_results = session.pop('search_results', [])

    return render_template('home.html', movies=movies_data, search_query=query, search_results=search_results)


def main():
    mysql_cursor = mysql_db.cursor()
    mysql_cursor.execute(
        "CREATE TABLE IF NOT EXISTS movie (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), director VARCHAR(255), year INT)")
    mysql_db.commit()
    
    app.run(debug=True)


if __name__ == "__main__":
    main()


