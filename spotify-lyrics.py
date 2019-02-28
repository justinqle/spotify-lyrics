#!/usr/bin/env python3.7

import os
import subprocess
import sys
import spotipy
import spotipy.util as util
import lyricsgenius

scope = 'user-read-currently-playing'
username = os.getenv('SPOTIFY_USERNAME')  # environment variable specifying Spotify username
if username is None:
    print("Please specify Spotify username in an environment variable called SPOTIFY_USERNAME.")
    sys.exit(1)
 
# Put Spotify developer credentials here
spotify_id = ""
spotify_secret = ""
# Put Genius developer credentials here
genius_access_token = ""

try:
    token = util.prompt_for_user_token(username=username,
                                       scope=scope,
                                       client_id=spotify_id,
                                       client_secret=spotify_secret,
                                       redirect_uri='http://localhost/')
except Exception:
    sys.exit(1)

spotify = spotipy.Spotify(auth=token)  # Spotipy API wrapper

try:
    playing = spotify.currently_playing()
except Exception:
    print("Network error, please verify connection.")
    sys.exit(1)

if playing is None:
    print("No song is currently playing.")
    sys.exit(1)

name = playing['item']['name']
# Song names with parentheses
name = name.split('(')[0].rstrip()
artist = playing['item']['artists'][0]['name']

genius = lyricsgenius.Genius(genius_access_token)  # Genius API wrapper
song = genius.search_song(name, artist)
if song is not None:
    rows, columns = subprocess.check_output(['stty', 'size']).decode().split()
    columns = int(columns)
    print('-' * columns)
    print(song.lyrics)
