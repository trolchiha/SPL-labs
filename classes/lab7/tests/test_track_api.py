import unittest
from data.lab7.api_classes.track import Track

class TestTrackClass(unittest.TestCase):

    def setUp(self):
        self.track = Track()

    def test_successful_request(self):
        track_name = 'I want to break free - remastered 2011'
        track_artist_name = "Queen"
        track_album_name = "the works (deluxe remastered version)"
        result = self.track.get_track_json_from_api(track_name)
        self.assertEqual(result['name'].lower(), track_name.lower())
        self.assertEqual(result['artists'][0]["name"].lower(), track_artist_name.lower())
        self.assertEqual(result['album']["name"].lower(), track_album_name.lower())
  
    def test_no_track_found(self):
        result = self.track.get_track_json_from_api('x5vs5ds20')
        self.assertIsNone(result)

