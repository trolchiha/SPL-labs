from config.settings import get_lab_settings

settings = get_lab_settings("lab8")

CSV_FILE_PATH = settings["csv_file_path"]
DIAGRAMS_DIR = settings["diagrams_dir"]
DEFAULT_YEAR = settings["default_year"]
DEFAULT_MONTH = settings["default_month"]