import json
from spotify_client import SpotifyClient
#TODO: Think about using CMD2 if wanting to go with command line interface, could work with gui

def run():
    #Load Credentials
    with open('creds\credentials.json') as data_file:
        data = json.load(data_file)
    AUTHTOKEN = data["spotify"]["authToken"]
    spotify_client = SpotifyClient(AUTHTOKEN)

    # user = spotify_client.get_user_profile()
    # show playlists
    list = spotify_client.get_playlists()
    print("Playlists:\n")
    for num, playlist in enumerate(list, start = 1):
        print(f"{num}.\t{playlist['name']}")

    # have user select a playlist
    while(True):
        #TODO: Create Static Message
        playlistNum = input("Input playlist number:\n")
        if(checkInteger(playlistNum)):
            num = int(playlistNum)
            if((num<=0).__or__(num>len(list)) ):
                #TODO: Create Static Message
                print("Please input a valid number.")
            else:
                break
        else:
            #TODO: Create Static Message
            print("Please input a valid number.")
    playlistId = list[int(playlistNum)-1]


    playlist = spotify_client.get_playlist_items(playlistId['id'],0)
    for num,song in enumerate(playlist, start=1):
        print(f"{num}.\t{song.name}")
    songNum = input("Select Song:\n")
    songNum = int(songNum)-1
    songRecs = spotify_client.get_song_recommendations([playlist[songNum].song_id])
    for num,song in enumerate(songRecs, start=1):
        print(f"{num}.\t{song.name}")



    # # search for songs
    # # TODO: Create Static Message
    # artist = input("Input artist name:\n")
    # # TODO: Create Static Message
    # track = input("Input track name:\n")
    # spotify_song = spotify_client.search_song(artist, track)
    # if spotify_song:
    #     added_song = spotify_client.add_song_to_spotify(spotify_song.song_id)
    #     if added_song:
    #         print(f"Added {artist}")
    #     added_song_playlist = spotify_client.add_song_to_playlist(spotify_song.uri,playlistId['id'])
    #     if added_song_playlist:
    #         # TODO: Create Static Message
    #         print("added to playlist")

# helper to decide if string is an integer
def checkInteger(input):
    try:
        int(input)
    except ValueError:
        return False
    return True

if __name__ == '__main__':
    run()
