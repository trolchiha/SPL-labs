from config.settings import get_lab_settings

settings = get_lab_settings("lab5")

ART_2D_PATH = settings["art_2D_path"]
ART_3D_PATH = settings["art_3D_path"]

DEFAULT_SHAPE_SETTINGS = settings["default_shape_settings"]
DEFAULT_SIZE = DEFAULT_SHAPE_SETTINGS["size"]
DEFAULT_JUSTIFY = DEFAULT_SHAPE_SETTINGS["justify"]
DEFAULT_COLOR = DEFAULT_SHAPE_SETTINGS["color"]
