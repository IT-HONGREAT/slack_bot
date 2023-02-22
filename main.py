import subprocess
from pathlib import Path

from bolt.actions import bolt_socket

BASE_DIR = Path(__file__).resolve().parent


def main(filename):
    """
    Runs the Python script with the given filename
    """
    try:
        subprocess.run(["python", str(filename)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running {filename}: {e}")


if __name__ == "__main__":
    bolt_socket()
    main(BASE_DIR / "bolt" / "main.py")
