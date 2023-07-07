import requests
import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, message
from scipy.integrate._ivp.ivp import MESSAGES

from database import sqlite_db
from main import db, bot
from keyboard.kb_consultation import kb_consultation, button_contact_cons
from keyboard.keyboard import kb_first_menu
from keyboard.kb_bot_link import url


class PhoneCons(StatesGroup):
    contact_cons = State()
    city = State()


@db.message_handler(text='Описание (консультация)')
async def description_cons(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"<b>КОНСУЛЬТАЦИИ ПО БУХГАЛТЕРСКОМУ И НАЛОГОВОМУ УЧЕТУ</b>\n\n"
                                                    f"По вопросам бухгалтерского учета и налогообложения, в том "
                                                    f"числе по вопросам постановки и ведения бухгалтерского, "
                                                    f"налогового учета \n\nПо оптимизации налогообложения "
                                                    f"\n\nПрактические консультации по вопросам работы в программе "
                                                    f"''1С: Предприятие'' в конфигурациях ''Бухгалтерия предприятия''"
                                                    f" и ''Зарплата и Управление Персоналом'' "
                                                    f"\n\nПо формированию учетной политики для целей бухгалтерского "
                                                    f"и налогового учета \n\nПо составлению  и сдаче всех видов "
                                                    f"отчетности."),
                           parse_mode='html')


@db.message_handler(text='Тарифы (консультация)')
async def rate_cons(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"Стоимость консультационных услуг: <b>от 850 руб/час</b>"))


@db.message_handler(text='Оставить заявку на услугу')
async def application_cons(message: types.Message):
    await bot.send_message(message.chat.id, "Для перехода в чат нажмите на кнопку ниже:", reply_markup=url)


@db.message_handler(commands=["Я хочу, чтобы со мной связались"])
async def contact_cons(message: types.Message):
    await bot.send_message(message.chat.id, 'Номер телефона', reply_markup=button_contact_cons)
    await PhoneCons.contact_cons.set()


@db.message_handler(content_types=['contact'])
async def contact_handler_cons(message: types.Message, state: FSMContext):
    if message.contact is not None:
        us_id_cons = message.from_user.id
        user_name_cons = message.from_user.first_name
        phone_number_cons = message.contact.phone_number
        button_cons = 'Консультационные услуги'
        await sqlite_db.db_table_val(us_id=us_id_cons, user_name=user_name_cons, phone_number=phone_number_cons)
        await state.finish()


@db.message_handler(text='Назад')
async def back_cons(message: types.Message):
    await bot.send_message(message.chat.id, 'Главное меню', reply_markup=kb_first_menu)


def register_handlers_search(db: Dispatcher):
    db.register_message_handler(description_cons, commands=['Описание (консультация)'])
    db.register_message_handler(rate_cons, commands=['Тарифы (консультация)'])
    db.register_message_handler(application_cons, commands=['Оставить заявку на услугу'])
    db.register_message_handler(contact_cons, commands=['Я хочу, чтобы со мной связались (консультация)'])
    db.register_message_handler(contact_handler_cons, content_types=['contact'], state=PhoneCons.contact_cons)
    db.register_message_handler(back_cons, commands=['Назад'])
