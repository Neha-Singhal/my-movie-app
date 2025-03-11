import os
import requests
import random
from dotenv import load_dotenv

load_dotenv()

class MovieApp:
    def __init__(self, storage):
        """Initialize MovieApp with a storage object
         :param storage: An object that implements the IStorage interface."""
        self._storage = storage
        self._api_key = os.getenv('API_KEY')

    def _fetch_movie_details(self, title):
        """
        Fetches movie details from the OMDb API.
        :param title: The title of the movie to search for.
        :return: A dictionary containing the movie details, or None if the movie is not found.
        """
        url = f"http://www.omdbapi.com/?apikey={self._api_key}&t={title}"
        print(f"Fetching data from: {url}")

        try:
            response = requests.get(url)
            response.raise_for_status() # Raise an exception for HTTP errors
            data = response.json()
            print("API Response:", data)
            if data.get("Response") == "True":
                return {
                    "title": data.get("Title","unknown"),
                    "year": int(data.get("Year","0")),
                    "rating": float(data.get("imdbRating","0")),
                    "poster": data.get("Poster","N/A")
                }
            else:
                print(f"Movie '{title}' not found in OMDb API.")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Error accessing OMDb API: {e}")
            return None


    def _command_list_movies(self):
        """List all movies in storage."""
        movies = self._storage.list_movies()
        if movies:
            for title, details in movies.items():
                print(f"{title} ({details['year']}): {details['rating']} /10")
        else:
            print("No movies found")


    def _command_add_movies(self):
        """Add a movie to storage by fetching details from the OMDb API"""
        title = input("Enter movie title: ")
        movie_details = self._fetch_movie_details(title)
        if movie_details:
            self._storage.add_movie(
                movie_details["title"],
                movie_details["year"],
                movie_details["rating"],
                movie_details["poster"]
            )

            print(f"Movie '{movie_details['title']}' added successfully!")
        else:
            print("Failed to add movie.")


    def _command_delete_movies(self):
        """Delete a movie from storage."""
        title = input("Enter the title of the movie to delete: ")
        self._storage.delete_movie(title)
        print(f"Movie '{title}' deleted successfully!")


    def _command_update_movie(self):
        """Update a movie rating."""
        title = input("Enter the title of the movie to update: ")
        rating = input("Enter new rating: ")
        self._storage.update_movie(title, rating)
        print(f"Movie '{title}' updated successfully!")


    def _command_movie_stats(self):
        """Displays statistic about the movies."""
        movies = self._storage.list_movies()
        if movies:
            total_movies = len(movies)
            # Convert ratings to float and handle missing or invalid ratings
            ratings = []
            for movie in movies.values():
                try:
                    rating = float(movie.get('rating', 0))
                    ratings.append(rating)
                except (ValueError, TypeError):
                    ratings.append(0)
            # Calculate average rating
            avg_rating = sum(ratings) / total_movies if total_movies > 0 else 0

            # Find the highest and lowest rated movies
            highest_rated = max(movies.items(), key=lambda x: float(x[1].get('rating', 0)))
            lowest_rated = min(movies.items(), key=lambda x: float(x[1].get('rating', 0)))

            print(f"\nTotal movies: {total_movies}")
            print(f"Average rating: {avg_rating:.2f}")
            print(f"Highest rated movie: {highest_rated[0]} (Rating: {highest_rated[1].get('rating', 'N/A')})")
            print(f"Lowest rated movie: {lowest_rated[0]} (Rating: {lowest_rated[1].get('rating', 'N/A')})")
        else:
            print("\nNo movies found.")


    def _command_random_movie(self):
        """
        Displays a random movie from the list.
        """
        movies = self._storage.list_movies()
        if movies:
            title = random.choice(list(movies.keys()))
            movie = movies[title]
            print(f"\nRandom Movie: {title} ({movie['year']})")
            print(f"Rating: {movie['rating']}")
            print(f"Poster: {movie['poster']}")
        else:
            print("\nNo movies found.")


    def _command_search_movie(self):
        """
        Searches for a movie by title and displays its details.
        """
        title = input("Enter movie title to search: ")
        movies = self._storage.list_movies()
        if title in movies:
            movie = movies[title]
            print(f"\nMovie Found: {title} ({movie['year']})")
            print(f"Rating: {movie['rating']}")
            print(f"Poster: {movie['poster']}")
        else:
            print(f"\nMovie '{title}' not found.")

    def _command_movies_sorted_by_rating(self):
        """
        Displays all movies sorted by rating in descending order.
        """
        movies = self._storage.list_movies()
        if movies:
            # Sort movies by rating in descending order
            sorted_movies = sorted(movies.items(), key=lambda x: float(x[1].get('rating',0)), reverse=True)

            print("\nMovies Sorted by Rating:")
            for title, details in sorted_movies:
                print(f"{title} ({details['year']}): Rating {details['rating']}")
        else:
            print("\nNo movies found.")


    def _generate_website(self):
        """Generates a website from the movie data."""
       # load the template file
        template_path = os.path.join("static", "index_template.html")
        try:
            with open(template_path, "r") as file:
                template = file.read()
        except FileNotFoundError:
            print("Error: Template file not found.")
            return

        #load movie data
        movies = self._storage.list_movies()

        # Generate the movie grid HTML
        movie_grid_html = ""
        for title, details in movies.items():
            movie_grid_html += f"""
                   <div class="movie-card">
                       <img src="{details['poster']}" alt="{title}">
                       <h2>{title} ({details['year']})</h2>
                       <p>Rating: {details['rating']}</p>
                   </div>
                   """

        # Replace placeholders in the template
        website_html = template.replace("__My Movie App__", "title")
        website_html = website_html.replace("__TEMPLATE_MOVIE_GRID__", movie_grid_html)

        # Save the generated HTML to a file
        output_path = os.path.join("static", "index.html")
        with open(output_path, "w") as file:
            file.write(website_html)

        print("Website was generated successfully.")


    def run(self):
        """runs the movie application."""
        while True:
            print("\nMenu:")
            print("0. Exit")
            print("1. List movies")
            print("2. Add movie")
            print("3. Delete movie")
            print("4. Update movie")
            print("5. Stats")
            print("6. Random movie")
            print("7. Search movie")
            print("8. Movies sorted by rating")
            print("9. Generate website")

            choice = input("Enter choice (0-9): ")

            if choice == '0':
                break
            elif choice == '1':
                self._command_list_movies()
            elif choice == '2':
                self._command_add_movies()
            elif choice == '3':
                self._command_delete_movies()
            elif choice == '4':
                self._command_update_movie()
            elif choice == '5':
                self._command_movie_stats()
            elif choice == '6':
                self._command_random_movie()
            elif choice == '7':
                self._command_search_movie()
            elif choice == '8':
                self._command_movies_sorted_by_rating()
            elif choice == '9':
                self._generate_website()
            else:
                print("Invalid choice. Please try again.")




