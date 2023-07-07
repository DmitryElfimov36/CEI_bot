import requests
import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from database import sqlite_db
from keyboard.kb_tab_ip import button_contact_tab_ip
from main import db, bot
from keyboard.contact import phone_number
from keyboard.keyboard import kb_first_menu
from keyboard.kb_bot_link import url


class PhoneIp(StatesGroup):
    application_cond_state = State()
    contact_staging_ip = State()


@db.message_handler(text='Описание (Налоговый учет для ИП)')
async def description_staging_ip(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"Здесь будет описание УЧЕТ ИП"))


@db.message_handler(text='Тарифы (Налоговый учет для ИП)')
async def rate_staging_ip(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"Налоговый учет ИП: <b>от 1 200 руб/мес</b>"))


@db.message_handler(text='Оставить заявку на услугу (Налоговый учет для ИП)')
async def application_staging_ip(message: types.Message):
    await bot.send_message(message.chat.id, "Для перехода в чат нажмите на кнопку ниже:", reply_markup=url)


@db.message_handler(commands=["Я хочу, чтобы со мной связались (Налоговый учет для ИП)"])
async def contact_staging_ip(message: types.Message):
    await bot.send_message(message.chat.id, 'Номер телефона', reply_markup=button_contact_tab_ip)
    await PhoneIp.contact_staging_ip.set()


@db.message_handler(content_types=['contact'])
async def contact_handler_staging_ip(message: types.Message, state: FSMContext):
    if message.contact is not None:
        us_id_ip = message.from_user.id
        user_name_ip = message.from_user.first_name
        phone_number_ip = message.contact.phone_number
        button_ip = 'Налоговый учет для ИП'
        await sqlite_db.db_table_val(us_id=us_id_ip, user_name=user_name_ip, phone_number=phone_number_ip)
        await state.finish()


@db.message_handler(text='Главное меню')
async def back_staging_ip(message: types.Message):
    await bot.send_message(message.chat.id, 'Главное меню', reply_markup=kb_first_menu)


def register_handlers_search(db: Dispatcher):
    db.register_message_handler(description_staging_ip, commands=['Описание (Налоговый учет для ИП)'])
    db.register_message_handler(rate_staging_ip, commands=['Тарифы (Налоговый учет для ИП)'])
    db.register_message_handler(application_staging_ip, commands=['Оставить заявку на услугу'])
    db.register_message_handler(contact_staging_ip, commands=['Я хочу, чтобы со мной связались'])
    db.register_message_handler(back_staging_ip, commands=['Главное меню'])