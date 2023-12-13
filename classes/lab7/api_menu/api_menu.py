"""
Spotify API Menu Module

This module provides a command-line interface for interacting with the Spotify API.
It includes a menu system with options to search for artists, tracks, and albums,
retrieve artist-related information, get recommendations, manage user history,
and save or print the obtained data in different formats.
"""
from UI.menu import Menu
from UI.menu_item import Item
from shared.history import History
from shared.settings import get_lab_settings
from classes.lab7.api_classes.artist import Artist
from classes.lab7.api_classes.album import Album
from classes.lab7.api_classes.track import Track
from classes.lab7.api_classes.data_by_artist import DataByArtist
from classes.lab7.data_manupulation.data_saver import DataSaver
from classes.lab7.data_manupulation.data_visualization import DataVisualization
from classes.lab7.data_manupulation.data_from_console import get_name, get_user_input_recommendations
from classes.lab7.api_classes.recommendation import Recommendation
import classes.lab7.tests.main as tests

settings = get_lab_settings("lab7")
HISTORY_FILE_PATH = settings["history_file_path"]

class APIMenu:
    """
    A class representing the API Menu for Spotify API.

    Attributes:
    - data: The data obtained from API calls.
    - history: An instance of the History class to manage user history.
    - data_visualization: An instance of the DataVisualization class to visualize data.
    """

    def __init__(self):
        """
        Initializes an instance of APIMenu.

        This method sets up the initial state of the object, including:
        - Setting `data` attribute to None.
        - Initializing the `history` attribute with an instance of the History class,
          loading historical data from the specified file path.
        - Initializing the `data_visualization` attribute with an instance of the DataVisualization class.

        Parameters:
        None

        Returns:
        None
        """
        self.data = None
        self.history = History(HISTORY_FILE_PATH)
        self.data_visualization = DataVisualization()

    def menu(self):
        """
        Displays the Spotify API menu and allows the user to navigate through different options.
        """
        menu = Menu("\nSpotify API Menu")
        menu.set_color("green")
        menu.add_item(Item("1", "Search Menu", self.search_menu))
        menu.add_item(Item("2", "Artist Menu", self.player_menu))
        menu.add_item(Item("3", "History Menu", self.history_menu))
        menu.add_item(Item("4", "Tests", tests.__main__))
        menu.add_item(Item("0", "Exit", ))
        menu.run()

    def history_menu(self):
        """
        Displays a menu for interacting with the history feature.

        This method creates a menu with options to view and clear history.
        The user's choice triggers corresponding actions and updates the program state.

        Parameters:
        None

        Returns:
        None
        """
        history_menu = Menu("\nHistory Menu")
        history_menu.set_color("green")
        history_menu.add_item(Item("1", "View History", self.history.print_history))
        history_menu.add_item(Item("2", "Clear History", self.history.clear_history))
        history_menu.add_item(Item("0", "Back"))
        history_menu.run()

    def search_menu(self):
        """
        Displays a menu for searching artists, tracks, and albums.

        This method creates a menu with options to search for artists, tracks, and albums.
        User choices trigger specific search functions and update the program state.

        Parameters:
        None

        Returns:
        None
        """
        search_menu = Menu("\nSearch Menu")
        search_menu.set_color("green")
        search_menu.add_item(Item("1", "Search Artist", self.search_artist))
        search_menu.add_item(Item("2", "Search Track", self.search_track))
        search_menu.add_item(Item("3", "Search Album", self.search_album))
        search_menu.add_item(Item("0", "Back"))
        search_menu.run()

    def search_artist(self):
        """
        Searches for an artist and updates the program state with the artist's information.

        This method prompts the user to enter an artist's name and retrieves information about the artist.
        The artist's data is formatted and stored, and the action is logged in the history.

        Parameters:
        None

        Returns:
        None
        """
        artist_name = get_name("artist")
        artist = Artist()
        artist.init_artist(artist_name)
        self.data = artist.get_artist_formatted_json()
        self.history.add_event(f"Get Artist {artist_name}")
        self.choose_menu()

    def search_track(self):
        """
        Searches for a track and updates the program state with the track's information.

        This method prompts the user to enter a track's name and retrieves information about the track.
        The track's data is formatted and stored, and the action is logged in the history.

        Parameters:
        None

        Returns:
        None
        """
        track_name = get_name("track")
        track = Track()
        track.init_track(track_name)
        self.data = track.get_track_formatted_json()
        self.history.add_event(f"Get Track {track_name}")
        self.choose_menu()

    def search_album(self):
        """
        Searches for an album and updates the program state with the album's information.

        This method prompts the user to enter an album's name and retrieves information about the album.
        The album's data is formatted and stored, and the action is logged in the history.

        Parameters:
        None

        Returns:
        None
        """
        album_name = get_name("album")
        album = Album()
        album.init_album(album_name)
        self.data = album.get_album_formatted_json()
        self.history.add_event(f"Get Album {album_name}")
        self.choose_menu()  

    def player_menu(self):
        """
        Displays a menu for interacting with artist-related features.

        This method creates a menu with options to get an artist's top tracks, albums, and recommendations.
        User choices trigger specific actions related to artists and update the program state.

        Parameters:
        None

        Returns:
        None
        """
        player_menu = Menu("\nArtist Menu")
        player_menu.set_color("green")
        player_menu.add_item(Item("1", "Get Artist's Top Tracks", self.get_artist_top_tracks))
        player_menu.add_item(Item("2", "Get Artist's Albums", self.get_artist_albums))
        player_menu.add_item(Item("3", "Get Recommendations", self.get_recommendations))
        player_menu.add_item(Item("0", "Back"))
        player_menu.run()

    def get_recommendations(self):
        """
        Retrieves track recommendations based on user input and updates the program state.

        This method prompts the user for input, generates track recommendations, and stores the recommendations.
        The action is logged in the history.

        Parameters:
        None

        Returns:
        None
        """
        user_input = get_user_input_recommendations()
        user_rec = Recommendation(seed_artists=user_input.get("artist"), seed_genres=user_input.get("genre"), seed_tracks=user_input.get("track"))
        self.data = user_rec.get_track_recommendation_formatted_json()
        self.history.add_event("Get recommendations")
        self.choose_menu()

    def get_artist_top_tracks(self):
        """
        Retrieves an artist's top tracks and updates the program state.

        This method prompts the user to enter an artist's name, retrieves the top tracks,
        and stores the tracks' data. The action is logged in the history.

        Parameters:
        None

        Returns:
        None
        """
        artist_name = get_name("artist")
        artist = DataByArtist()
        artist.init_artist(artist_name)
        self.data = artist.get_tracks_formatted_json()
        self.history.add_event(f"Get {artist_name} Top Tracks")
        self.choose_menu()

    def get_artist_albums(self):
        """
        Retrieves an artist's albums and updates the program state.

        This method prompts the user to enter an artist's name, retrieves the albums,
        and stores the albums' data. The action is logged in the history.

        Parameters:
        None

        Returns:
        None
        """
        artist_name = get_name("artist")
        artist = DataByArtist()
        artist.init_artist(artist_name)
        self.data = artist.get_albums_formatted_json()
        self.history.add_event(f"Get {artist_name} Albums")
        self.choose_menu()

    def choose_menu(self):
        """
        Displays a menu for choosing between printing, saving, or going back.

        This method creates a menu with options to print, save, or go back to the previous menu.
        User choices trigger specific actions and update the program state.

        Parameters:
        None

        Returns:
        None
        """
        choose_menu = Menu("\nPrint or Save")
        choose_menu.set_color("green")
        choose_menu.add_item(Item("1", "Print", self.print_menu))
        choose_menu.add_item(Item("2", "Save", self.save_menu))
        choose_menu.add_item(Item("0", "Back"))
        choose_menu.run()

    def save_menu(self):
        """
        Displays a menu for saving data in different formats.

        This method creates a menu with options to save data in JSON, CSV, or TXT formats.
        User choices trigger specific saving actions.

        Parameters:
        None

        Returns:
        None
        """
        save_menu = Menu("\nSave Menu")
        save_menu.set_color("green")
        save_menu.add_item(Item("1", "Save JSON", self.save_json))
        save_menu.add_item(Item("2", "Save CSV", self.save_csv))
        save_menu.add_item(Item("3", "Save TXT", self.save_txt))
        save_menu.add_item(Item("0", "Back", self.choose_menu))
        save_menu.run()

    def save_json(self):
        """
        Saves the current data to a JSON file.

        This method initializes a DataSaver object with the current data and
        triggers the save_to_json method to save the data in JSON format.

        Parameters:
        None

        Returns:
        None
        """
        data_saver = DataSaver(self.data)
        data_saver.save_to_json()

    def save_csv(self):
        """
        Saves the current data to a CSV file.

        This method initializes a DataSaver object with the current data and
        triggers the save_to_csv method to save the data in CSV format.

        Parameters:
        None

        Returns:
        None
        """
        data_saver = DataSaver(self.data)
        data_saver.save_to_csv()

    def save_txt(self):
        """
        Saves the current data to a TXT file.

        This method initializes a DataSaver object with the current data and
        triggers the save_to_txt method to save the data in TXT format.

        Parameters:
        None

        Returns:
        None
        """
        data_saver = DataSaver(self.data)
        data_saver.save_to_txt()

    def print_menu(self):
        """
        Displays a menu for printing data.

        This method creates a menu with options to print data as a table, list, view settings, or change color.
        User choices trigger specific print or settings actions.

        Parameters:
        None

        Returns:
        None
        """
        print_menu = Menu("\nPrint Menu")
        print_menu.set_color("green")
        print_menu.add_item(Item("1", "Print Table", self.print_table))
        print_menu.add_item(Item("2", "Print List", self.print_list))
        print_menu.add_item(Item("3", "Settings", self.settings_menu))
        print_menu.add_item(Item("0", "Back", self.choose_menu))
        print_menu.run()

    def print_table(self):
        """
        Prints the current data as a table.

        This method sets the data for visualization, and then triggers the visualization
        of the data in table format using the DataVisualization class.

        Parameters:
        None

        Returns:
        None
        """
        self.data_visualization.set_data(self.data)
        self.data_visualization.visualize_as_table()

    def print_list(self):
        """
        Prints the current data as a list.

        This method sets the data for visualization, and then triggers the visualization
        of the data in list format using the DataVisualization class.

        Parameters:
        None

        Returns:
        None
        """
        self.data_visualization.set_data(self.data)
        self.data_visualization.visualize_as_list()

    def settings_menu(self):
        """
        Displays a menu for managing visualization settings.

        This method creates a menu with options to view settings, change color, or go back.
        User choices trigger specific settings actions.

        Parameters:
        None

        Returns:
        None
        """
        settings_menu = Menu("\nSettings Menu")
        settings_menu.set_color("green")
        settings_menu.add_item(Item("1", "View Settings", self.print_settings))
        settings_menu.add_item(Item("2", "Change Color", self.change_color))
        settings_menu.add_item(Item("0", "Back", self.print_menu))
        settings_menu.run()

    def print_settings(self):
        """
        Displays the current application settings.

        This method retrieves and displays the current settings for visualization,
        allowing users to view and adjust the application's display settings.

        Parameters:
        None

        Returns:
        None
        """
        self.data_visualization.set_data(self.data)
        self.data_visualization.view_settings()

    def change_color(self):
        """
        Allows the user to change the color settings of the application.

        This method prompts the user to input new color preferences, which are then applied
        to the visualization components of the application.

        Parameters:
        None

        Returns:
        None
        """
        self.data_visualization.set_data(self.data)
        self.data_visualization.settings()
        