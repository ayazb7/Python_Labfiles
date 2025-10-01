movie_name = "X"
movie_dict = {}

# while movie_name:
#     movie_name = input("Enter movie name: ")
#     if movie_name:
#         movie_length_mins = int(input('Enter movie length (minutes): '))
#         movie_director = input('Enter movie director: ')
#         movie_year = input('Enter movie release year: ')
#         movie_dict[movie_name] = [movie_length_mins, movie_director, movie_year]
#
# print(movie_dict)
# for key, value in movie_dict.items():
#     print(f"Movie name is {key}, the duration is {value[0] // 60} hours {value[0] % 60} minutes long, and the director is {value[1]}. {key} was released in {value[2]}.")

while movie_name:
    movie_name = input("Enter movie name: ")
    if movie_name:
        movie_length_mins = int(input('Enter movie length (minutes): '))
        movie_director = input('Enter movie director: ')
        movie_year = input('Enter movie release year: ')
        movie_dict[movie_name] = {
            "year": movie_year,
            "length": movie_length_mins,
            "director": movie_director,
        }

print(movie_dict)
for key, value in movie_dict.items():
    print(f"The movie is {key}, the duration is {value['length'] // 60} hours and {value['length'] % 60} minutes long and released in {value['year']}. The director is {value['director']}.")
