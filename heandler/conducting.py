import requests
import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, ReplyKeyboardMarkup, KeyboardButton
from scipy.integrate._ivp.ivp import MESSAGES

from database import sqlite_db
from main import db, bot
from keyboard.contact import phone_number
from keyboard.keyboard import kb_first_menu
from keyboard.kb_bot_link import url
from keyboard.kb_conducting import button_contact_cond


class PhoneCond(StatesGroup):
    application_cond_state = State()
    contact_cond = State()


@db.message_handler(text='Описание (ведение бухучета)')
async def description_cond(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"<b>ВЕДЕНИЕ БУХГАЛТЕРСКОГО УЧЕТА</b>\n\n"
                                                    f"<b>Ведение бухгалтерского учета</b> обязательна для всех "
                                                    f"организаций в "
                                                    f"РФ. Бухгалтерская отчетность публична и необходима для анализа "
                                                    f"любым контрагентам вашего бизнеса: поставщикам, покупателям, "
                                                    f"инвесторам, фискальным органам и т.д. За достоверность "
                                                    f"бухгалтерской отчетности несет ответственность руководитель "
                                                    f"организации. Далеко не каждый руководитель разберется в дебрях "
                                                    f"российского законодательства, поэтому делегировать эти заботы "
                                                    f"нужно профессионалам, ведь это является гарантией безопасности "
                                                    f"и успешности развития бизнеса.\n\n<b>Бухгалтерское обслуживание"
                                                    f" силами нашей компании имеет ряд преимуществ по сравнению с "
                                                    f"наймом штатных специалистов:</b>\n1. затраты на лицензионное "
                                                    f"рограммное обеспечение мы полностью берем на себя\n2. "
                                                    f"не возникает необходимость оплачивать страховые взносы за "
                                                    f"штатного специалиста, составляющих 30% от суммы заработной "
                                                    f"платы сотрудника\n3.утствуют проблемы замены штатного "
                                                    f"бухгалтера на время отпуска, или больничного\n\n"
                                                    f"<b>Бухгалтерское обслуживание включает в себя:</b> \n<b>1.</b> "
                                                    f"консультации по оптимизации "
                                                    f"налогообложения в рамках действующего законодательства\n"
                                                    f"<b>2.</b> "
                                                    f"обработку и систематизацию первичных учетных документов\n"
                                                    f"<b>3.</b>"
                                                    f"отражение в регистрах бухгалтерского и налогового учета "
                                                    f"сведений об имуществе и обязательствах компании, а также об "
                                                    f"их движении\n<b>4.</b> расчет зарплаты, а также всех видов "
                                                    f"социальных выплат\n<b>5.</b> подготовку и сдачу бухгалтерской "
                                                    f"отчетности и налоговых деклараций\n<b>6.</b> подготовку "
                                                    f"отчетов и их сдачу во внебюджетные фонды"), parse_mode="html")


@db.message_handler(text='Тарифы (ведение бухучета)')
async def rate_cond(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"Здесь будут ЦЕНЫ БУХУЧЕТА"))


@db.message_handler(text='Оставить заявку на услугу')
async def application_cond(message: types.Message):
    await PhoneCond.application_cond_state.set()
    await bot.send_message(message.chat.id, "Для перехода в чат нажмите на кнопку ниже:", reply_markup=url)


@db.message_handler(commands=["Я хочу, чтобы со мной связались"])
async def contact_cond(message: types.Message):
    await bot.send_message(message.chat.id, 'Номер телефона', reply_markup=button_contact_cond)
    await PhoneCond.next()


@db.message_handler(content_types=['contact'])
async def contact_handler_cond(message: types.Message, state: FSMContext):
    if message.contact is not None:
        us_id_cond = message.from_user.id
        user_name_cond = message.from_user.first_name
        phone_number_cond = message.contact.phone_number
        button_cond = 'Ведение бухгалерского учета'
        await sqlite_db.db_table_val(us_id=us_id_cond, user_name=user_name_cond, phone_number=phone_number_cond)
        await state.finish()


@db.message_handler(text='Назад')
async def back_cond(message: types.Message):
    await bot.send_message(message.chat.id, 'Главное меню', reply_markup=kb_first_menu)


def register_handlers_search(db: Dispatcher):
    db.register_message_handler(description_cond, commands=['Описание (ведение бухучета)'])
    db.register_message_handler(rate_cond, commands=['Тарифы (ведение бухучета)'])
    db.register_message_handler(application_cond, commands=['Оставить заявку на услугу'])
    db.register_message_handler(contact_cond, commands=['Я хочу, чтобы со мной связались'])
    db.register_message_handler(contact_handler_cond, content_types=['contact'], state=PhoneCond.contact_cond)
    db.register_message_handler(back_cond, commands=['Назад'])
