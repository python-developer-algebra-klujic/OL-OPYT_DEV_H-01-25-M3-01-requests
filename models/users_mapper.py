import json
from models.users import User



# Konvertira User objekt u json i iz json formata kreira User objekt
class UserMapper:
    def from_json(self, user_json: str) -> User:
        if isinstance(user_json, dict):
            return User(
                id = user_json['id'],
                name = user_json['name'],
                email = user_json['email'],
                phone = user_json['phone']
            )
        else:
            return None

    def to_json(self, user: User) -> str:
        return json.dumps(user.__dict__)
