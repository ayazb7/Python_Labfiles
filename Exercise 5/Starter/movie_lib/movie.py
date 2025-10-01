class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def __str__(self):
        return f"{self.title} ({self.year}) - Director: {self.director}"

    def to_file_string(self):
        return f"{self.title},{self.director},{self.year}"
