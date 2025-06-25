import logging
import sys

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Create logger with default configuration and logging to console and file.

    Args:
        name (str): Logger's name (e.g. __name__)
        level (int): Level of logging (e.g. logging.DEBUG, logging.INFO)

    Returns:
        logging.Logger: Configured logger
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        # Format logów
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
            "%Y-%m-%d %H:%M:%S"
        )

        # Logi na konsolę
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        # Logi do pliku
        file_handler = logging.FileHandler("logs/pipeline.log", mode='a')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger