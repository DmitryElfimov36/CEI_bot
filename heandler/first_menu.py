import requests
import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from main import db, bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboard.kb_accounting import kb_acc
from keyboard.kb_tax import kb_tax
from keyboard.kb_times_services import kb_time_services


class FSM(StatesGroup):
    acc = State()
    tax = State()
    time_services = State()


@db.message_handler(text='Бухгалтерский учет')
async def account(message: types.Message):
    await bot.send_message(message.chat.id, 'Выберите интересующую услугу:', reply_markup=kb_acc)


@db.message_handler(text='Налоговый учет')
async def tax(message: types.Message):
    await bot.send_message(message.chat.id, 'Выберите интересующую услугу:', reply_markup=kb_tax)


@db.message_handler(text='Разовые услуги')
async def times_services(message: types.Message):
    await bot.send_message(message.chat.id, 'Выберите интересующую услугу:', reply_markup=kb_time_services)


def register_handlers_first_menu(db: Dispatcher):
    db.register_message_handler(account, commands=['Бухгалтерский учет'])
    db.register_message_handler(tax, commands=['Налоговый учет'])
    db.register_message_handler(times_services, commands=['Разовые услуги'])
