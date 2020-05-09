import json
from spotify_client import SpotifyClient


# TODO: Think about using CMD2 if wanting to go with command line interface, could work with gui
# helper to decide if string is an integer
def checkInteger(string):
    try:
        int(string)
    except ValueError:
        return False
    return True


def run():
    # Load Credentials
    with open('creds\credentials.json') as data_file:
        data = json.load(data_file)
    AUTHTOKEN = data["spotify"]["authToken"]
    spotify_client = SpotifyClient(AUTHTOKEN)

    # user = spotify_client.get_user_profile()
    # show playlists
    list = spotify_client.get_playlists()
    print("Playlists:\n")
    for num, playlist in enumerate(list, start=1):
        print(f"{num}.\t{playlist['name']}")

    # have user select a playlist
    while True:
        # TODO: Create Static Message
        playlist_num = input("Input playlist number:\n")
        if checkInteger(playlist_num):
            num = int(playlist_num)
            if (num <= 0).__or__(num > len(list)):
                # TODO: Create Static Message
                print("Please input a valid number.")
            else:
                break
        else:
            # TODO: Create Static Message
            print("Please input a valid number.")
    playlist_id = list[int(playlist_num) - 1]

    playlist = spotify_client.get_playlist_items(playlist_id['id'], 0)
    for num, song in enumerate(playlist, start=1):
        print(f"{num}.\t{song.name}")
    song_num = input("Select Song:\n")
    song_num = int(song_num) - 1
    songRecs = spotify_client.get_song_recommendations([playlist[song_num].song_id], )
    if not songRecs:
        print("No recommendations found.")
    else:
        for num, song in enumerate(songRecs, start=1):
            print(f"{num}.\t{song.name}")
        recommendation_num = input("Select Song:\n")
        recommendation_num = int(recommendation_num) - 1
        spotify_client.add_to_queue(songRecs[recommendation_num].uri)


if __name__ == '__main__':
    run()
