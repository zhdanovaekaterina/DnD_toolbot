import os
import logging
from logging.handlers import TimedRotatingFileHandler
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)


token = os.getenv('TOKEN')

# Redis settings
host = os.getenv('HOST')
port = os.getenv('PORT')
db = os.getenv('DB')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

# Logging settings
log_level = logging.DEBUG
LOG_FILENAME = '../logs/logs.log'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'


def enable_logging():
    handler = TimedRotatingFileHandler(LOG_FILENAME, when='d', interval=1,
                                       backupCount=7, encoding=None,
                                       delay=False, utc=False, atTime=None)

    console_handler = logging.StreamHandler()

    logging.basicConfig(
        level=log_level,
        force=True,
        format=LOG_FORMAT,
        datefmt=LOG_DATEFMT,
        handlers=[
            handler,
            console_handler],
    )
