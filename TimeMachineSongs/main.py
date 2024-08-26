from dotenv import load_dotenv, dotenv_values
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth
import spotipy
import requests
import os

# Getting API key from .env file
load_dotenv()

# On .env file create CLIENT_ID, CLIENT_KEY, USERNAME for spotify
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_KEY = os.getenv("CLIENT_KEY")
USERNAME = os.getenv("USERNAME")

# URL from where to get the top 100 songs from a certain date
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
URL = "https://www.billboard.com/charts/hot-100/" + f"{date}"

# Get HTML code in order to compose the list with 100 songs
response = requests.get(URL)
soup = BeautifulSoup(response.text, features="lxml")

# Auth with spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:4304/auth/spotify/callback",
        client_id=CLIENT_ID,
        client_secret=CLIENT_KEY,
        show_dialog=True,
        cache_path="token.txt",
        username=USERNAME,
    )
)

# Get top 100 song names and make a list of them
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
"""artist_spans = soup.select("li ul li span")
artist_names = [artist.getText().strip() for artist in artist_spans if not artist.getText().strip().isdigit() and artist.getText().strip() != "-"]"""

# Create a list with spotify URIs for each song
user_id = sp.current_user()["id"]
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Create Spotify playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

# Add songs to the playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print(song_uris)
print(playlist)
