import requests
import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from scipy.integrate._ivp.ivp import MESSAGES

from database import sqlite_db
from main import db, bot
from keyboard.keyboard import kb_first_menu
from keyboard.kb_audit import button_contact_audit, kb_audit
from keyboard.kb_bot_link import url


class PhoneAudit(StatesGroup):
    application_cond_state = State()
    contact_audit = State()


@db.message_handler(text='Описание (внутренний аудит)')
async def description_audit(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"Здесь будет описание АУДИТ"))


@db.message_handler(text='Тарифы (внутренний аудит)')
async def rate_audit(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"Здесь будут ЦЕНЫ АУДИТ"))


@db.message_handler(text='Оставить заявку на услугу (внутренний аудит)')
async def application_audit(message: types.Message):
    await bot.send_message(message.chat.id, "Для перехода в чат нажмите на кнопку ниже:", reply_markup=url)


@db.message_handler(commands=["Я хочу, чтобы со мной связались"])
async def contact_audit(message: types.Message):
    await bot.send_message(message.chat.id, 'Номер телефона', reply_markup=button_contact_audit)
    await PhoneAudit.next()


@db.message_handler(content_types=['contact'])
async def contact_handler_audit(message: types.Message, state: FSMContext):
    if message.contact is not None:
        us_id_audit = message.from_user.id
        user_name_audit = message.from_user.first_name
        phone_number_audit = message.contact.phone_number
        button_audit = 'Аудит'
        await sqlite_db.db_table_val(us_id=us_id_audit, user_name=user_name_audit, phone_number=phone_number_audit)
        await state.finish()


@db.message_handler(text='Главное меню')
async def back_audit(message: types.Message):
    await bot.send_message(message.chat.id, 'Главное меню', reply_markup=kb_first_menu)


def register_handlers_search(db: Dispatcher):
    db.register_message_handler(description_audit, commands=['Описание (внутренний аудит)'])
    db.register_message_handler(rate_audit, commands=['Тарифы (внутренний аудит)'])
    db.register_message_handler(application_audit, commands=['Оставить заявку на услугу (внутренний аудит)'])
    db.register_message_handler(contact_audit, commands=['Я хочу, чтобы со мной связались'])
    db.register_message_handler(back_audit, commands=['Главное меню'])

