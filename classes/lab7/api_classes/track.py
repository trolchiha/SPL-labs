"""
Track Module

This module defines the Track class, which represents a track object and provides methods for retrieving
track information from the Spotify API.
"""

from shared.settings import get_lab_settings
from classes.lab7.api_classes.api_error_handling.api_error_handling import APIError, APIRequest
from classes.lab7.auth.auth import get_auth_header, get_token

settings = get_lab_settings("lab7")
BASE_URL = settings["urls"]["base_url"]

class Track:
    """
    Represents a track object.

    Attributes:
        id (str): The ID of the track.
        track_name (str): The name of the track.
        artist (dict): The information about the artist of the track.
        album (dict): The information about the album of the track.
        spotify_link (str): The Spotify link of the track.
    """

    # def __init__(self, name):
    #     """
    #     Initializes a Track object with the given name.

    #     Args:
    #         name (str): The name of the track.
    #     """
    #     self.id = None
    #     self.track_name = None
    #     self.artist = None
    #     self.album = None
    #     self.spotify_link = None
    #     self.init_track(name)

    def __init__(self):
        """
        Initializes an empty Track object.
        """
        self.id = None
        self.track_name = None
        self.artist = None
        self.album = None
        self.spotify_link = None

    def __str__(self):
        """
        Returns a formatted JSON string representation of the Track object.

        Returns:
            str: The formatted JSON string representation of the Track object.
        """
        return str(self.get_track_formatted_json())

    # def get_track_json_from_api(self, token, track_name):
    #     """
    #     Retrieves the track JSON data from the API.

    #     Args:
    #         token (str): The access token for the API.
    #         track_name (str): The name of the track.

    #     Returns:
    #         dict: The track JSON data.
    #     """
    #     try:
    #         token = get_token()
    #         headers = get_auth_header(token)
    #         url = BASE_URL + "search"
    #         query = f"?q={track_name}&type=track&limit=1"

    #         query_url = url + query
    #         result = get(query_url, headers=headers)
    #         json_result = json.loads(result.content)["tracks"]["items"]
    #         if not json_result:
    #             print("No track with this name exists...")
    #             return None
    #         return json_result[0]
    #     except exceptions.RequestException as exception:
    #         print(f"Error making API request: {exception}")
    #         return None

    #     except json.JSONDecodeError as exception:
    #         print(f"Error decoding JSON response: {exception}")
    #         return None

    #     except KeyError as exception:
    #         print(f"Unexpected response format: {exception}")
    #         return None

    #     except Exception as exception:
    #         print(f"An unexpected error occurred: {exception}")
    #         return None
    

    def get_track_json_from_api(self, track_name):
        """
        Retrieves the JSON data for a track from the API.

        Args:
            track_name (str): The name of the track.

        Returns:
            dict: The JSON data for the track, or None if the track does not exist.

        Raises:
            APIError: If there is an error with the API request.
        """
        api_request = APIRequest(BASE_URL)
        try:
            token = get_token()
            headers = get_auth_header(token)
            track_data = api_request.make_request("search", params={"q": track_name, "type": "track", "limit": 1}, headers=headers)
            if not track_data:
                print("No track with this name exists...")
                return None
            return track_data["tracks"]["items"][0]
        except APIError as api_error:
            print(f"API Error: {api_error.message}")

            
    def init_track(self, name):
        """
        Initializes the Track object with the given name.

        Args:
            name (str): The name of the track.
        """
        track_json = self.get_track_json_from_api(name)
        
        if track_json is None:
            print("The object was not created")
            return
        
        self.set_values(track_json)
        
    def set_values(self, track_json):
        """
        Sets the values of the Track object based on the track JSON data.

        Args:
            track_json (dict): The track JSON data.
        """
        self.id = track_json["id"]
        self.track_name = track_json["name"]
        artist_id = track_json["artists"][0]["id"]
        artist_name = track_json["artists"][0]["name"]
        artist_link = track_json["artists"][0]["external_urls"]["spotify"]
        self.artist = {"id": artist_id, "name": artist_name, "spotify_link": artist_link}
        album_id = track_json["album"]["id"]
        album_name = track_json["album"]["name"]
        album_link = track_json["album"]["external_urls"]["spotify"]
        self.album =  {"id": album_id, "name": album_name, "spotify_link": album_link}
        self.spotify_link = track_json["external_urls"]["spotify"]
        

    def get_track_formatted_json(self):
        """
        Returns the formatted JSON representation of the Track object.

        Returns:
            dict: The formatted JSON representation of the Track object.
        """
        return {
            'id': self.id,
            'track_name': self.track_name,
            'artist': self.artist,
            'album': self.album,
            'spotify_link': self.spotify_link
        }
    