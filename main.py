from movie_app import MovieApp
from storage_json import StorageJson
from storage_csv import StorageCsv

def main():

    storage = StorageCsv('movies.csv')
    storage1=StorageJson('movies.json')
    # Create an instance of MovieApp with the chosen storage
    movie_app = MovieApp(storage)

    # Run the movie application
    movie_app.run()


if __name__ == "__main__":
    main()