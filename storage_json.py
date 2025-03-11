import json
import os.path
from istorage import IStorage

class StorageJson(IStorage):
    """JSON-based storage implementation"""
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open (self.file_path,"w") as file:
                json.dump({},file)    #intialize with empty dictionary


    def _load_movies(self):
        """load movies from json file"""
        with open (self.file_path,"r") as file:
            return json.load(file)


    def _save_movies(self,movies):
        """save movies to json file"""
        with open (self.file_path,"w") as file:
            json.dump(movies, file, indent=4)


    def list_movies(self):
        """Returns all sorted movies as dictionary"""
        try:
            with open(self.file_path,'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}


    def add_movie(self, title, year, rating, poster):
        """Adds a new movies to storage"""
        movies = self._load_movies()
        movies[title] = {"year": year , "rating": rating , "poster": poster}
        with open(self.file_path, 'w') as file:
            json.dump(movies, file, indent=4)


    def delete_movie(self, title):
        """Deletes a movies from storage """
        movies = self._load_movies()
        if title in movies:
            del movies[title]
            with open(self.file_path, 'w') as file:
                json.dump(movies, file, indent=4)


    def update_movie(self, title, rating):
        """Updates an existing movie's rating"""
        movies = self._load_movies()
        if title in movies:
            movies[title]["rating"] = rating
            with open(self.file_path, 'w') as file:
                json.dump(movies, file, indent=4)


