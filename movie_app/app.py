from flask import Flask, render_template, url_for, redirect, request, Response, jsonify, session

from forms.register_form import RegisterForm
from forms.login_form import LoginForm
from data_access import db_register_user, db_login_user, db_add_movie, db_remove_movie, db_search_movie, db_get_movies

MOVIES_FILEPATH = 'movies.txt'

app = Flask(__name__)
app.secret_key = 'dev'

@app.route("/api/add_movie", methods=["POST"])
def add_movie():
    title = (request.form.get("title") or "").strip().title()
    director = (request.form.get("director") or "").strip().title()
    year = (request.form.get("year") or "").strip()
    if not title or not director or not year:
        return redirect(url_for('home'))
    
    db_add_movie(title, director, year)
    
    return redirect(url_for('home'))

@app.route("/api/remove_movie/<int:index>", methods=["POST", "DELETE"])
def remove_movie(index):
    db_remove_movie(index)
    
    return redirect(url_for('home'))

@app.route("/api/search_movie", methods=["GET"])
def search_movie():
    query = (request.args.get("query") or "").strip()
    
    results = db_search_movie(query)

    session['search_query'] = query
    session['search_results'] = results
    return redirect(url_for('home'))

@app.route("/register", methods=["GET", "POST"])
def register():
    error = ""
    register_form = RegisterForm()

    if request.method == 'POST':
        username = register_form.username.data
        password = register_form.password.data

        if len(username) == 0 or len(password) == 0:
            error = 'Please enter a username and a password'

        else:
            error = db_register_user(username, password)
            print(error)
            if error == "":
                session['username'] = username
                session['logged_in'] = True
                return redirect(url_for('home'))
    
    return render_template('register.html', form=register_form, message=error, title="Register")

@app.route("/login", methods=["GET", "POST"])
def login():
    error = ""
    login_form = LoginForm()

    if request.method == "POST":
        username = login_form.username.data
        password = login_form.password.data

        if len(username) == 0 or len(password) == 0:
            error = 'Please enter a username and a password'
        
        else:
            response = db_login_user(username, password)
            print(response)
            try:
                session['username'] = response.get('username')
                session['logged_in'] = True
                return redirect(url_for('home'))
            except:
                error = response

    return render_template('register.html', form=login_form, message=error, title="Login")

@app.route("/logout", methods=["GET"])
def logout():
    session['logged_in'] = False
    session.pop("username", '')

    return redirect(url_for('login'))

@app.route("/")
def home():
    movies_data = db_get_movies()

    query = session.pop('search_query', '')
    search_results = session.pop('search_results', [])
    logged_in = session.get('logged_in', False)
    username = session.get('username', '')

    if not logged_in:
        return redirect(url_for('login'))
    
    return render_template('home.html', movies=movies_data, search_query=query, search_results=search_results, logged_in=logged_in, username=username)


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()


