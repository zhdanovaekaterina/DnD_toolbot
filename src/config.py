import os
import logging
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
LOG_FILENAME = 'logs/logs.log'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'
