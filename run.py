import json
from spotipy_client import SpotifyClient


def run():
    #Load Credentials
    with open('creds/credentials.json') as data_file:
        data = json.load(data_file)
    CLIENT_ID = data["spotify"]["clientId"]
    CLIENT_SECRET = data["spotify"]["clientSecret"]
    USERNAME = data["spotify"]["username"]
    client = SpotifyClient(CLIENT_ID, CLIENT_SECRET, USERNAME)

if __name__ == '__main__':
    run()
