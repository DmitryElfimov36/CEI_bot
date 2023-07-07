import requests
import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from database import sqlite_db
from keyboard.kb_null import button_contact_null
from main import db, bot
from keyboard.contact import phone_number
from keyboard.keyboard import kb_first_menu
from keyboard.kb_bot_link import url


class PhoneNull(StatesGroup):
    application_cond_state = State()
    contact_null = State()


@db.message_handler(text='Описание (Нулевая отчетность)')
async def description_null(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"Здесь будет описание НУЛ ОТЧЕТ"))


@db.message_handler(text='Тарифы (Нулевая отчетность)')
async def rate_null(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"Стоимость нулевой отчетности: <b>от 1380 руб/мес</b>"))


@db.message_handler(text='Оставить заявку на услугу')
async def application_null(message: types.Message):
    await bot.send_message(message.chat.id, "Для перехода в чат нажмите на кнопку ниже:", reply_markup=url)


@db.message_handler(commands=["Я хочу, чтобы со мной связались (заполнение документов)"])
async def contact_null(message: types.Message):
    await bot.send_message(message.chat.id, 'Номер телефона', reply_markup=button_contact_null)
    await PhoneNull.contact_null.set()


@db.message_handler(content_types=['contact'])
async def contact_handler_null(message: types.Message, state: FSMContext):
    if message.contact is not None:
        us_id_null = message.from_user.id
        user_name_null = message.from_user.first_name
        phone_number_null = message.contact.phone_number
        button_null = 'Нулевая отчетность'
        await sqlite_db.db_table_val(us_id=us_id_null, user_name=user_name_null, phone_number=phone_number_null)
        await state.finish()


@db.message_handler(text='Главное меню')
async def back_null(message: types.Message):
    await bot.send_message(message.chat.id, 'Главное меню', reply_markup=kb_first_menu)


def register_handlers_search(db: Dispatcher):
    db.register_message_handler(description_null, commands=['Описание (Нулевая отчетность)'])
    db.register_message_handler(rate_null, commands=['Тарифы (Нулевая отчетность)'])
    db.register_message_handler(application_null, commands=['Оставить заявку на услугу'])
    db.register_message_handler(contact_null, commands=['Я хочу, чтобы со мной связались'])
    db.register_message_handler(back_null, commands=['Главное меню'])