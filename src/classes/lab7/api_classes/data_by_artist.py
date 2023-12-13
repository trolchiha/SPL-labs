"""
Spotify Data by Artist Module

This module provides a class for retrieving data related to a specific artist from the Spotify API.
It includes functionality to initialize an instance of the DataByArtist class, search for an artist,
retrieve albums and top tracks by the artist, and format the obtained data.
"""
import json
from requests import get, exceptions

from classes.lab7.auth.auth import get_auth_header, get_token
from classes.lab7.api_classes.artist import Artist
from classes.lab7.api_classes.album import Album
from classes.lab7.api_classes.track import Track
from shared.settings import get_lab_settings

settings = get_lab_settings("lab7")
BASE_URL = settings["urls"]["base_url"]

class DataByArtist(Artist):
    """
    A class that represents data retrieval for a specific artist.

    Attributes:
        data (list): A list to store the retrieved data.
    """

    def __init__(self):
        """
        Initializes an instance of the DataByArtist class.
        """
        self.data = []
        super().__init__()

    def init_artist(self, name):
        """
        Initializes the artist by name.

        Args:
            name (str): The name of the artist.

        Returns:
            bool: True if the artist is successfully initialized, False otherwise.
        """
        return super().init_artist(name)

    def get_albums_by_artist_json_from_api(self):
        """
        Retrieves the albums by the artist from the API.

        Returns:
            list: A list of albums in JSON format.
        """
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
      
        except exceptions.RequestException as exeption:
            print(f"Error making API request: {exeption}")
            return None

        except json.JSONDecodeError as exeption:
            print(f"Error decoding JSON response: {exeption}")
            return None

        except KeyError as exeption:
            print(f"Unexpected response format: {exeption}")
            return None

        except Exception as exeption:
            print(f"An unexpected error occurred: {exeption}")
            return None
    
    def get_albums_formatted_json(self):
        """
        Retrieves the albums by the artist in a formatted JSON format.

        Returns:
            list: A list of albums in a formatted JSON format.
        """
        json_albums = self.get_albums_by_artist_json_from_api()
        data = []
        for json_album in json_albums:
            album = Album()
            album.set_values(json_album)
            data.append(album.get_album_formatted_json())
        return data
    
    def get_top_tracks_by_artist_json_from_api(self):
        """
        Retrieves the top tracks by the artist from the API.

        Returns:
            list: A list of top tracks in JSON format.
        """
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
      
        except exceptions.RequestException as exeption:
            print(f"Error making API request: {exeption}")
            return None

        except json.JSONDecodeError as exeption:
            print(f"Error decoding JSON response: {exeption}")
            return None

        except KeyError as exeption:
            print(f"Unexpected response format: {exeption}")
            return None

        except Exception as exeption:
            print(f"An unexpected error occurred: {exeption}")
            return None

    def get_tracks_formatted_json(self):
        """
        Retrieves the top tracks by the artist in a formatted JSON format.

        Returns:
            list: A list of top tracks in a formatted JSON format.
        """
        json_tracks = self.get_top_tracks_by_artist_json_from_api()
        data = []
        
        for json_track in json_tracks:
            track = Track()
            track.set_values(json_track)
            data.append(track.get_track_formatted_json())
        return data
    