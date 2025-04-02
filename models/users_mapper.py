from models.users import User



# Konvertira User objekt u json i iz json formata kreira User objekt
class UserMapper:

    def from_json(self, user_json: str) -> User:
        if isinstance(user_json, dict):
            pass
        else:
            return User()

    def to_json(self) -> str:
        pass
