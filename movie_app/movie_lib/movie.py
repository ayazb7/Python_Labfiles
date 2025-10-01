class Movie:
    def __init__(self, title, director, year):
        self._title = title
        self._director = director
        self._year = year

    def __str__(self):
        return f"{self._title} ({self._year}) - Director: {self._director}"

    def to_file_string(self):
        return f"{self._title},{self._director},{self._year}"

    def get_title(self):
        return self._title

    def get_director(self):
        return self._director

    def get_year(self):
        return self._year
