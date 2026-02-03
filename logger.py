# Logger Setup Module
import logging
import os

def seting_logger():  # Configure and return a logger
    try:
        os.mkdir("logs")
    except FileExistsError:
        pass

    logging.basicConfig(
        filename="logs/system.log",
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s", # Log format
        datefmt="%Y-%m-%d %H:%M:%S" # Date format
    )

    return logging
