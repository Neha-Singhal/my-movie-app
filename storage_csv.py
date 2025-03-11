import csv
from istorage import IStorage


class StorageCsv(IStorage):
    def __init__(self, file_path):
        """
        Initializes the CSV storage with the given file path.
        :param file_path: Path to the CSV file."""

        self.file_path = file_path

    def list_movies(self):
        """
        Returns a dictionary of dictionaries that
        contains the movies information in the database."""

        movies = {}
        try:
            with open(self.file_path,'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    movies[row['title']] = {'rating' : float(row['rating']),
                                            'year' : int(row['year']),
                                            'poster': row['poster']
                                            }
        except FileNotFoundError:
            pass
        return movies

    def add_movie(self, title, year, rating, poster):
        """
        Adds a movie to the CSV storage.
        """
        movies = self.list_movies()
        movies[title] = {'year': year, 'rating': rating, 'poster': poster}
        self._save_movies(movies)


    def delete_movie(self, title):
        """
        Deletes a movie from the CSV storage.
        """
        movies = self.list_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)


    def update_movie(self, title, rating):
        """
        Updates a movie's rating in the CSV storage.
        """
        movies = self.list_movies()
        if title in movies:
            movies[title]['rating'] = rating
            self._save_movies(movies)


    def _save_movies(self, movies):
        """
        Saves the movie data to the CSV file.
        """
        with open(self.file_path, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['title', 'rating', 'year', 'poster'])
            writer.writeheader()
            for title, details in movies.items():
                writer.writerow({
                    'title': title,
                    'rating': details['rating'],
                    'year': details['year'],
                    'poster': details['poster']
                })




