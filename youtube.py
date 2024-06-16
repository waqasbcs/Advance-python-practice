
import os
from pytube import YouTube, Playlist
from pytube.exceptions import PytubeError
import urllib.parse as urlparse
from urllib.parse import parse_qs

def download_youtube_video(video_url, download_path):
    try:
        yt = YouTube(video_url)
        print(f'Downloading video: {yt.title}')
        yt.streams.get_highest_resolution().download(output_path=download_path)
        print(f'Download complete: {os.path.join(download_path, yt.title)}')
    except PytubeError as e:
        print(f"An error occurred with pytube: {e}")

def download_youtube_playlist(playlist_url, download_path):
    try:
        playlist = Playlist(playlist_url)
        print(f'Downloading playlist: {playlist.title}')
        
        for video in playlist.videos:
            print(f'Downloading video: {video.title}')
            video.streams.get_highest_resolution().download(output_path=download_path)
        
        print('Download complete.')
        
    except KeyError as e:
        print(f"Invalid URL format: {e}. Ensure the URL is a valid YouTube playlist URL.")
    except PytubeError as e:
        print(f"An error occurred with pytube: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    input_url = input('Enter YouTube Video or Playlist URL: ')
    download_path = input('Enter the directory where you want to save the videos: ')
    
    # Ensure the download path exists
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    parsed_url = urlparse.urlparse(input_url)
    query_params = parse_qs(parsed_url.query)
    
    if 'list' in query_params:
        # It's a playlist URL
        download_youtube_playlist(input_url, download_path)
    else:
        # It's a single video URL
        download_youtube_video(input_url, download_path)
        
        
        
        
