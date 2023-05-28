import requests
import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from main import db, bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboard.keyboard import kb_first_menu
from keyboard.kb_conducting import kb_conducting
from keyboard.kb_recovery import kb_recovery
from keyboard.kb_staging import kb_staging
from keyboard.kb_staging_1c import kb_staging_1c
from keyboard.kb_correction import kb_correction
from keyboard.kb_consultation import kb_consultation


class FSM(StatesGroup):
    conducting = State()
    recovery = State()
    staging = State()
    staging_1c = State()
    correction = State()
    consultation = State()
    back = State()


@db.message_handler(text='Ведение бухгалтерского учета')
async def conducting_acc(message: types.Message):
    await bot.send_message(message.chat.id, 'Выберите интересующую услугу', reply_markup=kb_conducting)


@db.message_handler(text='Восстановление бухгалтерского учета')
async def recovery_acc(message: types.Message):
    await bot.send_message(message.chat.id, 'Восстановление бухгалтерского учета', reply_markup=kb_recovery)


@db.message_handler(text='Постановка бухгалтерского учета')
async def staging_acc(message: types.Message):
    await bot.send_message(message.chat.id, 'Постановка бухгалтерского учета', reply_markup=kb_staging)


@db.message_handler(text='Постановка учета 1С')
async def staging_1c_acc(message: types.Message):
    await bot.send_message(message.chat.id, 'Постановка учета 1С', reply_markup=kb_staging_1c)


@db.message_handler(text='Исправление ошибок')
async def correction_acc(message: types.Message):
    await bot.send_message(message.chat.id, 'Исправление ошибок', reply_markup=kb_correction)


@db.message_handler(text='Консультационные услуги')
async def consultation_acc(message: types.Message):
    await bot.send_message(message.chat.id, 'Консультационные услуги', reply_markup=kb_consultation)


@db.message_handler(text='Назад')
async def back_acc(message: types.Message):
    await bot.send_message(message.chat.id, 'Главное меню', reply_markup=kb_first_menu)


def register_handlers_accounting(db: Dispatcher):
    db.register_message_handler(conducting_acc, commands=['Ведение бухгалтерского учета'])
    db.register_message_handler(recovery_acc, commands=['Восстановление бухгалтерского учета'])
    db.register_message_handler(staging_acc, commands=['Постановка бухгалтерского учета'])
    db.register_message_handler(staging_1c_acc, commands=['Постановка учета 1С'])
    db.register_message_handler(correction_acc, commands=['Исправление ошибок'])
    db.register_message_handler(consultation_acc, commands=['Консультационные услуги'])
    db.register_message_handler(back_acc, commands=['Назад'])
