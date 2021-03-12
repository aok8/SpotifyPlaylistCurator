import requests
import urllib.parse
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

scope = "user-library-read user-read-playback-position user-read-privateu ser-read-email playlist-read-private user-library-modify user-top-read playlist-read-collaborative playlist-modify-public playlist-modify-private ugc-image-upload user-follow-read user-follow-modify user-read-playback-state user-modify-playback-state user-read-currently-playing user-read-recently-played"

redirect_uri = "https://localhost:8080"

# client_credentials_manager = SpotifyClientCredentials(client_id=client_id, 
#                                                       client_secret=client_secret)

# auth_manager = SpotifyClientCredentials(client_id=client_id, 
#                                                       client_secret=client_secret)

# sp = spotipy.Spotify(auth_manager=auth_manager)


class Song(object):
    def __init__(self, name, albumName, artists, song_id, uri):
        self.name = name
        self.albumName = albumName
        self.artists = artists
        self.song_id = song_id
        self.uri = uri

class SongInfo(object):
    def __init__(self, song, acousticness, danceability, energy, 
    instrumentalness, liveness, loudness, valence):
        self.song = song
        self.acousticness = acousticness
        self.danceability = danceability
        self.energy = energy
        self.instrumentalness = instrumentalness
        self.liveness = liveness
        self.loudness = loudness
        self.valence = valence

class Playlist(object):
    def __init__(self, name, owner, id, uri):
        self.name = name
        self.owner = owner
        self.id = id
        self.uri = uri
class SpotifyClient(object):
    def __init__(self, client_id, client_secret, username):
        self.client_id = client_id
        self.client_secret = client_secret
        self.usename = username
        auth_manager = SpotifyClientCredentials(client_id=self.client_id, 
                                                      client_secret=self.client_secret)
        self.sp = spotipy.Spotify(auth_manager=auth_manager)
    
    def search_song(self,query,off=0):
        results = self.sp.search(query, limit=50,offset=off,type="track")
        songList = []
        for song in results['tracks']['items']:
            songList.append(Song(song['name'], song['album']['name'], song['artists'], song['id'], song['uri']))
        return songList

    def get_playlists(self, off=0):
        results  =  self.sp.user_playlists(self.usename, limit = 50, offset = off)
        playlists = []
        for playlist in results['items']:
            playlists.append(Playlist(playlist['name'],  playlist['owner']['id'], playlist['id'], playlist['uri']))
        return playlists
    
    def get_songs_in_playlist(self, id, off = 0):
        results = self.sp.playlist_items(id,offset = off)
        songList = []
        for song in results['items']:
            songList.append(Song(song['track']['name'], song['track']['album']['name'], song['track']['artists'], song['track']['id'], song['track']['uri']))
        return songList

        

    




# playlists = sp.user_playlists('aokouassi')
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None