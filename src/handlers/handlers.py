from aiogram import Router, F
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.dispatcher.filters import Command

import src.config as c

router = Router()
router.message.filter(F.chat.type == "private")


@router.message(Command(commands=['start']))
async def start(message: Message):
    await message.answer('Введите ваше имя:')
