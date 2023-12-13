"""
Module: test_album

This module contains unit tests for the Album class.
"""
import unittest
from classes.lab7.api_classes.album import Album

class TestAlbumClass(unittest.TestCase):
    """
    This class contains unit tests for the Album class.
    """

    def setUp(self):
        """
        Set up the test case by creating an instance of the Album class.
        """
        self.album = Album()

    def test_successful_request(self):
        """
        Test the successful request to get album JSON from the API.
        """
        album_name = 'master of puppets'
        result = self.album.get_album_json_from_api(album_name)
        self.assertEqual(result['artists'][0]["name"], 'Metallica')
  
    def test_no_album_found(self):
        """
        Test the case where no album is found in the API.
        """
        result = self.album.get_album_json_from_api('x5vs5ds20')
        self.assertIsNone(result)
