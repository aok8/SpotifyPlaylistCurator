import requests
import urllib.parse

class Song(object):
    def __init__(self, name, song_id, uri):
        self.name = name
        self.song_id = song_id;
        self.uri = uri

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
                "Authorization" : f"Bearer {self.api_token}"
            }
        )
        response_json = response.json()
        results = response_json['tracks']['items']
        if results:
            song = Song(results[0]['name'],results[0]['id'], results[0]['uri'])
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
                "uris" : [uri]
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
    def get_playlist_items(self, playlist_id):
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        response = requests.get(
            url,
            params={
                "limit": 50
            },
            headers={
                "Authorization": f"Bearer {self.api_token}"
            }
        )
        json = response.json()
        results = json['items']
        songList = []
        for item in results:
            track = item['track']
            songList.append(
                Song(track['name'], track['id'], track['uri'])
            )
        return songList
