import requests
import sys
import pandas
import datetime


def clean_track_info(track):
    """Create a more compact json object out of the lastfm track json"""
    artist = track["artist"]["#text"]
    album = track["album"]["#text"]
    song = track["name"]
    if "@attr" in track.keys() and track["@attr"]["nowplaying"] == "true":
        date_listened = datetime.datetime.utcnow()
    else:
        date_str = track["date"]["#text"]
        date_listened = datetime.datetime.strptime(date_str, "%d %b %Y, %H:%M")
    return {"artist": artist, "album": album, "song": song, "date_listened": date_listened}


def get_recent_tracks():
    lastfm_url = "http://ws.audioscrobbler.com/2.0/"
    default_parameters = {'api_key': '5649d896a3612b8869d799019e658b5a', 'user': 'PrescottGagnon', 'format': 'json'}

    data = default_parameters
    data['method'] = 'user.getrecenttracks'
    data['limit'] = 200

    cleanTracks = []

    page = 1
    totalPages = sys.maxint

    while page <= totalPages:
        data['page'] = page
        page += 1

        print page - 1

        r = requests.get(lastfm_url, params=data)

        if r.status_code >= 400:
            break

        jsonData = r.json()

        totalPages = int(jsonData['recenttracks']['@attr']['totalPages'])
        jsonTracks = jsonData['recenttracks']['track']

        for v in jsonTracks:
            cleanTrack = clean_track_info(v)
            cleanTracks.append(cleanTrack)

    dataframe = pandas.DataFrame(cleanTracks)

    return dataframe
