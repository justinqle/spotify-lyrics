import os
import sys
import spotipy
import spotipy.util as util

scope = 'user-read-currently-playing'
username = os.getenv('SPOTIFY_USERNAME')  # environment variable for Spotify username
if username is None:
    print("Please specify Spotify username in environment variable.")
    sys.exit(1)

token = util.prompt_for_user_token(username=username,
                                   scope=scope,
                                   client_id='762e2be7c3bf47fb94c4fc3aa210647f',
                                   client_secret='42b74dea41ff48ffafb7f00eb9a3aaf5',
                                   redirect_uri='http://localhost/')
spotify = spotipy.Spotify(auth=token)

print(spotify.currently_playing())
