"""
Artist Module

This module defines the Artist class for retrieving artist information from an API.
"""
from shared.settings import get_lab_settings
from classes.lab7.api_classes.api_error_handling.api_error_handling import APIError, APIRequest
from classes.lab7.auth.auth import get_auth_header, get_token

settings = get_lab_settings("lab7")
BASE_URL = settings["urls"]["base_url"]

class Artist:
    """
    Represents an artist and provides methods for retrieving artist information from an API.
    Attributes:
        id (str): The ID of the artist.
        artist_name (str): The name of the artist.
        spotify_link (str): The Spotify link of the artist.
    """

    def __init__(self):
        """
        Initializes an instance of the Artist class.
        """
        self.id = None
        self.artist_name = None
        self.spotify_link = None

    def __str__(self):
        """
        Returns a string representation of the Artist object.
        """
        return str(self.get_artist_formatted_json())
    
    # def get_artist_json_from_api(self, artist_name):
    #     """
    #     Retrieves the JSON data for an artist from the API.

    #     Parameters:
    #     - artist_name (str): The name of the artist.

    #     Returns:
    #     - dict: The JSON data for the artist, or None if the artist does not exist.
    #     """
    #     try:
    #         token = get_token()
    #         headers = get_auth_header(token)
    #         url = BASE_URL + "search"
    #         query = f"?q={artist_name}&type=artist&limit=1"

    #         query_url = url + query
    #         result = get(query_url, headers=headers)
    #         json_result = json.loads(result.content)["artists"]["items"]
    #         if not json_result:
    #             print("No artist with this name exists...")
    #             return None
    #         return json_result[0]
        
    #     except exceptions.RequestException as exeption:
    #         print(f"Error making API request: {exeption}")
    #         return None

    #     except json.JSONDecodeError as exeption:
    #         print(f"Error decoding JSON response: {exeption}")
    #         return None

    #     except KeyError as exeption:
    #         print(f"Unexpected response format: {exeption}")
    #         return None

    #     except Exception as exeption:
    #         print(f"An unexpected error occurred: {exeption}")
    #         return None

    def get_artist_json_from_api(self, artist_name):
        """
        Retrieves the JSON data for an artist from the API.

        Parameters:
        - artist_name (str): The name of the artist.

        Returns:
        - dict: The JSON data for the artist, or None if the artist does not exist.
        """
        api_request = APIRequest(BASE_URL)
        try:
            token = get_token()
            headers = get_auth_header(token)
            artist_data = api_request.make_request("search", params={"q": artist_name, "type": "artist", "limit": 1}, headers=headers)
            return artist_data["artists"]["items"][0]
        except APIError as api_error:
            print(f"API Error: {api_error.message}")
            return None
    
    def init_artist(self, name):
        """
        Initializes the Artist object with the data for the specified artist.

        Parameters:
        - name (str): The name of the artist.
        """
        artist_json = self.get_artist_json_from_api(name)
        
        if artist_json is None:
            print("The object was not created")
            return
        
        self.set_values(artist_json)
        

    def set_values(self, artist_json):
        """
        Sets the values of the Artist object using the provided artist JSON data.

        Parameters:
        - artist_json (dict): The JSON data for the artist.
        """
        self.id = artist_json["id"]
        self.artist_name = artist_json["name"]
        self.spotify_link = artist_json["external_urls"]["spotify"]

    def get_artist_formatted_json(self):
        """
        Returns a formatted dictionary representation of the Artist object.

        Returns:
        - dict: The formatted dictionary representation of the Artist object.
        """
        return {
            'id': self.id,
            'artist_name': self.artist_name,
            'spotify_link': self.spotify_link
        }
    