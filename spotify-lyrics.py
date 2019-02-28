#!/usr/bin/env python3.7

import os
import sys
import spotipy
import spotipy.util as util
import lyricsgenius

scope = 'user-read-currently-playing'
username = os.getenv('SPOTIFY_USERNAME')  # environment variable specifying Spotify username
if username is None:
    print("Please specify Spotify username in an environment variable called SPOTIFY_USERNAME.")
    sys.exit(1)
 
# Put Spotify credentials here
client_id = ""
client_secret = ""
# Put Genius API key
api_key = ""

token = util.prompt_for_user_token(username=username,
                                   scope=scope,
                                   client_id=client_id,
                                   client_secret=client_secret,
                                   redirect_uri='http://localhost/')
spotify = spotipy.Spotify(auth=token)  # Spotipy API wrapper

playing = spotify.currently_playing()
name = playing['item']['name']
artist = playing['item']['artists'][0]['name']

genius = lyricsgenius.Genius(api_key)  # Genius API wrapper
song = genius.search_song(name, artist)
print()
print(song.lyrics)
