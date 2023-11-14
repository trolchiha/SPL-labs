import json
from requests import post, get

from data.lab7.auth.auth import get_auth_header, get_token

BASE_URL = 'https://api.spotify.com/v1/'

class Artist:
    def __init__(self, name):
        self.id = None
        self.artist_name = None
        self.spotify_link = None
        self.init_artist(name)

    def __str__(self):
        return str(self.get_artist_formatted_json())
    
    def get_artist_json_from_api(self, artist_name):
        token = get_token()
        headers = get_auth_header(token)
        url = BASE_URL + "search"
        query = f"?q={artist_name}&type=artist&limit=1"

        query_url = url + query
        result = get(query_url, headers=headers)
        json_result = json.loads(result.content)["artists"]["items"]
        if len(json_result) == 0:
            print("No artist with this name exists...")
            return 
        return json_result[0]
    
    def init_artist(self, name):
        artist_json = self.get_artist_json_from_api(name)
        
        if artist_json is None:
            print("The object was not created")
            return
        
        self.id = artist_json["id"]
        self.artist_name = artist_json["name"]
        self.spotify_link = artist_json["external_urls"]["spotify"]

    def get_artist_formatted_json(self):
        return {
            'id': self.id,
            'artist_name': self.artist_name,
            'spotify_link': self.spotify_link
        }
    