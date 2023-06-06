import requests
import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from database import sqlite_db
from keyboard.kb_fill import button_contact_fill
from main import db, bot
from keyboard.contact import phone_number
from keyboard.keyboard import kb_first_menu
from keyboard.kb_bot_link import url


class PhoneFill(StatesGroup):
    application_cond_state = State()
    contact_fill = State()


@db.message_handler(text='Описание (заполнение документов)')
async def description_fill(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"Здесь будет описание ЗАП ДЕКЛ"))


@db.message_handler(text='Тарифы (заполнение документов)')
async def rate_fill(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"Здесь будут ЦЕНЫ ЗАП ДЕКЛ"))


@db.message_handler(text='Оставить заявку на услугу')
async def application_fill(message: types.Message):
    await bot.send_message(message.chat.id, "Для перехода в чат нажмите на кнопку ниже:", reply_markup=url)


@db.message_handler(commands=["Я хочу, чтобы со мной связались (заполнение документов)"])
async def contact_fill(message: types.Message):
    await bot.send_message(message.chat.id, 'Номер телефона', reply_markup=button_contact_fill)
    await PhoneFill.contact_fill.set()


@db.message_handler(content_types=['contact'])
async def contact_handler_fill(message: types.Message, state: FSMContext):
    if message.contact is not None:
        us_id_fill = message.from_user.id
        user_name_fill = message.from_user.first_name
        phone_number_fill = message.contact.phone_number
        button_fill = 'Заполнение документов'
        await sqlite_db.db_table_val(us_id=us_id_fill, user_name=user_name_fill, phone_number=phone_number_fill)
        await state.finish()


@db.message_handler(text='Главное меню')
async def back_fill(message: types.Message):
    await bot.send_message(message.chat.id, 'Главное меню', reply_markup=kb_first_menu)


def register_handlers_search(db: Dispatcher):
    db.register_message_handler(description_fill, commands=['Описание (заполнение документов)'])
    db.register_message_handler(rate_fill, commands=['Тарифы (заполнение документов)'])
    db.register_message_handler(application_fill, commands=['Оставить заявку на услугу'])
    db.register_message_handler(contact_fill, commands=['Я хочу, чтобы со мной связались'])
    db.register_message_handler(back_fill, commands=['Главное меню'])