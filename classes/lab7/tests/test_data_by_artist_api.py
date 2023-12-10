"""
Module: test_data_by_artist

This module contains unit tests for the DataByArtist class.

Classes:
    TestDataByArtistClass:
        This class contains unit tests for the DataByArtist class.

Methods:
    - setUp(self): Set up the test case by initializing an instance of DataByArtist and setting the artist to "Nirvana".
    - test_successful_request_top_tracks(self): Test the successful request for top tracks by the artist.
    - test_successful_request_artist_albums(self): Test the successful request for artist albums.
"""
import unittest
from classes.lab7.api_classes.data_by_artist import DataByArtist

class TestDataByArtistClass(unittest.TestCase):
    """
    This class contains unit tests for the DataByArtist class.
    """

    def setUp(self):
        """
        Set up the test case by initializing an instance of DataByArtist and setting the artist to "Nirvana".
        """
        self.artist = DataByArtist()
        self.artist.init_artist("Nirvana")

    def test_successful_request_top_tracks(self):
        """
        Test the successful request for top tracks by the artist.
        """
        num_of_tracks = 10
        result = self.artist.get_tracks_formatted_json()
        self.assertEqual(len(result), num_of_tracks)

    def test_successful_request_artist_albums(self):
        """
        Test the successful request for artist albums.
        """
        num_of_albums = 10
        result = self.artist.get_tracks_formatted_json()
        self.assertEqual(len(result), num_of_albums)
