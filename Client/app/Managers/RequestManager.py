from Client.app.Managers.ConfigManager import ConfigManager
import requests


def set_request(url, endpoint):
    return requests.get(url + endpoint)
