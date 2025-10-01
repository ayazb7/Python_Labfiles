# Input details of a movie
# Name of movie
# Length (in minutes)
# Director's name
# Year

# Print out all the details

movie_name = input('Enter movie name: ')
movie_length_mins = int(input('Enter movie length (minutes): '))
movie_director = input('Enter movie director: ')
movie_year = input('Enter movie release year: ')

print(f"The movie is called {movie_name}, the duration is {movie_length_mins // 60} hours {movie_length_mins % 60} minutes long, and the director is {movie_director}. {movie_name} was released in {movie_year}.")
