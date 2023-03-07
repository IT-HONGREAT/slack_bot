from slack_bolt.adapter.socket_mode import SocketModeHandler

from bolt_python.actions import actions_check
from bolt_python.app import bolt_app, slack_setting
from bolt_python.main import main_button_check

if __name__ == "__main__":
    print(
        actions_check,
        main_button_check,
    )
    SocketModeHandler(bolt_app, slack_setting.slack_app_token).start()
