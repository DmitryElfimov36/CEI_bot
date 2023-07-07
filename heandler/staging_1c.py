import requests
import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from database import sqlite_db
from keyboard.kb_staging_1c import button_contact_1c
from main import db, bot
from keyboard.contact import phone_number
from keyboard.keyboard import kb_first_menu
from keyboard.kb_bot_link import url


class Phone1c(StatesGroup):
    application_cond_state = State()
    contact_1c = State()


@db.message_handler(text='Описание (постановка учета 1С)')
async def description_staging_1c(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"<b>Постановка учета и работа в 1С</b>\n\n "
                                                    f"Постановка бухгалтерского учета на платформе 1С \n\nВедение "
                                                    f"отдельных участков учета в 1С \n\nФормирование регистров "
                                                    f"бухгалтерского учета и отчетности \n\nВосстановление базы "
                                                    f"клиента, приведение регистров учета в соответствии с "
                                                    f"законодательством \n\nОтладка учетных регистров и конфигурации "
                                                    f"программы, подходящей для специфики  компании \n\nПодготовка "
                                                    f"документов на основании аналитики по конкретным операциям "
                                                    f"или направлениям деятельности компании"),
                           parse_mode='html')


@db.message_handler(text='Тарифы (постановка учета 1С)')
async def rate_staging_1c(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"Стоимость постановки учета в 1С: <b>от 5 000 руб</b>"))


@db.message_handler(text='Оставить заявку на услугу')
async def application_staging_1c(message: types.Message):
    await bot.send_message(message.chat.id, "Для перехода в чат нажмите на кнопку ниже:", reply_markup=url)


@db.message_handler(commands=["Я хочу, чтобы со мной связались (постановка учета 1С)"])
async def contact_1c(message: types.Message):
    await bot.send_message(message.chat.id, 'Номер телефона', reply_markup=button_contact_1c)
    await Phone1c.contact_1c.set()


@db.message_handler(content_types=['contact'])
async def contact_handler_1c(message: types.Message, state: FSMContext):
    if message.contact is not None:
        us_id_1c = message.from_user.id
        user_name_1c = message.from_user.first_name
        phone_number_1c = message.contact.phone_number
        button_1c = 'Постановка учета 1С'
        await sqlite_db.db_table_val(us_id=us_id_1c, user_name=user_name_1c, phone_number=phone_number_1c)
        await state.finish()


@db.message_handler(text='Главное меню')
async def back_staging_1c(message: types.Message):
    await bot.send_message(message.chat.id, 'Главное меню', reply_markup=kb_first_menu)


def register_handlers_search(db: Dispatcher):
    db.register_message_handler(description_staging_1c, commands=['Описание (постановка учета 1С)'])
    db.register_message_handler(rate_staging_1c, commands=['Тарифы (постановка учета 1С)'])
    db.register_message_handler(application_staging_1c, commands=['Оставить заявку на услугу'])
    db.register_message_handler(contact_1c, commands=['Я хочу, чтобы со мной связались'])
    db.register_message_handler(back_staging_1c, commands=['Главное меню'])