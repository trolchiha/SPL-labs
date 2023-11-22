import json
from requests import get, exceptions

from data.lab7.auth.auth import get_auth_header, get_token
from data.lab7.api_classes.artist import Artist
from data.lab7.api_classes.track import Track

class Recommendation():
    def __init__(self, limit=5, seed_artists=None, seed_genres=None, seed_tracks=None):
        self.limit = limit
        self.seed_artists = seed_artists
        self.seed_genres = seed_genres
        self.seed_tracks = seed_tracks

    def get_track_recommendation_json_from_api(self):
        try:
            url = self.form_url()
            token = get_token()
            headers = get_auth_header(token)
            result = get(url, headers=headers)
            json_result = json.loads(result.content)["tracks"]
            if not json_result:
                print("No track recommendation...")
                return None
            return json_result
        except exceptions.RequestException as e:
            print(f"Error making API request: {e}")
            return None

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON response: {e}")
            return None

        except KeyError as e:
            print(f"Unexpected response format: {e}")
            return None

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
    
    def get_track_recommendation_formatted_json(self):
        json_tracks = self.get_track_recommendation_json_from_api()
        data = []
        
        for json_track in json_tracks:
            track = Track()
            track.set_values(json_track)
            data.append(track.get_track_formatted_json())
        
        return data

    def get_seed_artists_id(self):
        artists_ids = []
        for artist in self.seed_artists:
            obj = Artist()
            obj.init_artist(artist)
            if obj.id is not None:
                artists_ids.append(obj.id)

        return artists_ids
    
    def get_seed_tracks_id(self):
        tracks_ids = []
        for track in self.seed_tracks:
            obj = Track()
            obj.init_track(track)
            if obj.id is not None:
                tracks_ids.append(obj.id)

        return tracks_ids
    
    def form_url(self): 
        url = f"https://api.spotify.com/v1/recommendations?limit={self.limit}"
        if self.seed_artists:
            url += "&seed_artists="
            artists_ids = self.get_seed_artists_id()
            url += self.add_item_to_url(artists_ids)
        if self.seed_genres:
            url += "&seed_genres="
            url += self.add_item_to_url(self.seed_genres)
        if self.seed_tracks:
            url += "&seed_tracks="
            tracks_id = self.get_seed_tracks_id()
            url += self.add_item_to_url(tracks_id)
        return url

    def add_item_to_url(self, items):
        url_part = ""
        if items is None:
            return url_part
        
        for idx in range(len(items)):
            if idx == len(items) - 1:
                url_part +=  str(items[idx])
            else:
                url_part +=  str(items[idx]) + "%2C"
        
        return url_part
    
