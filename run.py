import json
from spotify_client import SpotifyClient


def run():
    with open('creds\credentials.json') as data_file:
        data = json.load(data_file)
    AUTHTOKEN = data["spotify"]["authToken"]
    spotify_client = SpotifyClient(AUTHTOKEN)

    # search for songs
    artist = input("Input artist name:\n")
    track = input("Input track name:\n")
    spotify_song_id = spotify_client.search_song(artist, track)
    if spotify_song_id:
        added_song = spotify_client.add_song_to_spotify(spotify_song_id)
        if added_song:
            print(f"Added {artist}")


if __name__ == '__main__':
    run()
