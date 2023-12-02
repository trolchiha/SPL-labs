import unittest
from data.lab7.api_classes.data_by_artist import DataByArtist

class TestDataByArtistClass(unittest.TestCase):

    def setUp(self):
        self.artist = DataByArtist()
        self.artist.init_artist("Nirvana")

    def test_successful_request_top_tracks(self):
        num_of_tracks = 10
        result = self.artist.get_tracks_formatted_json()
        self.assertEqual(len(result), num_of_tracks)

    def test_successful_request_artist_albums(self):
        num_of_albums = 10
        result = self.artist.get_tracks_formatted_json()
        self.assertEqual(len(result), num_of_albums)

