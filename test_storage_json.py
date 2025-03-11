from movie_app import MovieApp
from storage_json import StorageJson


storage = StorageJson('movies.json')


print( "movies:", storage.list_movies())

#Add movie
storage.add_movie("Inception", 2010, 9.0,"https://image-url.com")

#List movie
print(storage.list_movies())

#Update movie rating
storage.update_movie("Inception", 8.8)
print(storage.list_movies())

#Delete movie
storage.delete_movie("Inception")
print(storage.list_movies())

movie_app = MovieApp(storage)

# Run the movie application
movie_app.run()
