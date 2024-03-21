import imdb
from jinja2 import Environment, FileSystemLoader

ia = imdb.IMDb()

for rank, movie in enumerate(ia.get_top250_movies(), start=1):
    m = reobj.search(str(movie), re.IGNORECASE)
    if m:
        print(f"{rank:>4d}: {movie}")

