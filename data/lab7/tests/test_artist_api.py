import unittest
from data.lab7.api_classes.artist import Artist

class TestArtistClass(unittest.TestCase):

    def setUp(self):
        self.artist = Artist()

    def test_successful_request(self):
        result = self.artist.get_artist_json_from_api('Pink Floyd')
        self.assertEqual(result['name'], 'Pink Floyd')
  
    def test_no_artist_found(self):
        result = self.artist.get_artist_json_from_api('x5vs5ds20')
        self.assertIsNone(result)

