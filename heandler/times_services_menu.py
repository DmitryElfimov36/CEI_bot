import requests
import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from main import db, bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboard.kb_fill import kb_fill
from keyboard.kb_null import kb_null
from keyboard.keyboard import kb_first_menu


class FSM(StatesGroup):
    fill1 = State()
    null1 = State()


@db.message_handler(text='Заполнение деклараций, заявлений, справок')
async def conducting_ts(message: types.Message):
    await bot.send_message(message.chat.id, 'Выберите интересующую услугу', reply_markup=kb_fill)


@db.message_handler(text='Нулевая отчетность')
async def recovery_ts(message: types.Message):
    await bot.send_message(message.chat.id, 'Восстановление бухгалтерского учета', reply_markup=kb_null)


@db.message_handler(text='Назад')
async def back_ts(message: types.Message):
    await bot.send_message(message.chat.id, 'Главное меню', reply_markup=kb_first_menu)


def register_handlers_time_services(db: Dispatcher):
    db.register_message_handler(conducting_ts, commands=['Ведение бухгалтерского учета'])
    db.register_message_handler(recovery_ts, commands=['Восстановление бухгалтерского учета'])
    db.register_message_handler(back_ts, commands=['Назад'])