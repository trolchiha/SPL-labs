import json
from requests import get, exceptions

from classes.lab7.auth.auth import get_auth_header, get_token
from classes.lab7.api_classes.artist import Artist
from classes.lab7.api_classes.album import Album
from classes.lab7.api_classes.track import Track
from classes.lab7.settings import BASE_URL

class DataByArtist(Artist):
    def __init__(self):
        self.data = []
        super().__init__()

    def init_artist(self, name):
        return super().init_artist(name)

    def get_albums_by_artist_json_from_api(self):
        try:
            token = get_token()
            headers = get_auth_header(token)
            url = BASE_URL + f"artists/{self.id}/albums"
            result = get(url, headers=headers)
            json_result = json.loads(result.content)["items"]
            if not json_result:
                    print("No top tracks found for this artist.")
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
    
    def get_albums_formatted_json(self):
        json_albums = self.get_albums_by_artist_json_from_api()
        data = []
        
        for json_album in json_albums:
            album = Album()
            album.set_values(json_album)
            data.append(album.get_album_formatted_json())
        return data
    
    def get_top_tracks_by_artist_json_from_api(self):
        try:
            token = get_token()
            headers = get_auth_header(token)
            url = BASE_URL + f"artists/{self.id}/top-tracks?country=UA"
            result = get(url, headers=headers)
            json_result = json.loads(result.content)["tracks"]
            
            if not json_result:
                print("No top tracks found for this artist.")
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

    def get_tracks_formatted_json(self):
        json_tracks = self.get_top_tracks_by_artist_json_from_api()
        data = []
        
        for json_track in json_tracks:
            track = Track()
            track.set_values(json_track)
            data.append(track.get_track_formatted_json())
        return data
    