import requests
import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from main import db, bot
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSM(StatesGroup):
    price = State()
    doc = State()


@db.message_handler(text='Ведение бухгалтерского учета')
async def conducting(message: types.Message):
    await bot.send_message(message.chat.id, 'Составление декларации 3-НДФЛ - 720 руб.')


def register_handlers_search(db: Dispatcher):
    db.register_message_handler(conducting, commands=['Ведение бухгалтерского учета'])
