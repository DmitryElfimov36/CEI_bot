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


@db.message_handler(text='Помощь')
async def help(message: types.Message):
    await bot.send_message(message.chat.id, 'Бот <b>Центра Экономической Информации</b> предназначен для '
                                            'информационной поддержки и заказа услуг. С помощью данного бота '
                                            'вы можете:\n\n<b>1.</b> получить необходимую информацию по стоимости, '
                                            'и нужных документах;\n\n<b>2.</b> прочитать описание услуги, '
                                            'узнать, почему она необходима именно вам;\n\n<b>3.</b> оставить заявку '
                                            'на исполнение услуги, отправив номер телефона с помощью кнопки '
                                            '<b>"Я хочу, чтобы со мной связались"</b>, или перейти непосредственно к '
                                            'общению со специалистом по кнопке <b>"Оставить заявку на услугу"</b>.\n\n'
                                            'Наши специалисты - дипломированные профессионалы по различным сферам '
                                            'бухгалтерских услуг, поэтому мы гарантируем, что вы получите свою'
                                            'услугу качественно и в срок. Будем рады видеть вас среди наших клиентов!\n'
                                            '\n<em>Для продолжения выберите необходимый пукнт меню</em>',
                           parse_mode='html')



def register_handlers_first_menu(db: Dispatcher):
    db.register_message_handler(account, commands=['Бухгалтерский учет'])
    db.register_message_handler(tax, commands=['Налоговый учет'])
    db.register_message_handler(times_services, commands=['Разовые услуги'])
