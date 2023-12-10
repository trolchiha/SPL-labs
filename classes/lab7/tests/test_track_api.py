"""
Module: test_track_class

This module contains unit tests for the Track class.

Classes:
    TestTrackClass:
        A test case for the Track class.

Methods:
    - setUp(self): Set up the test case by creating an instance of the Track class.
    - test_successful_request(self): Test a successful request to get track information from the API.
    - test_no_track_found(self): Test the case where no track is found in the API.
"""
import unittest
from classes.lab7.api_classes.track import Track

class TestTrackClass(unittest.TestCase):
    """
    A test case for the Track class.
    """

    def setUp(self):
        """
        Set up the test case by creating an instance of the Track class.
        """
        self.track = Track()

    def test_successful_request(self):
        """
        Test a successful request to get track information from the API.
        """
        track_name = 'I want to break free - remastered 2011'
        track_artist_name = "Queen"
        track_album_name = "the works (deluxe remastered version)"
        result = self.track.get_track_json_from_api(track_name)
        self.assertEqual(result['name'].lower(), track_name.lower())
        self.assertEqual(result['artists'][0]["name"].lower(), track_artist_name.lower())
        self.assertEqual(result['album']["name"].lower(), track_album_name.lower())
  
    def test_no_track_found(self):
        """
        Test the case where no track is found in the API.
        """
        result = self.track.get_track_json_from_api('x5vs5ds20')
        self.assertIsNone(result)
