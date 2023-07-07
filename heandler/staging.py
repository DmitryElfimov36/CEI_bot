import requests
import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from database import sqlite_db
from keyboard.kb_staging import button_contact_stag
from main import db, bot
from keyboard.contact import phone_number
from keyboard.keyboard import kb_first_menu
from keyboard.kb_bot_link import url


class PhoneStag(StatesGroup):
    application_cond_state = State()
    contact_staging = State()


@db.message_handler(text='Описание (постановка бухучета)')
async def description_staging(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"<b>ПОСТАНОВКА БУХГАЛТЕРСКОГО УЧЕТА</b>\n\nЧто сложного в "
                                                    f"Анализ правовой структуры компании и направлений ее деятельности "
                                                    f"\n\nОрганизация системы документооборота и построение системы "
                                                    f"внутреннего контроля \n\nПостроение эффективной организационной "
                                                    f"структуры бухгалтерии с учётом распределения обязанностей в целях "
                                                    f"предотвращения риска обмана и хищений \n\nРазработка собственной "
                                                    f"системы регистров бухгалтерского и налогового учёта "
                                                    f"\n\nСоставление схемы документооборота и графика его осуществления"),
                           parse_mode='html')


@db.message_handler(text='Тарифы (постановка бухучета)')
async def rate_staging(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"Стоимость постановки бухгалтерского учета: <b>от 12 000 руб</b>"))


@db.message_handler(text='Оставить заявку на услугу')
async def application_staging(message: types.Message):
    await bot.send_message(message.chat.id, "Для перехода в чат нажмите на кнопку ниже:", reply_markup=url)


@db.message_handler(commands=["Я хочу, чтобы со мной связались (постановка бухучета)"])
async def contact_staging(message: types.Message):
    await bot.send_message(message.chat.id, 'Номер телефона', reply_markup=button_contact_stag)
    await PhoneStag.contact_staging.set()


@db.message_handler(content_types=['contact'])
async def contact_handler_stag(message: types.Message, state: FSMContext):
    if message.contact is not None:
        us_id_stag = message.from_user.id
        user_name_stag = message.from_user.first_name
        phone_number_stag = message.contact.phone_number
        button_stag = 'Постановка бух учета'
        await sqlite_db.db_table_val(us_id=us_id_stag, user_name=user_name_stag, phone_number=phone_number_stag)
        await state.finish()


@db.message_handler(text='Главное меню')
async def back_staging(message: types.Message):
    await bot.send_message(message.chat.id, 'Главное меню', reply_markup=kb_first_menu)


def register_handlers_search(db: Dispatcher):
    db.register_message_handler(description_staging, commands=['Описание (постановка бухучета)'])
    db.register_message_handler(rate_staging, commands=['Тарифы (постановка бухучета)'])
    db.register_message_handler(application_staging, commands=['Оставить заявку на услугу (постановка бухучета)'])
    db.register_message_handler(contact_staging, commands=['Я хочу, чтобы со мной связались (постановка бухучета)'])
    db.register_message_handler(back_staging, commands=['Главное меню'])