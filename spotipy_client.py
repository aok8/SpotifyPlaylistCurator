import requests
import urllib.parse
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

scope = "ugc-image-upload user-read-recently-played user-top-read user-read-playback-position user-read-playback-state user-modify-playback-state user-read-currently-playing app-remote-control streaming playlist-modify-public playlist-modify-private playlist-read-private playlist-read-collaborative user-follow-modify user-follow-read user-library-modify user-library-read user-read-email user-read-private"

redirect_uri = "https://localhost:8080"

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
        # self.sp = spotipy.Spotify(auth_manager=auth_manager)
        self.sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(scope=scope, client_id =self.client_id, client_secret =self.client_secret, redirect_uri = 'https://localhost:8080'))
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

    def get_song(self, id):
        result = self.sp.track(id)
        song = Song(
                result['name'],
                result['album']['name'],
                result['artists'],
                result['id'],
                result['uri'],
            )
        return song

    def get_values_of_songs(self, song_list):
        if not isinstance(song_list, list): song_list = [song_list]
        id_list = []
        for song in song_list:
            id_list.append(song.song_id)
        features = self.sp.audio_features(id_list)
        info = []
        for info_set, song in zip(features,song_list):
            info.append(SongInfo(
                song, 
                info_set['acousticness'],
                info_set['danceability'],
                info_set['energy'],
                info_set['instrumentalness'],
                info_set['liveness'],
                info_set['loudness'],
                info_set['valence'],
            ))
        return info

    def get_values_of_playlist(self, id, off =0):
        song_list = self.get_songs_in_playlist(id, off)
        value_list = self.get_values_of_songs(song_list)
        return value_list
    
    def get_song_recommendations_no_values_single(self,id, limit = 50):
        songList = self.sp.recommendations(seed_tracks = [id], limit = limit, target_danceability='0.7', target_energy='0.6',target_liveness='0.1')
        recommendations = []
        for song in songList['tracks']:
             recommendations.append(Song(song['name'], song['album']['name'], song['artists'], song['id'], song['uri']))
        return recommendations

    def add_song_to_queue(self, id, device_id=None):
        self.sp.add_to_queue(id,device_id)

    def add_song_list_to_queue(self, id_list, device_id=None):
        for song in id_list:
            self.add_song_to_queue(song, device_id)
    