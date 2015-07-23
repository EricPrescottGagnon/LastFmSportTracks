import requests, json
import pandas

lastfm_url = "http://ws.audioscrobbler.com/2.0/"
default_parameters = {'api_key': '5649d896a3612b8869d799019e658b5a', 'user': 'PrescottGagnon', 'format': 'json'}

data = default_parameters
data['method'] = 'user.getrecenttracks'

r = requests.get(lastfm_url, params=data)
dataframe = pandas.read_json(r.content, orient='records')

print r
print dataframe.head()
