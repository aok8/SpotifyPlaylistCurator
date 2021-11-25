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
    def song_to_string(self, songInfo, acoustic = False, dance = False, energy = False, instrumental = False, liveness = False, loudness = False, valence = False):
        response = "Song Name: %s\n" %songInfo.song.name
        if acoustic:
            response = response + ("Acousticness: %s\n" %songInfo.acousticness)
        if dance:
            response = response + "Danceability: %s\n" %songInfo.danceability
        if energy:
            response = response + "Energy: %s\n" %songInfo.energy
        if instrumental:
            response = response + "Instrumentalness: %s\n" %songInfo.instrumentalness
        if liveness:
            response = response + "Liveness: %s\n" %songInfo.liveness
        if loudness:
            response = response + "Loudness: %s\n" %songInfo.loudness
        if valence:
            response = response + "Valence: %s\n" %songInfo.valence
        return response
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

    def get_song_recommendations(self, seed_artists = None, seed_genres  = None, seed_tracks = None, limit = 20, country = None, **kwargs):
        params = dict(limit=limit)
        if seed_artists:
            params["seed_artists"] = seed_artists
        if seed_genres:
            params["seed_genres"] = seed_genres
        if seed_tracks:
            params["seed_tracks"] = seed_tracks
        if country:
            params["market"] = country

        for attribute in [
            "acousticness",
            "danceability",
            "duration_ms",
            "energy",
            "instrumentalness",
            "key",
            "liveness",
            "loudness",
            "mode",
            "popularity",
            "speechiness",
            "tempo",
            "time_signature",
            "valence",
        ]:
            for prefix in ["min_", "max_", "target_"]:
                param = prefix + attribute
                if param in kwargs:
                    params[param] = kwargs[param]
        songList = self.sp.recommendations(
            **params
        )
        recommendations = []
        for song in songList['tracks']:
            recommendations.append(Song(song['name'], song['album']['name'], song['artists'], song['id'], song['uri']))
        return recommendations

    def add_song_to_queue(self, id, device_id=None):
        self.sp.add_to_queue(id,device_id)

    def add_song_list_to_queue(self, id_list, device_id=None):
        for song in id_list:
            self.add_song_to_queue(song, device_id)

    def get_recs_and_add_to_queue(self,seed_artists = None, seed_genres  = None, seed_tracks = None, limit = 20, country = None, **kwargs):
        songlist = self.get_song_recommendations(seed_artists = seed_artists,
                                                 seed_genres  = seed_genres,
                                                 seed_tracks = seed_tracks,
                                                 limit = 20,
                                                 country = None,
                                                 **kwargs)
        song_id_list = []
        for songInfo in songlist:
            song_id_list.append(songInfo.song_id)
        self.add_song_list_to_queue(id_list=song_id_list)

    def next(self, device_id = None):
        self.sp.next_track(device_id)

    def pause(self, device_id = None):
        self.sp.pause_playback(device_id)

    def previous(self, device_id = None):
        self.sp.previous_track(device_id)

    def currently_playing(self, market = None, additional_types = None):
        return self.sp.currently_playing(market = market, additional_types = additional_types)

