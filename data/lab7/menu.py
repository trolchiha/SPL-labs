from UI.menu import Menu
from UI.menu_item import Item

from data.lab7.api_classes.artist import Artist
from data.lab7.api_classes.album import Album
from data.lab7.api_classes.track import Track
from data.lab7.api_classes.data_by_artist import DataByArtist
from data.lab7.data_manupulation.data_saver import DataSaver
from data.lab7.data_manupulation.data_visualization import DataVisualization
from data.lab7.data_manupulation.data_from_console import get_name
from data.lab7.api_classes.recommendation import Recommendation

class APIMenu:
    def __init__(self):
        self.data = None
        
    def menu(self):
        menu = Menu("Spotify API Menu")
        menu.set_color("green")
        menu.add_item(Item("1", "Search Menu", self.search_menu))
        menu.add_item(Item("2", "Artist Menu", self.player_menu))
        menu.add_item(Item("0", "Exit", ))
        menu.run()

    def search_menu(self):
        search_menu = Menu("Search Menu")
        search_menu.set_color("light_green")
        search_menu.add_item(Item("1", "Search Artist", self.search_artist))
        search_menu.add_item(Item("2", "Search Track", self.search_track))
        search_menu.add_item(Item("3", "Search Album", self.search_album))
        search_menu.add_item(Item("0", "Back", self.menu))
        search_menu.run()

    def search_artist(self):
        artist_name = get_name("artist")
        artist = Artist(artist_name)
        self.data = artist.get_artist_formatted_json()
        self.choose_menu()

    def search_track(self):
        track_name = get_name("track")
        track = Track(track_name)
        self.data = track.get_track_formatted_json()
        self.choose_menu()

    def search_album(self):
        album_name = get_name("album")
        album = Album(album_name)
        self.data = album.get_album_formatted_json()
        self.choose_menu()  
   
    def player_menu(self):
        
        player_menu = Menu("Artist Menu")
        player_menu.set_color("light_green")
        player_menu.add_item(Item("1", "Get Artist's Top Tracks", self.get_artist_top_tracks))
        player_menu.add_item(Item("2", "Get Artist's Albums", self.get_artist_albums))
        # player_menu.add_item(Item("3", "Get Recommendations", ))
        player_menu.add_item(Item("0", "Back", self.menu))
        player_menu.run()

    def get_artist_top_tracks(self):
        artist_name = get_name("artist")
        artist = DataByArtist(artist_name)
        self.data = artist.get_tracks_formatted_json()
        self.choose_menu()

    def get_artist_albums(self):
        artist_name = get_name("artist")
        artist = DataByArtist(artist_name)
        self.data = artist.get_albums_formatted_json()
        self.choose_menu()

    def choose_menu(self):
        choose_menu = Menu("Print or Save")
        choose_menu.add_item(Item("1", "Print", self.print_menu))
        choose_menu.add_item(Item("2", "Save", self.save_menu))
        choose_menu.add_item(Item("0", "Back", self.menu))
        choose_menu.run()

    def save_menu(self):
        save_menu = Menu("Save Menu")
        save_menu.add_item(Item("1", "Save JSON", self.save_json))
        save_menu.add_item(Item("2", "Save CSV", self.save_csv))
        save_menu.add_item(Item("3", "Save TXT", self.save_txt))
        save_menu.add_item(Item("0", "Back", self.choose_menu))
        save_menu.run()

    def save_json(self):
        data_saver = DataSaver(self.data)
        data_saver.save_to_json()

    def save_csv(self):
        data_saver = DataSaver(self.data)
        data_saver.save_to_csv()

    def save_txt(self):
        data_saver = DataSaver(self.data)
        data_saver.save_to_txt()

    def print_menu(self):
        print_menu = Menu("Print Menu")
        print_menu.add_item(Item("1", "Print Table", self.print_table))
        print_menu.add_item(Item("2", "Print List", self.print_list))
        print_menu.add_item(Item("3", "Settings", self.print_settings))
        print_menu.add_item(Item("0", "Back", self.choose_menu))
        print_menu.run()

    def print_table(self):
        data_visualization = DataVisualization(self.data)
        data_visualization.visualize_as_table()

    def print_list(self):
        data_visualization = DataVisualization(self.data)
        data_visualization.visualize_as_list()

    def print_settings(self):
        pass