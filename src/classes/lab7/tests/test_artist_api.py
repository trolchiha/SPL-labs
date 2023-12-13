"""
Module: test_artist

This module contains unit tests for the Artist class.
"""
import unittest
from classes.lab7.api_classes.artist import Artist

class TestArtistClass(unittest.TestCase):
    """
    This class contains unit tests for the Artist class.
    """

    def setUp(self):
        """
        Set up the test environment before each test case.
        """
        self.artist = Artist()

    def test_successful_request(self):
        """
        Test the successful request to get artist JSON from API.
        """
        result = self.artist.get_artist_json_from_api('Pink Floyd')
        self.assertEqual(result['name'], 'Pink Floyd')
  
    def test_no_artist_found(self):
        """
        Test the case when no artist is found in the API.
        """
        result = self.artist.get_artist_json_from_api('x5vs5ds20')
        self.assertIsNone(result)
