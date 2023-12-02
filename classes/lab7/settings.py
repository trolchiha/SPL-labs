from config.settings import get_lab_settings

settings = get_lab_settings("lab7")

HISTORY_FILE_PATH = settings["history_file_path"]
JSON_FILE_PATH = settings["json_file_path"]
CSV_FILE_PATH = settings["csv_file_path"]
TXT_FILE_PATH = settings["txt_file_path"]

DEFAULT_DATA_VISUALIZATION_SETTINGS = settings["data_visualization_settings"]
DEFAULT_TABLE_FORMAT = DEFAULT_DATA_VISUALIZATION_SETTINGS["DEFAULT_TABLE_FORMAT"]
DEFAULT_COLOR = DEFAULT_DATA_VISUALIZATION_SETTINGS["DEFAULT_COLOR"]

URLS = settings["urls"]
BASE_URL = URLS["base_url"]
AUTH_URL = URLS["auth_utl"]
TOKEN_URL = URLS["token_url"]
