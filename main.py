import subprocess
from pathlib import Path

from bolt.actions import bolt_socket

BASE_DIR = Path(__file__).resolve().parent

# TODO : improve run process [subprocess => ?]
def main(filename):
    subprocess.call(["python", filename])


if __name__ == "__main__":
    bolt_socket()
    main(f"{BASE_DIR}/bolt/main.py")
