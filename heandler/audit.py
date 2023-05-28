import requests
import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from main import db, bot
from keyboard.keyboard import kb_first_menu
from keyboard.kb_audit import button_contact_audit
from keyboard.kb_bot_link import url


class PhoneandBot(StatesGroup):
    application_cond_state = State()
    phone_cond_state = State()


@db.message_handler(text='Описание (внутренний аудит)')
async def description_audit(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"Здесь будет описание АУДИТ"))


@db.message_handler(text='Тарифы (внутренний аудит)')
async def rate_audit(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"Здесь будут ЦЕНЫ АУДИТ"))


@db.message_handler(text='Оставить заявку на услугу')
async def application_audit(message: types.Message):
    await bot.send_message(message.chat.id, "Для перехода в чат нажмите на кнопку ниже:", reply_markup=url)


@db.message_handler(text='Я хочу, чтобы со мной связались')
async def contact_audit(message: types.Message):
    await bot.send_message(message.chat.id, 'Спасибо. С вами свяжутся')


@db.message_handler(text='Назад')
async def back_audit(message: types.Message):
    await bot.send_message(message.chat.id, 'Главное меню', reply_markup=kb_first_menu)


def register_handlers_search(db: Dispatcher):
    db.register_message_handler(description_audit, commands=['Описание (внутренний аудит)'])
    db.register_message_handler(rate_audit, commands=['Тарифы (внутренний аудит)'])
    db.register_message_handler(application_audit, commands=['Оставить заявку на услугу'])
    db.register_message_handler(contact_audit, commands=['Я хочу, чтобы со мной связались'])
    db.register_message_handler(back_audit, commands=['Назад'])

