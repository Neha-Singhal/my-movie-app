from movie_app import MovieApp
from storage_csv import StorageCsv

storage = StorageCsv('movies.csv')
# Create an instance of MovieApp with the CSV storage
movie_app = MovieApp(storage)

# Run the movie application
movie_app.run()
