import subprocess
from pathlib import Path

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from bolt.actions import bolt_socket
from bolt.app import bolt_app, slack_setting

BASE_DIR = Path(__file__).resolve().parent


# def main(filename):
#     """
#     Runs the Python script with the given filename
#     """
#     try:
#         subprocess.run(["python", str(filename)], check=True)
#     except subprocess.CalledProcessError as e:
#         print(f"Error running {filename}: {e}")


def create_app():
    app = App(
        token=slack_setting.slack_bot_token,
        signing_secret=slack_setting.slack_signing_secret,
    )
    import bolt.events

    app.add_blueprint()
    bolt_socket()
    SocketModeHandler(app, slack_setting.slack_app_token)

    return app


if __name__ == "__main__":
    create_app(bolt_app)
    # main(BASE_DIR / "bolt" / "main.py")
