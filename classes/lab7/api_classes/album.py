"""
Spotify Album Module

This module provides a class for representing albums and methods to interact with the Spotify API
to retrieve album information. It includes functionality to initialize an Album object, search for
an album by name, and obtain details such as the album's release date, artist information, and
Spotify link.
"""

from shared.settings import get_lab_settings
from classes.lab7.api_classes.api_error_handling.api_error_handling import APIError, APIRequest
from classes.lab7.auth.auth import get_auth_header, get_token

settings = get_lab_settings("lab7")
BASE_URL = settings["urls"]["base_url"]

class Album:
    """
    Represents an album.

    Attributes:
        id (str): The ID of the album.
        album_name (str): The name of the album.
        artist (dict): The artist of the album, containing the ID, name, and Spotify link.
        release_date (str): The release date of the album.
        spotify_link (str): The Spotify link of the album.
    """

    # def __init__(self, name):
    #     """
    #     Initializes an Album object.

    #     Args:
    #         name (str): The name of the album.
    #     """
    #     self.id = None
    #     self.album_name = None
    #     self.artist = None
    #     self.release_date = None
    #     self.spotify_link = None
    #     self.init_album(name)

    def __init__(self):
        """
        Initializes an empty Album object.
        """
        self.id = None
        self.album_name = None
        self.artist = None
        self.release_date = None
        self.spotify_link = None

    def __str__(self):
        """
        Returns a formatted JSON representation of the album.

        Returns:
            str: The formatted JSON representation of the album.
        """
        return str(self.get_album_formatted_json())
    
    # def get_album_json_from_api(self, album_name):
    #     """
    #     Retrieves the album JSON data from the API.

    #     Args:
    #         album_name (str): The name of the album.

    #     Returns:
    #         dict: The album JSON data.
    #     """
    #     try:
    #         token = get_token()
    #         headers = get_auth_header(token)
    #         url = BASE_URL + "search"
    #         query = f"?q={album_name}&type=album&limit=1"

    #         query_url = url + query
    #         result = get(query_url, headers=headers)
    #         json_result = json.loads(result.content)["albums"]["items"]
    #         if not json_result:
    #             print("No album with this name exists...")
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

    def get_album_json_from_api(self, album_name):
        """
        Retrieves the JSON data of an album from the API based on the album name.

        Args:
            album_name (str): The name of the album to search for.

        Returns:
            dict: The JSON data of the album, or None if no album with the given name exists.

        Raises:
            APIError: If there is an error while making the API request.
        """
            
        api_request = APIRequest(BASE_URL)
        try:
            token = get_token()
            headers = get_auth_header(token)
            album_data = api_request.make_request("search", params={"q": album_name, "type": "album", "limit": 1}, headers=headers)
            if not album_data:
                print("No album with this name exists...")
                return None
            return album_data["albums"]["items"][0]
        except APIError as api_error:
            print(f"API Error: {api_error.message}")
    
    def init_album(self, name):
        """
        Initializes the album object with the given name.

        Args:
            name (str): The name of the album.
        """
        album_json = self.get_album_json_from_api(name)
        
        if album_json is None:
            print("The object was not created")
            return
        self.set_values(album_json)
        
    def set_values(self, album_json):
        """
        Sets the values of the album object based on the album JSON data.

        Args:
            album_json (dict): The album JSON data.
        """
        self.id = album_json["id"]
        self.album_name = album_json["name"]
        self.release_date = album_json["release_date"]
        artist_id = album_json["artists"][0]["id"]
        artist_name = album_json["artists"][0]["name"]
        artist_link = album_json["artists"][0]["external_urls"]["spotify"]
        self.artist = {"id": artist_id, "name": artist_name, "spotify_link": artist_link}
        self.spotify_link = album_json["external_urls"]["spotify"]

    def get_album_formatted_json(self):
        """
        Returns a formatted dictionary representation of the album.

        Returns:
            dict: The formatted dictionary representation of the album.
        """
        return {
            'id': self.id,
            'album_name': self.album_name,
            'album_artist': self.artist,
            'release_date': self.release_date,
            'spotify_link': self.spotify_link
        }
