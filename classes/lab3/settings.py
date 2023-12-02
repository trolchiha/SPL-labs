from config.settings import get_lab_settings

settings = get_lab_settings("lab3")

ART_PATH = settings["art_path"]

DEFAULT_FIGLET_SETTINGS = settings["default_figlet_settings"]
DEFAULT_FONT = DEFAULT_FIGLET_SETTINGS["font"]
DEFAULT_WIDTH = DEFAULT_FIGLET_SETTINGS["width"]
DEFAULT_COLOR = DEFAULT_FIGLET_SETTINGS["color"]

FIGLET_FONT_SIZES = settings["figlet_font_sizes"]
