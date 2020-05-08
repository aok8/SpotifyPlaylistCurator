import json
from spotify_client import SpotifyClient


def run():
    with open('creds\credentials.json') as data_file:
        data = json.load(data_file)
    AUTHTOKEN = data["spotify"]["authToken"]
    spotify_client = SpotifyClient(AUTHTOKEN)

    # show playlists
    user = spotify_client.get_user_profile()
    list = spotify_client.get_playlists()
    print("Playlists:\n")
    for num, playlist in enumerate(list, start = 1):
        print(f"{num}.\t{playlist['name']}")
    playlistNum = input("Input playlist number:\n")
    playlistId = list[int(playlistNum)-1]
    # search for songs
    artist = input("Input artist name:\n")
    track = input("Input track name:\n")
    spotify_song = spotify_client.search_song(artist, track)
    if spotify_song:
        added_song = spotify_client.add_song_to_spotify(spotify_song.song_id)
        if added_song:
            print(f"Added {artist}")
        added_song_playlist = spotify_client.add_song_to_playlist(spotify_song.uri,playlistId['id'])
        if added_song_playlist:
            print("added to playlist")


if __name__ == '__main__':
    run()
