import json
from spotipy_client import SpotifyClient
from prompt_toolkit import prompt
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import WordCompleter
import click


def run():
    #Load Credentials
    with open('creds/credentials.json') as data_file:
        data = json.load(data_file)
    CLIENT_ID = data["spotify"]["clientId"]
    CLIENT_SECRET = data["spotify"]["clientSecret"]
    USERNAME = data["spotify"]["username"]
    client = SpotifyClient(CLIENT_ID, CLIENT_SECRET, USERNAME)
    commands = {
        'search_song': 'search_song',
        'view_song': 'view_song',
        'get_playlists': 'get_playlists',
        'view_playlist': 'view_playlist',
        'add_song_recs': 'add_song_recs',
        'view_song_recs': 'view_song_recs',
        'quit': 'quit'
    }

    spotify_completer = WordCompleter([
        'search_song',
        'view_song',
        'get_playlists',
        'view_playlist',
        'add_song_recs',
        'view_song_recs',
        'quit'
    ])

    # Need to add flow for inputing songs and getting recommendations as well as overall return features.
    while 1:
        text = prompt('Input Spotify Command: ', completer=spotify_completer)
        if(text=='quit'):
            break

if __name__ == '__main__':
    run()
