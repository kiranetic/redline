from pathlib import Path
from decouple import config


BASE_DIR = Path(__file__).resolve().parent.parent

LOG_DIR = BASE_DIR / "logs"
LOG_FILE_NAME = config("LOG_FILE_NAME", "app.log")
LOG_LEVEL = config("LOG_LEVEL", "INFO")

LOG_FILE_PATH = LOG_DIR / LOG_FILE_NAME

MAX_RERUNS = config("MAX_RERUNS", default=2, cast=int)

