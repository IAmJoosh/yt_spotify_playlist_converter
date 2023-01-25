import requests
import os

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
URL_FOR_TOKEN = "https://accounts.spotify.com/api/token"

auth_response = requests.post(
    URL_FOR_TOKEN,
    {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
    },
)

response_data = auth_response.json()

TOKEN = response_data["access_token"]
URL_FOR_PLAYLISTS = "https://api.spotify.com/v1/playlists/"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
PLAYLIST_ID = "5BIJzByhTgiMOfnZ5fZp8S"

URL = URL_FOR_PLAYLISTS + PLAYLIST_ID
playlist_data = requests.get(URL, headers=HEADERS).text

with open("playlist-data.json", "w") as f:
    f.writelines(playlist_data)
