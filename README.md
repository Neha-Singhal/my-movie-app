MovieApp

MovieApp is a Python-based movie management application that allows users to:
	•	Add, update, delete, and search for movies.
	•	Display movie statistics like average rating, median rating, highest-rated, and lowest-rated movies.
	•	Generate a website showing the list of movies.

It integrates with the OMDb API to fetch movie details.

Features
	•	Add Movies: Fetch movie details from the OMDb API and add them to the storage.
	•	Delete Movies: Delete a movie from the storage by title.
	•	Update Movie: Update a movie’s rating.
	•	Search Movies: Search for movies by title or part of the title.
	•	Movies Sorted by Rating: Display movies sorted by rating in descending order.
	•	Movie Stats: Display statistics like total movies, average rating, median rating, highest-rated, and lowest-rated movies.
	•	Random Movie: Display a random movie from the list.
	•	Generate Website: Generate a static HTML website showing the list of movies.

Installation
	1.	Clone the repository
 git clone https://github.com/Neha-Singhal/my-movie-app
 cd movieapp
 	2.	Install dependencies:
  pip install -r requirements.txt
  3.	Create a .env file in the root directory and add your OMDb API key:
  API_KEY=your_omdb_api_key

  Usage

Run the app with:python movieapp.py
