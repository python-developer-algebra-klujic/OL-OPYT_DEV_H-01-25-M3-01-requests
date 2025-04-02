import json
import requests

from constants import URL


class UsersApi:
    def __init__(self):
        self.url = URL

    def get_users(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                return json.loads(response.text)
            else:
                print(response.status_code)
        except Exception as ex:
            print(f'Dogodila se greska {ex}')
