import dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class PlatFormSetting:
    def __init__(self):
        self.token = self._get_secret()

    @classmethod
    def _get_secret(cls):
        print("cls~!!", cls.__name__)
        check = dotenv.get_key(
            dotenv_path=f"{BASE_DIR}/.env",
            key_to_get=f"{cls.__name__}",
        )
        return check
