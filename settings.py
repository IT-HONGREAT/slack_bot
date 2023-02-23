from pathlib import Path
from typing import Union

import dotenv

BASE_DIR = Path(__file__).resolve().parent

#
# class PlatFormSetting:
#     def __init__(
#         self,
#     ):
#         self.token = self._get_secret()
#
#     @classmethod
#     def _get_secret(cls, database_name: Optional[str] = None, slack_child: Optional[str] = None):
#
#         class_name = cls.__name__.upper()
#         if class_name == "NOTION" and database_name:
#             class_name += f"_{database_name}"
#         if class_name == "SLACK":
#             if slack_child:
#                 class_name += f"_{slack_child.upper()}"
#             elif not slack_child:
#                 return
#
#         secret_key = dotenv.get_key(
#             dotenv_path=f"{BASE_DIR}/.env",
#             key_to_get=f"{class_name}",
#         )
#         return secret_key
#
#     def get_database_id(self, database_name):
#
#         return self._get_secret(database_name=database_name)
#
#     def get_slack_detail_key(self, child):
#         return self._get_secret(slack_child=child)


BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"


class PlatformSetting:
    dotenv.load_dotenv(ENV_PATH)

    def __init__(self):
        self.token = self._get_secret()

    @classmethod
    def _get_secret(cls, database_name: Union[str, None] = None, slack_child: Union[str, None] = None):
        key_to_get = f"{cls.__name__.upper()}"
        print("key_to_get", key_to_get)

        if cls.__name__.upper() == "NOTION" and database_name:
            key_to_get += f"_{database_name}"
        elif cls.__name__.upper() == "SLACK" and slack_child:
            key_to_get += f"_{slack_child.upper()}"
        else:
            return None
        return dotenv.get_key(dotenv_path=ENV_PATH, key_to_get=key_to_get)

    def get_database_id(self, database_name: str) -> Union[str, None]:
        return self._get_secret(database_name=database_name)

    def get_slack_detail_key(self, child: str) -> Union[str, None]:
        return self._get_secret(slack_child=child)
