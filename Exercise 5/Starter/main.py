# Write a Python script to use this:
# The user to have the ability to add movie
# Remove a movie (by title or number)
# Search for a movie (by title, director, partial matches)
# List all movies (list with an index number)
#
# Can use functions, will continue later

from movie_lib.library import MovieLibrary

def main():
    movie_library = MovieLibrary("movies.txt")

    print("=================================")
    print("Welcome to the Movies Dictionary!")
    print("[1] Add a new movie")
    print("[2] Remove a movie")
    print("[3] Search for a movie")
    print("[4] List all movies")
    print("[5] Exit")
    print("=================================")

    choice = 0

    while choice != 5:
        choice = int(input("Enter your movies dictionary choice: "))
        print("=====================================")

        if choice == 1:
            movie_title = input("Enter movie title: ").title()
            movie_director = input("Enter movie director: ").title()
            movie_year = input("Enter movie year: ")
            movie_library.add_movie(movie_title, movie_director, movie_year)

        elif choice == 2:
            query = input("Enter the title or number of the movie to remove: ")
            if query.isdigit():
                movie_library.remove_movie_by_index(int(query) - 1)
            else:
                result = movie_library.search_movies(query)
                if not result:
                    print("No results")
                elif len(result) > 1:
                    print("Multiple matches found. Please remove by number instead.")
                    movie_library.display_results(result)
                else:
                    movie_to_remove, idx = result[0]
                    movie_library.remove_movie_by_index(idx)

        elif choice == 3:
            query = input("Enter a movie title or director to search for: ")
            found_movies = movie_library.search_movies(query)
            if found_movies:
                print(f"Found {len(found_movies)} match(es):")
                movie_library.display_results(found_movies)

        elif choice == 4:
            print("--- All Movies ---")
            movie_library.display_movies()

        print("=====================================")

    print("Goodbye!")


if __name__ == "__main__":
    main()