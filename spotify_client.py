import requests
import urllib.parse


class Song(object):
    def __init__(self, name, album_name, artists, song_id, uri):
        self.name = name
        self.albumName = album_name
        self.artists = artists
        self.song_id = song_id
        self.uri = uri


def build_dictionary(keys, values):
    res = {keys[i]: values[i] for i in range(len(keys))}
    result = {k: v for k, v in res.items() if v is not None}
    return result


class SpotifyClient(object):
    def __init__(self, api_token):
        self.api_token = api_token

    def get_user_profile(self):
        url = "https://api.spotify.com/v1/me/"
        response = requests.get(
            url,
            headers={
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        json = response.json()
        return json

    def search_song(self, artist, track):
        query = urllib.parse.quote(f'{artist} {track}')
        url = f"https://api.spotify.com/v1/search?q={query}&type=track"
        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        response_json = response.json()
        results = response_json['tracks']['items']
        if results:
            song = Song(
                results[0]['name'],
                results[0]['album']['name'],
                results[0]['artists'],
                results[0]['id'],
                results[0]['uri']
            )
            return song
        else:
            raise Exception(f"No song found for {artist} = {track}")

    def add_song_to_spotify(self, song_id):
        url = "https://api.spotify.com/v1/me/tracks"
        response = requests.put(
            url,
            json={
                "ids": [song_id]
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        return response.ok

    def add_song_to_playlist(self, uri, playlist_id):
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        response = requests.post(
            url,
            json={
                "uris": [uri]
            },
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_token}"

            }
        )
        return response.ok

    def get_playlists(self):
        url = "https://api.spotify.com/v1/me/playlists"
        response = requests.get(
            url,
            headers={
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        json = response.json()
        results = json['items']
        return results

    def get_playlist_items(self, playlist_id, offset):
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        response = requests.get(
            url,
            params={
                "limit": 50,
                "offset": offset
            },
            headers={
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        json = response.json()
        results = json['items']
        song_list = []
        for item in results:
            track = item['track']
            song_list.append(
                Song(
                    track['name'],
                    track['album']['name'],
                    track['artists'],
                    track['id'],
                    track['uri']
                )
            )
        return song_list

    # give list
    def get_song_recommendations(self, seed_tracks, acousticness=None, danceability=None, energy=None,
                                 instrumentalness=None, loudness=None, valence=None):
        # create lists to be made into dictionary
        keys = ["seed_tracks", "acousticness", "danceability", "energy", "instrumentalness", "loudness", "valence"]
        values = [seed_tracks, acousticness, danceability, energy, instrumentalness, loudness, valence]
        parameters = build_dictionary(keys, values)

        url = f"https://api.spotify.com/v1/recommendations"
        response = requests.get(
            url,
            params=parameters,
            headers={
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        json = response.json()
        results = json['tracks']
        song_list = []
        for track in results:
            song_list.append(
                Song(
                    track['name'],
                    track['album']['name'],
                    track['artists'],
                    track['id'],
                    track['uri']
                )
            )
        return song_list

    def get_devices(self):
        url = "https://api.spotify.com/v1/me/player/play"
        response = requests.get(
            url,
            headers={
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        return response['devices']

    def start_playback(self):
        url = "https://api.spotify.com/v1/me/player/play"
        response = requests.put(
            url,
            headers={
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        return response.ok

    def add_to_queue(self, uri):
        url = f"https://api.spotify.com/v1/me/player/queue"
        response = requests.post(
            url,
            params={
                "uri": uri
            },
            headers={
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        return response.ok
