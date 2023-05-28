import requests
import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from main import db, bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboard.kb_tab_ooo import kb_tab_ooo
from keyboard.kb_tab_ip import kb_tab_ip
from keyboard.kb_audit import kb_audit
from keyboard.keyboard import kb_first_menu


class FSM(StatesGroup):
    tab_ooo1 = State()
    tab_ip1 = State()
    audit1 = State()


@db.message_handler(text='Налоговый учет для ООО')
async def conducting_tax(message: types.Message):
    await bot.send_message(message.chat.id, 'Налоговый учет для ООО', reply_markup=kb_tab_ooo)


@db.message_handler(text='Налоговый учет для ИП')
async def recovery_tax(message: types.Message):
    await bot.send_message(message.chat.id, 'Налоговый учет для ИП', reply_markup=kb_tab_ip)


@db.message_handler(text='Внутренний аудит налогового учета')
async def staging_tax(message: types.Message):
    await bot.send_message(message.chat.id, 'Внутренний аудит налогового учета', reply_markup=kb_audit)


@db.message_handler(text='🔙Назад')
async def back_tax(message: types.Message):
    await bot.send_message(message.chat.id, 'Главное меню', reply_markup=kb_first_menu)


def register_handlers_tax(db: Dispatcher):
    db.register_message_handler(conducting_tax, commands=['Ведение бухгалтерского учета'])
    db.register_message_handler(recovery_tax, commands=['Восстановление бухгалтерского учета'])
    db.register_message_handler(staging_tax, commands=['Постановка бухгалтерского учета'])
    db.register_message_handler(back_tax, commands=['🔙Назад'])
