import json
from spotipy_client import SpotifyClient


def run():
    #Load Credentials
    with open('creds/credentials.json') as data_file:
        data = json.load(data_file)
    CLIENT_ID = data["spotify"]["clientId"]
    CLIENT_SECRET = data["spotify"]["clientSecret"]
    USERNAME = data["spotify"]["username"]
    client = SpotifyClient(CLIENT_ID, CLIENT_SECRET, USERNAME)
    # lst = client.search_song("Say so Doja Cat")
    # lst = client.get_playlists()
    # lst = client.get_values_of_playlist("7cu6nfbH5LoaHe4Vq9fulq")
    # for i, songInfo in enumerate(lst):
    #     print("%4d %s\t %s" % (i + 1, songInfo.song.name, songInfo.danceability))

    lst = client.get_song_recommendations_no_values_single('3Dv1eDb0MEgF93GpLXlucZ')
    for i, song in enumerate(lst):
        print("%4d %s" %(i+1, song.name))

# def options():
#     print("Welcome to the Spotify Playlist Curator")
#     print('1.\t Find Song recommendations')
#     while(True):
#         option = input("Please select an option:")
#         if(checkInteger(option)):
#             num = int(option)
#             if((num<=0).__or__(num>1)):
#                 #TODO: Create Static Message
#                 print("Please input a valid number.")
#             else:
#                 break
#         else:
#             #TODO: Create Static Message
#             print("Please input a valid number.")
#     findRecommendations()


# def getValuesForSong():
#     print("NOT FINISHED")


# def findRecommendations():
#     spotify_client = SpotifyClient(AUTHTOKEN)
#     # user = spotify_client.get_user_profile()
#     # show playlists
#     list = spotify_client.get_playlists()
#     print("Playlists:\n")
#     for num, playlist in enumerate(list, start = 1):
#         print(f"{num}.\t{playlist['name']}")

#     # have user select a playlist
#     while(True):
#         #TODO: Create Static Message
#         playlistNum = input("\nInput playlist number:\n")
#         if(checkInteger(playlistNum)):
#             num = int(playlistNum)
#             if((num<=0).__or__(num>len(list)) ):
#                 #TODO: Create Static Message
#                 print("Please input a valid number.")
#             else:
#                 break
#         else:
#             #TODO: Create Static Message
#             print("Please input a valid number.")
#     playlistId = list[int(playlistNum)-1]

#     playlist = spotify_client.list_playlist_song_info(playlistId['id'], 0)
#     for num, song in enumerate(playlist, start=1):
#         print(f"{num}.\t {song.name}, {song.acousticness}")
#     # playlist = spotify_client.get_playlist_items(playlistId['id'],0)
#     # print("Songs:")
#     # for num,song in enumerate(playlist, start=1):
#     #     print(f"{num}.\t{song.name}")
#     # songNum = input("\nSelect Song:\n")
#     # songNum = int(songNum)-1
#     # songRecs = spotify_client.get_song_recommendations([playlist[songNum].song_id])
#     # print("Recommendations:")
#     # for num,song in enumerate(songRecs, start=1):
#     #     print(f"{num}.\t{song.name}")



#     # # search for songs
#     # # TODO: Create Static Message
#     # artist = input("Input artist name:\n")
#     # # TODO: Create Static Message
#     # track = input("Input track name:\n")
#     # spotify_song = spotify_client.search_song(artist, track)
#     # if spotify_song:
#     #     added_song = spotify_client.add_song_to_spotify(spotify_song.song_id)
#     #     if added_song:
#     #         print(f"Added {artist}")
#     #     added_song_playlist = spotify_client.add_song_to_playlist(spotify_song.uri,playlistId['id'])
#     #     if added_song_playlist:
#     #         # TODO: Create Static Message
#     #         print("added to playlist")

# # helper to decide if string is an integer
# def checkInteger(input):
#     try:
#         int(input)
#     except ValueError:
#         return False
#     return True

if __name__ == '__main__':
    run()
