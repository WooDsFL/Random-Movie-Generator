import requests
import random

# Your TMDb API Key
API_KEY = '8fb70b4c5713da4eeb852ffdc6279332'
BASE_URL = 'https://api.themoviedb.org/3'

# Function to get a random movie
def get_random_movie():
    # Generate a random page number to fetch a random movie
    page = random.randint(1, 500)  # You can adjust the range for more pages if needed
    discover_url = f'{BASE_URL}/discover/movie'
    params = {
        'api_key': API_KEY,
        'language': 'en-US',
        'sort_by': 'popularity.desc',  # Sort by popularity
        'include_adult': False,        # Exclude adult content
        'include_video': False,        # Exclude video content
        'page': page                   # Random page number
    }
    response = requests.get(discover_url, params=params)
    response.raise_for_status()  # Raise an exception for HTTP errors
    movies = response.json().get('results', [])

    if not movies:
        print("No movies found. Try again.")
        return None

    # Randomly pick a movie from the list
    movie = random.choice(movies)
    return {
        'title': movie.get('title'),
        'release_date': movie.get('release_date', 'N/A'),
        'overview': movie.get('overview', 'No description available.'),
        'poster_url': f"https://image.tmdb.org/t/p/w500{movie['poster_path']}" if movie.get('poster_path') else None
    }

# Main function to display a random movie
def main():
    print("Welcome to the Movie Randomizer!")

    # Get a random movie
    movie = get_random_movie()

    if movie:
        print("\nRandom Movie Suggestion:")
        print(f"Title: {movie['title']}")
        print(f"Release Date: {movie['release_date']}")
        print(f"Overview: {movie['overview']}")
        if movie['poster_url']:
            print(f"Poster URL: {movie['poster_url']}")

if __name__ == '__main__':
    main()
