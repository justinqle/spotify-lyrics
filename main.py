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

token = util.prompt_for_user_token(username=username,
                                   scope=scope,
                                   client_id='762e2be7c3bf47fb94c4fc3aa210647f',
                                   client_secret='42b74dea41ff48ffafb7f00eb9a3aaf5',
                                   redirect_uri='http://localhost/')
spotify = spotipy.Spotify(auth=token)  # Spotipy API wrapper

playing = spotify.currently_playing()
name = playing['item']['name']
artist = playing['item']['artists'][0]['name']

genius = lyricsgenius.Genius('H5mBdF6qCxfIjMFXY8pTFw-0vxFInPmJyJdpzF0Wc5sxEE7ECS4RikIrhv1JoDA_')  # Genius API wrapper
song = genius.search_song(name, artist)
print()
print(song.lyrics)
