import json
from requests import get

from data.lab7.auth.auth import get_auth_header, get_token
from data.lab7.api_classes.artist import Artist
from data.lab7.api_classes.album import Album
from data.lab7.api_classes.track import Track

BASE_URL = 'https://api.spotify.com/v1/'

class DataByArtist(Artist):
    def __init__(self, artist_name):
        self.data = []
        super().__init__(artist_name)

    def get_albums_by_artist_json_from_api(self):
        token = get_token()
        headers = get_auth_header(token)
        url = BASE_URL + f"artists/{self.id}/albums"
        result = get(url, headers=headers)
        json_result = json.loads(result.content)["items"]
        return json_result
    
    def get_albums_formatted_json(self):
        json_albums = self.get_albums_by_artist_json_from_api()
        data = []
        
        for album in json_albums:
            album = Album(album["name"])
            data.append(album.get_album_formatted_json())
        return data
    
    def get_top_tracks_by_artist_json_from_api(self):
        token = get_token()
        headers = get_auth_header(token)
        url = BASE_URL + f"artists/{self.id}/top-tracks?country=UA"
        result = get(url, headers=headers)
        json_result = json.loads(result.content)["tracks"]
        return json_result
    
    def get_tracks_formatted_json(self):
        json_tracks = self.get_top_tracks_by_artist_json_from_api()
        data = []
        
        for track in json_tracks:
            track = Track(track["name"])
            data.append(track.get_track_formatted_json())
        return data