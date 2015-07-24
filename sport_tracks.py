import requests
from requests_oauthlib import OAuth2Session
from oauthlib import oauth2

def get_activities():
    client_id = "<your client key>"
    client_secret = "<your client secret>"

    token_url = 'https://github.com/login/oauth/access_token'

    sport_tracks_auth_url = "https://api.sporttracks.mobi/oauth2/authorize"

    sport_tracks_url = " https://api.sporttracks.mobi/api/v2/"
    default_parameters = {'api_key': '5649d896a3612b8869d799019e658b5a', 'user': 'PrescottGagnon', 'format': 'json'}

#    oauth = OAuth2Session(client_id=client_id,client=oauth2.Client.)



