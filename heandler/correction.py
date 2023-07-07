import requests
import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from database import sqlite_db
from keyboard.kb_correction import button_contact_corr
from main import db, bot
from keyboard.contact import phone_number
from keyboard.keyboard import kb_first_menu
from keyboard.kb_bot_link import url


class PhoneCorr(StatesGroup):
    application_cond_state = State()
    contact_corr = State()


@db.message_handler(text='Описание (исправление ошибок)')
async def description_corr(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"<b>Исправление ошибок в бухгалтерском и налоговом учете</b>\n\n"
                                                    f"Регулярное проведение инвентаризаций имущества и обязательств "
                                                    f"организации, в том числе – сверка расчетов с контрагентами "
                                                    f"\n\nАнализ данных, содержащихся в регистрах бухгалтерского "
                                                    f"учета, в том числе – проверка сопоставимости показателей по "
                                                    f"периодам (проверяется соответствие уровня доходов уровню "
                                                    f"расходов) \n\nПроверка нестандартных проводок и крупных "
                                                    f"(существенных) операций \n\nСопоставимость показателей "
                                                    f"(арифметическо - логический контроль) бухгалтерской отчетности."),
                           parse_mode='html')


@db.message_handler(text='Тарифы (исправление ошибок)')
async def rate_corr(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"Здесь будут ЦЕНЫ ИСП ОШИБОК"))


@db.message_handler(text='Оставить заявку на услугу')
async def application_corr(message: types.Message):
    await bot.send_message(message.chat.id, "Для перехода в чат нажмите на кнопку ниже:", reply_markup=url)


@db.message_handler(commands=["Я хочу, чтобы со мной связались"])
async def contact_corr(message: types.Message):
    await bot.send_message(message.chat.id, 'Номер телефона', reply_markup=button_contact_corr)
    await PhoneCorr.contact_corr.set()


@db.message_handler(content_types=['contact'])
async def contact_handler_corr(message: types.Message, state: FSMContext):
    if message.contact is not None:
        us_id_corr = message.from_user.id
        user_name_corr = message.from_user.first_name
        phone_number_corr = message.contact.phone_number
        button_cons = 'Исправление ошибок'
        await sqlite_db.db_table_val(us_id=us_id_corr, user_name=user_name_corr, phone_number=phone_number_corr)
        await state.finish()


@db.message_handler(text='Назад')
async def back_corr(message: types.Message):
    await bot.send_message(message.chat.id, 'Главное меню', reply_markup=kb_first_menu)


def register_handlers_search(db: Dispatcher):
    db.register_message_handler(description_corr, commands=['Описание (исправление ошибок)'])
    db.register_message_handler(rate_corr, commands=['Тарифы (исправление ошибок)'])
    db.register_message_handler(application_corr, commands=['Оставить заявку на услугу'])
    db.register_message_handler(contact_corr, commands=['Я хочу, чтобы со мной связались'])
    db.register_message_handler(back_corr, commands=['Назад'])
