from .movie import Movie

class MovieLibrary:
    def __init__(self, filename="movies.txt"):
        self.filename = filename
        self.movies = self._load_movies()

    def _load_movies(self):
        movies_list = []
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    if line.strip():
                        title, director, year = line.strip().split(',')
                        movies_list.append(Movie(title, director, year))
        except FileNotFoundError:
            print(f"Warning: '{self.filename}' not found. Starting with an empty library.")
        return movies_list

    def _save_movies(self):
        with open(self.filename, "w") as f:
            for movie in self.movies:
                f.write(movie.to_file_string() + "\n")

    def add_movie(self, title, director, year):
        new_movie = Movie(title, director, year)
        self.movies.append(new_movie)
        self._save_movies()
        print(f"Successfully added and saved '{title}'.")

    def remove_movie_by_index(self, index):
        if 0 <= index < len(self.movies):
            removed_movie = self.movies.pop(index)
            self._save_movies()
            print(f"Successfully removed '{removed_movie.title}'.")
            return removed_movie
        else:
            print("Error: Index is invalid.")
            return None

    def search_movies(self, query):
        results = []
        for idx, movie in enumerate(self.movies):
            if query.lower() in movie.title.lower() or query.lower() in movie.director.lower():
                results.append((movie, idx))
        return results

    def display_movies(self):
        for idx, movie in enumerate(self.movies):
            print(f"[{idx + 1}] {str(movie)}")

    def display_results(self, search_result):
        for movie, idx in search_result:
            print(f"[{idx + 1}] {str(movie)}")