from abc import ABC, abstractmethod

class IStorage(ABC):
    """Interface for movie storage management"""

    @abstractmethod
    def list_movies(self):
        """Returns a dictionary of movies from storage."""
        pass

    @abstractmethod
    def add_movie(self,title,year ,rating ,poster):
        """Adds a new movie to storage."""
        pass

    @abstractmethod
    def delete_movie(self,title):
        """Delete a movie from storage"""
        pass

    @abstractmethod
    def update_movie(self,title, rating):
        """Update an existing movie's rating"""
        pass

