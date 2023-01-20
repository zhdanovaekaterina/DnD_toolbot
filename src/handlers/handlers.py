import logging

from aiogram import Router, F
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.dispatcher.filters import Command

import src.config as c

logger = logging.getLogger(__name__)
router = Router()
router.message.filter(F.chat.type == "private")


@router.message(Command(commands=['start']))
async def start(event: Message,
                state: FSMContext
                ):
    await event.answer('Введите ваше имя:')


@router.message(Command(commands=['name']))
async def name_command(event: Message,
                       state: FSMContext
                       ):
    data = await state.get_data()
    name = data.get('name', False)
    message = f'Ваше имя - {name}' if name else 'Я не знаю как вас зовут...'
    await event.answer(message)


@router.message()
async def input_proceed(event: Message,
                        state: FSMContext
                        ):
    await state.update_data(name=event.text)
    await event.answer(f'Ваше имя - {event.text}')
