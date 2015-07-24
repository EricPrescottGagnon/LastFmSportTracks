import requests
import json
import pandas
import datetime

def clean_track_info(track):
    """Create a more compact json object out of the lastfm track json"""
    artist = track["artist"]["#text"]
    song = track["name"]
    if "@attr" in track.keys() and track["@attr"]["nowplaying"] == "true":
        date_listened = datetime.utcnow()
    else:
        date_str = track["date"]["#text"]
        date_listened = datetime.datetime.strptime(date_str, "%d %b %Y, %H:%M")
    return {"artist": artist, "song": song, "date_listened": date_listened}

def get_recent_tracks():
    lastfm_url = "http://ws.audioscrobbler.com/2.0/"
    default_parameters = {'api_key': '5649d896a3612b8869d799019e658b5a', 'user': 'PrescottGagnon', 'format': 'json'}

    data = default_parameters
    data['method'] = 'user.getrecenttracks'

    r = requests.get(lastfm_url, params=data)
    jsonData = json.loads(r.content)['recenttracks']['track']

    cleanTracks = []

    for v in jsonData:
        cleanTrack = clean_track_info(v)
        cleanTracks.append(cleanTrack)

    dataframe = pandas.DataFrame(cleanTracks)

    return dataframe
