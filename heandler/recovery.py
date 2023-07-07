import requests
import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from database import sqlite_db
from keyboard.kb_recovery import button_contact_rec
from main import db, bot
from keyboard.contact import phone_number
from keyboard.keyboard import kb_first_menu
from keyboard.kb_bot_link import url


class PhoneRec(StatesGroup):
    application_cond_state = State()
    contact_rec = State()


@db.message_handler(text='Описание (восстановление бухучета)')
async def description_rec(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"<b>ВОССТАНОВЛЕНИЕ БУХГАЛТЕРСКОГО УЧЕТА</b>\n\n"
                                                    f"Анализ бухгалтерского и налогового учета на выявление нарушений, "
                                                    f"обработка первичной документации, восстановление недостающих "
                                                    f"документов, формирование регистров бухгалтерского учета, расчет, "
                                                    f"формирование отчетности в налоговом учете, отправка отчетности в "
                                                    f"фискальные органы и заказчику"),
                           parse_mode='html')


@db.message_handler(text='Тарифы (восстановление бухучета)')
async def rate_rec(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"Восстановленние бухгалтерского учета: <b>от 10 000 руб</b>"))


@db.message_handler(text='Оставить заявку на услугу')
async def application_rec(message: types.Message):
    await bot.send_message(message.chat.id, "Для перехода в чат нажмите на кнопку ниже:", reply_markup=url)


@db.message_handler(commands=["Я хочу, чтобы со мной связались (восстановление бухучета)"])
async def contact_rec(message: types.Message):
    await bot.send_message(message.chat.id, 'Номер телефона', reply_markup=button_contact_rec)
    await PhoneRec.contact_rec.set()


@db.message_handler(content_types=['contact'])
async def contact_handler_rec(message: types.Message, state: FSMContext):
    if message.contact is not None:
        us_id_rec = message.from_user.id
        user_name_rec = message.from_user.first_name
        phone_number_rec = message.contact.phone_number
        button_rec = 'Восстановление бухучета'
        await sqlite_db.db_table_val(us_id=us_id_rec, user_name=user_name_rec, phone_number=phone_number_rec)
        await state.finish()


@db.message_handler(text='Главное меню')
async def back_rec(message: types.Message):
    await bot.send_message(message.chat.id, 'Главное меню', reply_markup=kb_first_menu)


def register_handlers_search(db: Dispatcher):
    db.register_message_handler(description_rec, commands=['Описание (восстановление бухучета)'])
    db.register_message_handler(rate_rec, commands=['Тарифы (восстановление бухучета)'])
    db.register_message_handler(application_rec, commands=['Оставить заявку на услугу'])
    db.register_message_handler(contact_rec, commands=['Я хочу, чтобы со мной связались'])
    db.register_message_handler(back_rec, commands=['Главное меню'])