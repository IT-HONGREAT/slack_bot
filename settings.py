import dotenv
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent


class PlatFormSetting:
    def __init__(self, temp_purpose=None):
        self.token = self._get_secret(temp_purpose)

    def _get_secret(self, temp_purpose):

        check = dotenv.get_key(
            dotenv_path=f"{BASE_DIR}/.env",
            key_to_get=f"{temp_purpose}",
        )
        return check


test = PlatFormSetting(temp_purpose="Notion")
db = PlatFormSetting(temp_purpose="reservation_db")

print("!!", test.token)
print("dbdbd", db.token)
