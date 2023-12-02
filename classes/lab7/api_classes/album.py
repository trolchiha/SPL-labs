import json
from requests import get, exceptions

from data.lab7.auth.auth import get_auth_header, get_token

BASE_URL = 'https://api.spotify.com/v1/'

class Album:
    def __init__(self, name):
        self.id = None
        self.album_name = None
        self.artist = None
        self.release_date = None
        self.spotify_link = None
        self.init_album(name)

    def __init__(self):
        self.id = None
        self.album_name = None
        self.artist = None
        self.release_date = None
        self.spotify_link = None

    def __str__(self):
        return str(self.get_album_formatted_json())
    
    def get_album_json_from_api(self, album_name):
        try:
            token = get_token()
            headers = get_auth_header(token)
            url = BASE_URL + "search"
            query = f"?q={album_name}&type=album&limit=1"

            query_url = url + query
            result = get(query_url, headers=headers)
            json_result = json.loads(result.content)["albums"]["items"]
            if not json_result:
                print("No album with this name exists...")
                return None
            return json_result[0]
        
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
    
    def init_album(self, name):
        album_json = self.get_album_json_from_api(name)
        
        if album_json is None:
            print("The object was not created")
            return
        self.set_values(album_json)
        
    def set_values(self, album_json):
        self.id = album_json["id"]
        self.album_name = album_json["name"]
        self.release_date = album_json["release_date"]
        artist_id = album_json["artists"][0]["id"]
        artist_name = album_json["artists"][0]["name"]
        artist_link = album_json["artists"][0]["external_urls"]["spotify"]
        self.artist = {"id": artist_id, "name": artist_name, "spotify_link": artist_link}
        self.spotify_link = album_json["external_urls"]["spotify"]

    def get_album_formatted_json(self):
        return {
            'id': self.id,
            'album_name': self.album_name,
            'album_artist': self.artist,
            'release_date': self.release_date,
            'spotify_link': self.spotify_link
        }
    

