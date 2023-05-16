from aiogram import types, Dispatcher
import aiogram.utils.markdown as md
from main import bot, db
from keyboard import keyboard
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


async def bot_start(message: types.Message):
    await bot.send_message(message.chat.id, md.text("Здравствуйте! Выберите интересующую категорию"), reply_markup=keyboard.kb_client)


def register_handlers_start(db: Dispatcher):
    db.register_message_handler(bot_start)
