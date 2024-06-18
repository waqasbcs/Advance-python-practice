# Make sure to install pytube first
# pip install pytube

from pytube import Playlist

playlist_url = input('Enter Playlist URL:')
playlist = Playlist(playlist_url)

for video in playlist.videos:
    video.streams.get_highest_resolution().download()
    
    
#https://www.youtube.com/watch?v=wkmcYZPw3PdY&list=PLelGx8BAyD6aVCkNOBJ-85rYm3DdscjBX&ab_channel=PythonCoding

    


