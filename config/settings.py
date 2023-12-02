import json

config_file_path = 'config/init.json'

def load_config():
    try:
        with open(config_file_path, 'r') as file:
            config_data = json.load(file)
        return config_data
    except FileNotFoundError:
        print(f"Config file '{config_file_path}' not found.")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in config file: {e}")
        return {}

def get_lab_settings(lab_name):
    settings = load_config()
    return settings.get(lab_name, {})
