from flask import Flask, render_template, url_for, redirect, request
import os
import sys

CURRENT_DIR = os.path.dirname(__file__)
STARTER_DIR = os.path.join(CURRENT_DIR, 'Starter')
if STARTER_DIR not in sys.path:
    sys.path.append(STARTER_DIR)

from movie_lib.library import MovieLibrary

app = Flask(__name__)

MOVIES_FILEPATH = os.path.join(CURRENT_DIR, 'Starter', 'movies.txt')
movie_library = MovieLibrary(MOVIES_FILEPATH)


@app.route("/")
def root():
    return redirect(url_for('movies_home'))


@app.route("/movies", methods=["GET"])
def movies_home():
    query = request.args.get("q")
    message = request.args.get("m")
    error = request.args.get("e")

    if query:
        results = movie_library.search_movies(query)
        movies_with_index = [(m.get_title(), m.get_director(), m.get_year(), idx + 1) for m, idx in results]
        return render_template(
            "movies.html",
            movies=movies_with_index,
            query=query,
            message=message,
            error=error,
        )
    movies_with_index = [
        (m.get_title(), m.get_director(), m.get_year(), idx + 1)
        for idx, m in enumerate(movie_library.movies)
    ]
    return render_template("movies.html", movies=movies_with_index, message=message, error=error)


@app.route("/movies/add", methods=["POST"])
def add_movie():
    title = (request.form.get("title") or "").strip().title()
    director = (request.form.get("director") or "").strip().title()
    year = (request.form.get("year") or "").strip()

    if not title or not director or not year:
        return redirect(url_for('movies_home', e="Please provide title, director, and year"))

    movie_library.add_movie(title, director, year)
    return redirect(url_for('movies_home', m=f"Added '{title}'"))


@app.route("/movies/remove", methods=["POST"])
def remove_movie():
    index_text = (request.form.get("index") or "").strip()
    if not index_text.isdigit():
        return redirect(url_for('movies_home', e="Invalid movie number"))

    index_1_based = int(index_text)
    removed = movie_library.remove_movie_by_index(index_1_based - 1)
    if removed is None:
        return redirect(url_for('movies_home', e="Movie number out of range"))
    return redirect(url_for('movies_home', m=f"Removed '{removed.get_title()}'."))


if __name__ == "__main__":
    app.run(debug=True)


