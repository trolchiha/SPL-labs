from config.settings import get_lab_settings

settings = get_lab_settings("lab4")

ART_PATH = settings["art_path"]

DEFAULT_ART_SETTINGS = settings["default_art_settings"]
DEFAULT_SYMBOL = DEFAULT_ART_SETTINGS["symbol"]
DEFAULT_WIDTH = DEFAULT_ART_SETTINGS["width"]
DEFAULT_HEIGHT = DEFAULT_ART_SETTINGS["height"]
DEFAULT_JUSTIFY = DEFAULT_ART_SETTINGS["justify"]
DEFAULT_COLOR = DEFAULT_ART_SETTINGS["color"]
