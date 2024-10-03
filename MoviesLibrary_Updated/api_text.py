import requests

URL = "https://api.themoviedb.org/3/movie/9737"


https://api.themoviedb.org/3/search/movie/87101
https://api.themoviedb.org/3/movie/9737


headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI3NDRhNjdiZGJmOGQ3MDYxYzU1NzA5OGVjNmE5ZTVhMyIsIm5iZiI6MTcyNzc4OTY3MC41MjI4NjksInN1YiI6IjY2ZmJmOTlhNDExNjU2YzBlNGYxODM0OSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.vmkeo6anPGExY1oblX92W-AVtvt6yhXEZinFts-nUhg"
}

response = requests.get(URL, params={"language": "en-US"}, headers=headers)
data = response.text
print(data)
