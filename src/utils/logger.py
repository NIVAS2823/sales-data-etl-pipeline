import logging
from pathlib import Path
from config.settings import settings


def get_logger(name: str) -> logging.Logger:
    """
    Creates and returns a configured logger instance.
    Logs to both console and a file, using the log level defined in .env.
    """
    logger = logging.getLogger(name)

    # Prevent adding duplicate handlers if get_logger() is called multiple times
    if logger.handlers:
        return logger

    logger.setLevel(settings.log_level)

    # Ensure the logs directory exists before writing to it
    settings.log_file.parent.mkdir(parents=True, exist_ok=True)

    # Common format for both handlers
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Console handler — for real-time visibility during development
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File handler — for persistent, reviewable logs
    file_handler = logging.FileHandler(settings.log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger