import dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class PlatFormSetting:
    def __init__(self, db_name=None):
        self.token = self._get_secret(**db_name)

    # TODO db 이름 받고, 아래 함수에서 뽑을 수 있는 구조로 만들기
    @classmethod
    def _get_secret(cls, db_name=None):
        add = ""
        if db_name:
            add = db_name
        check = dotenv.get_key(
            dotenv_path=f"{BASE_DIR}/.env",
            key_to_get=f"{cls.__name__}{add}",
        )
        return check
