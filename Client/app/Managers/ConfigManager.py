import json
import os


class ConfigManager:
    _instance = None

    _app_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    _settings_file = os.path.join(_app_dir, "settings.json")

    _default_settings = {
        "api_url" : "http://localhost:5000"
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "settings"):
            self.settings = self.load_settings()

    def load_settings(self):
        if not os.path.exists(self._settings_file):
            self.save_settings(self._default_settings)

        try:
            with open(self._settings_file, "r") as f:
                return json.load(f)
        except(json.JSONDecodeError, IOError):
            return self._default_settings.copy()

    def save_settings(self, new_settings=None):
        if new_settings:
            self.settings = new_settings.copy()
        with open(self._settings_file, "w") as f:
            json.dump(self.settings, f, indent=4)

    def get(self, key):
        return self.settings.get(key, self._default_settings.get(key))

    def set(self, key, value):
        self.settings[key] = value
        self.save_settings()