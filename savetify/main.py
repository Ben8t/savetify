import os

from savetify.src.handler import parse, save_data


GITHUB_API_KEY = os.getenv("GITHUB_API_KEY")
URL = "https://api.spotify.com/v1/me/tracks"
API_TOKEN = os.getenv("API_TOKEN")


if __name__ == "__main__":
    data = parse(URL, API_TOKEN)
    save_data(data)
