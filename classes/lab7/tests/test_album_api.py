import unittest
from data.lab7.api_classes.album import Album

class TestAlbumClass(unittest.TestCase):

    def setUp(self):
        self.album = Album()

    def test_successful_request(self):
        album_name = 'master of puppets'
        result = self.album.get_album_json_from_api(album_name)
        self.assertEqual(result['artists'][0]["name"], 'Metallica')
  
    def test_no_album_found(self):
        result = self.album.get_album_json_from_api('x5vs5ds20')
        self.assertIsNone(result)

