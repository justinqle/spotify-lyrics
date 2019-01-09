# spotify-lyrics
`spotify-lyrics` is a command line script that fetches lyrics for the currently playing Spotify song and displays it in the terminal.

## Setup
`spotify-lyrics` requires the following dependencies:
* [Python 3](https://www.python.org)
* [Spotipy](https://github.com/plamere/spotipy)
    * [Requests](https://github.com/requests/requests)
* [LyricsGenius](https://github.com/johnwmillr/LyricsGenius)

Additionally, for the application to properly function, you will have to specify an environment variable with your Spotify username in your `~/bash_profile`:
```
export SPOTIFY_USERNAME='username'
```

## Installation
These following instructions are primarily written for a MacOS installation.

Firstly, clone this repository and run the script:
```
git clone https://github.com/justinqle/spotify-lyrics.git
cd spotify-lyrics
python3 spotify-lyrics.py
```

The script will subsequently ask the user to copy and paste into the terminal the URL the script redirects to. Then you will have to give permission for `spotify-lyrics` to view your Spotify data.

To allow the script to be run by name without calling `python3`, give the file executable permission:
```
chmod +x spotify-lyrics.py
```

To allow the script to be run from anywhere in the terminal, copy the script into a directory specified by your system's `$PATH`.

For example, one safe way of doing this is creating a `bin/` directory in your `$HOME` directory and adding the script to that `bin/` directory.

Then, in your `~/.bash_profile`, you can add on to your `$PATH` environment variable like so:
```
export PATH="$PATH:$HOME/bin"
```

## Usage
If the script is not given executable permission, it will have to be run like this every time:
```
python3 spotify-lyrics.py
```

Additionally, if the script is not in your `$PATH`, you will have to be in the same directory as the script to run it.

However, if the script is given executable permission and is in your `$PATH`, it can be run from anywhere in the terminal simply like this:
```
spotify-lyrics.py
```

You can even rename the executable file to just say `lyrics` and call it like this:
```
lyrics
```
