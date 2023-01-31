from pathlib import Path
from typing import Optional

import dotenv

BASE_DIR = Path(__file__).resolve().parent


class PlatFormSetting:
    def __init__(
        self,
    ):
        self.token = self._get_secret()

    @classmethod
    def _get_secret(cls, database_name: Optional[str] = None):

        class_name = cls.__name__
        if database_name:
            class_name += f"_{database_name}"
        secret_key = dotenv.get_key(
            dotenv_path=f"{BASE_DIR}/.env",
            key_to_get=f"{class_name}",
        )
        return secret_key

    def get_database_id(self, database_name):
        db_id = self._get_secret(database_name=database_name)
        return db_id
