'''
     Challenge : Personal Movie Tracker with JSON

     Create a python CLI tool that lets users maintain their own 
     person movie database, Like a mini  IMDB.

     Program should :
        1. Store all movie data in a 'movie.jsonfile.
        2. Each movie should have :
            - Title
            - Director
            - Year of Release
            - Genre
            - Rating (out of 10)
        3. Allow the user to :
            - Add a new movie
            - View all movies
            - Search for a movie by title or genre
            - Exit the app
            - Update movie details
            - Delete a movie from the database
            

'''


import json
import os

# File where the movie data will be stored
FILE_NAME = "movie.json"

# Function to load data from the JSON file
def load_data():
    if not os.path.exists(FILE_NAME):
        return []  # Return empty list if file doesn't exist
    with open(FILE_NAME, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

# Function to save data to the JSON file
def save_data(movies):
    with open(FILE_NAME, "w") as file:
        json.dump(movies, file, indent=4)

# Function to add a new movie
def add_movie(movies):
    print("\n--- Add New Movie ---")
    title = input("Enter the movie name: ")
    director = input("Director: ")
    year = input("Year of Release: ")
    genre = input("Genre: ")
    rating = input("Enter rating (0-10): ")
    
    new_movie = {
        "title": title,
        "director": director,
        "year": year,
        "genre": genre,
        "rating": rating
    }
    
    movies.append(new_movie)
    save_data(movies)
    print("Movie added")

# Function to display all movies
def view_movies(movies):
    print("\n--- All Movies ---")
    if not movies:
        print("Your database is empty!")
        return
    for i, movie in enumerate(movies, 1):
        print(f"{i}. {movie['title']} | Genre: {movie['genre']} | Rating: {movie['rating']}/10")

# Function to search movies by title or genre
def search_movie(movies):
    query = input("\nSearch by Title or Genre: ").lower()
    found = [m for m in movies if query in m['title'].lower() or query in m['genre'].lower()]
    
    if found:
        print("\n--- Search Results ---")
        for m in found:
            print(f"Title: {m['title']} | Director: {m['director']} | Rating: {m['rating']}")
    else:
        print("No matching movies found.")

# NEW: Function to delete a movie
def delete_movie(movies):
    view_movies(movies)
    if not movies: return
    try:
        index = int(input("\nEnter the movie number to delete: ")) - 1
        if 0 <= index < len(movies):
            removed = movies.pop(index)
            save_data(movies)
            print(f"'{removed['title']}' has been deleted.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

# NEW: Function to update movie details
def update_movie(movies):
    view_movies(movies)
    if not movies: return
    try:
        index = int(input("\nEnter the movie number to update: ")) - 1
        if 0 <= index < len(movies):
            print("Leave blank to keep existing value.")
            title = input(f"New Title ({movies[index]['title']}): ") or movies[index]['title']
            rating = input(f"New Rating ({movies[index]['rating']}): ") or movies[index]['rating']
            
            movies[index]['title'] = title
            movies[index]['rating'] = rating
            save_data(movies)
            print("Movie updated successfully!")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")

# Main Menu Logic
def main():
    movies = load_data()
    
    while True:
        print("\n MyMovieDB")
        print("1. Add Movie")
        print("2. View All Movies")
        print("3. Search Movie")
        print("4. Update Movie")
        print("5. Delete Movie")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
        if choice == '1':
            add_movie(movies)
        elif choice == '2':
            view_movies(movies)
        elif choice == '3':
            search_movie(movies)
        elif choice == '4':
            update_movie(movies)
        elif choice == '5':
            delete_movie(movies)
        elif choice == '6':
            print("Exiting application... Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-6.")

if __name__ == "__main__":
    main()