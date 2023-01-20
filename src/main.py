import asyncio
import logging
from logging.handlers import TimedRotatingFileHandler

from aioredis import Redis
from aiogram import Bot, Dispatcher
from aiogram.dispatcher.fsm.storage.redis import RedisStorage

import src.config as c
import src.handlers.handlers as handlers

logger = logging.getLogger(__name__)


async def main():

    # Enable logging
    handler = TimedRotatingFileHandler(c.LOG_FILENAME, when='d', interval=1,
                                       backupCount=7, encoding=None,
                                       delay=False, utc=False, atTime=None)

    console_handler = logging.StreamHandler()

    logging.basicConfig(
        level=c.log_level,
        force=True,
        format=c.LOG_FORMAT,
        datefmt=c.LOG_DATEFMT,
        handlers=[
            handler,
            console_handler],
    )

    # Configure bot
    bot = Bot(token=c.token)
    dp = Dispatcher(
        storage=RedisStorage(
            Redis(host=c.host, port=c.port, db=c.db,
                  # username=c.username, password=c.password
                  )
        )
    )

    # Configure routers
    dp.include_router(handlers.router)

    # Start working
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.debug('Bot was stopped manually')
