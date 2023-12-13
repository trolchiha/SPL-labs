"""
Spotify Recommendation Module

This module provides a class for retrieving track recommendations from the Spotify API.
It includes functionality to initialize a Recommendation object, retrieve and format track recommendations,
and formulate API requests based on seed artists, genres, and tracks.
"""
import json
from requests import get, exceptions

from classes.lab7.auth.auth import get_auth_header, get_token
from classes.lab7.api_classes.artist import Artist
from classes.lab7.api_classes.track import Track

class Recommendation():
    """
    Represents a recommendation object that retrieves track recommendations from the Spotify API.

    Attributes:
        limit (int): The maximum number of track recommendations to retrieve.
        seed_artists (list): A list of seed artist names.
        seed_genres (list): A list of seed genre names.
        seed_tracks (list): A list of seed track names.
    """

    def __init__(self, limit=5, seed_artists=None, seed_genres=None, seed_tracks=None):
        """
        Initialize a Recommendation object.

        Args:
            limit (int): The maximum number of track recommendations to retrieve. Default is 5.
            seed_artists (list): A list of seed artist names. Default is None.
            seed_genres (list): A list of seed genre names. Default is None.
            seed_tracks (list): A list of seed track names. Default is None.
        """
        self.limit = limit
        self.seed_artists = seed_artists
        self.seed_genres = seed_genres
        self.seed_tracks = seed_tracks

    def get_track_recommendation_json_from_api(self):
        """
        Retrieve track recommendation JSON from the Spotify API.

        Returns:
            list: A list of track recommendation JSON objects.
        """
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
        except exceptions.RequestException as exception:
            print(f"Error making API request: {exception}")
            return None

        except json.JSONDecodeError as exception:
            print(f"Error decoding JSON response: {exception}")
            return None

        except KeyError as exception:
            print(f"Unexpected response format: {exception}")
            return None

        except Exception as exception:
            print(f"An unexpected error occurred: {exception}")
            return None
    

    def get_track_recommendation_formatted_json(self):
        """
        Retrieve formatted track recommendation JSON from the Spotify API.

        Returns:
            list: A list of formatted track recommendation JSON objects.
        """
        json_track_recommendation = self.get_track_recommendation_json_from_api()
        data = []
        
        for json_track in json_track_recommendation:
            track = Track()
            track.set_values(json_track)
            data.append(track.get_track_formatted_json())
        
        return data


    def get_seed_artists_id(self):
        """
        Get the IDs of the seed artists.

        Returns:
            list: A list of seed artist IDs.
        """
        artists_ids = []
        for artist in self.seed_artists:
            obj = Artist()
            obj.init_artist(artist)
            if obj.id is not None:
                artists_ids.append(obj.id)

        return artists_ids


    def get_seed_tracks_id(self):
        """
        Get the IDs of the seed tracks.

        Returns:
            list: A list of seed track IDs.
        """
        tracks_ids = []
        for track in self.seed_tracks:
            obj = Track()
            obj.init_track(track)
            if obj.id is not None:
                tracks_ids.append(obj.id)

        return tracks_ids

    def form_url(self): 
        """
        Formulate the URL for the Spotify API request.

        Returns:
            str: The URL for the API request.
        """
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
        """
        Add items to the URL.

        Args:
            items (list): A list of items to add to the URL.

        Returns:
            str: The URL with the added items.
        """
        url_part = ""
        if items is None:
            return url_part
        
        for idx in range(len(items)):
            if idx == len(items) - 1:
                url_part +=  str(items[idx])
            else:
                url_part +=  str(items[idx]) + "%2C"
        
        return url_part
   