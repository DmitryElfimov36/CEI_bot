import requests
import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from main import db, bot
from keyboard.contact import phone_number
from keyboard.keyboard import kb_first_menu
from keyboard.kb_bot_link import url


class PhoneandBot(StatesGroup):
    application_cond_state = State()
    phone_cond_state = State()


@db.message_handler(text='Описание (Нулевая отчетность)')
async def description_null(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"Здесь будет описание НУЛ ОТЧЕТ"))


@db.message_handler(text='Тарифы (Нулевая отчетность)')
async def rate_null(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"Здесь будут ЦЕНЫ НУЛ ОТЧЕТ"))


@db.message_handler(text='Оставить заявку на услугу')
async def application_null(message: types.Message):
    await bot.send_message(message.chat.id, "Для перехода в чат нажмите на кнопку ниже:", reply_markup=url)


@db.message_handler(text='Я хочу, чтобы со мной связались')
async def contact_null(message: types.Message):
    await bot.send_message(message.chat.id, 'Спасибо. С вами свяжутся')


@db.message_handler(text='Назад')
async def back_null(message: types.Message):
    await bot.send_message(message.chat.id, 'Главное меню', reply_markup=kb_first_menu)


def register_handlers_search(db: Dispatcher):
    db.register_message_handler(description_null, commands=['Описание (Нулевая отчетность)'])
    db.register_message_handler(rate_null, commands=['Тарифы (Нулевая отчетность)'])
    db.register_message_handler(application_null, commands=['Оставить заявку на услугу'])
    db.register_message_handler(contact_null, commands=['Я хочу, чтобы со мной связались'])
    db.register_message_handler(back_null, commands=['Назад'])