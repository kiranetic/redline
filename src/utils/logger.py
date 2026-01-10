import logging
from pathlib import Path

from src.config import LOG_FILE_PATH, LOG_LEVEL


def _ensure_log_dir() -> None:
    Path(LOG_FILE_PATH).parent.mkdir(parents=True, exist_ok=True)


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    
    if logger.handlers:
        return logger
    
    _ensure_log_dir()

    logger.setLevel(LOG_LEVEL)
    logger.propagate = False  # Prevent FastAPI / uvicorn console logging

    handler = logging.FileHandler(filename=LOG_FILE_PATH, mode="a", encoding="utf-8")

    formatter = logging.Formatter(
        "{asctime} | {levelname} | {name}:{lineno} | {message}",
        style="{",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger

