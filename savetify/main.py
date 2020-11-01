import os
import logging
from savetify.src.handler import download, save_data, get_token

URL = "https://api.spotify.com/v1/me/tracks"
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET") 
REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    logger.addHandler(logging.StreamHandler())

    logger.info("Retrieve token")
    token = get_token(CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN)
    logger.info("Download data...")
    data = download(URL, token)
    logger.info("Save data")
    save_data(data)
