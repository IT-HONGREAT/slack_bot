import dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class PlatFormSetting:
    def __init__(
        self,
    ):
        self.token = self._get_secret()
        self.db_name = None
        # self.db = self._ttt_get_db(db_name=self.db_name)

        # self.temp = dotenv.get_key(
        #     dotenv_path=f"{BASE_DIR}/.env",
        #     key_to_get=f"{self._get_secret()}",
        # )

        # self.db = dotenv.get_key(
        #     dotenv_path=f"{BASE_DIR}/.env",
        #     key_to_get=f"{self._get_secret(self.db_name)}",
        # )

    # TODO db 이름 받고, 아래 함수에서 뽑을 수 있는 구조로 만들기
    @classmethod
    def _get_secret(cls, db_name=None):

        nnnnn = cls.__name__
        if db_name:
            nnnnn += f"_{db_name}"
        check = dotenv.get_key(
            dotenv_path=f"{BASE_DIR}/.env",
            key_to_get=f"{nnnnn}",
        )
        return check

    def temp_get_db_id(self, db_name):
        db_id = self._get_secret(db_name=db_name)
        print("dpdpdpdp", db_id)
        return db_id
