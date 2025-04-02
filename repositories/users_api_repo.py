from typing import List
import requests

from constants import BASE_URL
from models.users import User
from models.users_mapper import UserMapper


class UsersApiRepo:
    def __init__(self):
        self.url = f'{BASE_URL}/users'

    def get_users(self) -> List[User]:
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                user_mapper = UserMapper()
                # users = json.loads(response.text)
                users = response.json()
                # users = list(map(lambda user: user_mapper.from_json(user), users))
                # return users
                return list(map(lambda user: user_mapper.from_json(user), users))

            else:
                print(response.status_code)
                return None
        except Exception as ex:
            print(f'Dogodila se greska {ex}')
            return None


    def get_user(self, id: int) -> User:
        try:
            response = requests.get(self.url + f'/{id}')
            if response.status_code == 200:
                user_mapper = UserMapper()
                return user_mapper.from_json(response.json())
            else:
                print(response.status_code)
                return None
        except Exception as ex:
            print(f'Dogodila se greska {ex}')
            return None
