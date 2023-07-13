import lyricsgenius
import os
from dotenv import load_dotenv
import re
# generate an api key and paste it
# https://genius.com/api-clients
load_dotenv()

genius_access_token = 'HjDCLDj-PpUHvjWEf9-9Zxmu5bg9i44EuPM6Pp_20qPlAt_7hmfbGEzmX4kHffsT'
genius = lyricsgenius.Genius(genius_access_token)

def save_lyrics(songs, artist_name, album_name):
    for i in range(len(songs
    )):
        song_title = songs[i]
        song = genius.search_song(song_title, artist_name)
        if song is not None:
            lyrics = song.lyrics
            lyrics_lines = lyrics.split('\n')[1:]  # Skip the first line
            lyrics_lines = [re.sub(r'\d+Embed$', '', line) for line in lyrics_lines]  # Remove trailing xxEmbed
            lyrics_lines = [line for line in lyrics_lines if not line.startswith('[')]  # Remove lines starting with [

            with open('data/songs/{}/{}_{}_{}.txt'.format('_'.join(artist_name.split(' ')), i+1, album_name, '-'.join(''.join(song_title.split('\'')).split(' '))), 'w') as f:
                f.writelines('\n'.join(lyrics_lines))  # Write the remaining lines to the file
        else:
            print(f"Song {song_title} not found!")


if __name__ == '__main__':
    drakeSongs = [

    "Worst Behavior",
    "Over",
    "Successful",
    "Forever",
    "Back To Back",
    "Know Yourself",
    "Pop Style",
    "I'm Upset",
    "Jumpman",
    "Gyalchester",
    "Chicago Freestyle",
    "Pain 1993",
    "Toosie Slide",
    "Laugh Now Cry Later",
    "War",
    "Life Is Good",
    "Teenage Fever",
    "Jaded",
    "Sneakin'",
    "Do Not Disturb",
    "Tuscan Leather",
    "Feel No Ways",
    "Hype",
    "Furthest Thing",
    "From Time",
    "Wu-Tang Forever",
    "5AM In Toronto",
    "Free Smoke",
    "No Tellin'",
    "Summer Sixteen",
    "Signs",
    "Omertà",
    "Lose You",
    "Portland",
    "Blem",
    "Madiba Riddim",
    "Ice Melts",
    "Can't Have Everything",
    "Glow",
    "Since Way Back",
    "Nothings Into Somethings",
    "Sacrifices",
    "KMT",
    "Do Not Disturb",
    "Desires",
    "Time Flies",
    "Landed",
    "D4L",
    "Pain 1993",
    "Losses",
    "From Florida With Love",
    "Demons",
    "War",
    "When To Say When",
    "Chicago Freestyle",
    "Not You Too",
    "Tootsie Slide",
    "Desires",
    "Time Flies",
    "Landed",
    "D4L",
    "Pain 1993",
    "Losses",
    "From Florida With Love",
    "Demons",
    "War",
    "When To Say When",
    "Chicago Freestyle",
    "Not You Too"]

    # remove duplicate songs
    taylor_swift_songs = list(dict.fromkeys(drakeSongs))


    save_lyrics(taylor_swift_songs, 'drake', '')
