from config.settings import get_lab_settings

settings = get_lab_settings("lab1")

HISTORY_PATH = settings["history_path"]
DECIMAL_PLACES = settings["decimal_places"]