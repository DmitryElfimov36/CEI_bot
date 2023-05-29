import requests
import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from scipy.integrate._ivp.ivp import MESSAGES

from database import sqlite_db
from main import db, bot
from keyboard.kb_consultation import kb_consultation
from keyboard.keyboard import kb_first_menu
from keyboard.kb_bot_link import url


class PhoneCons(StatesGroup):
    contact_cons = State()
    city = State()


@db.message_handler(text='Описание (консультация)')
async def description_cons(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"<b>КОНСУЛЬТАЦИИ ПО БУХГАЛТЕРСКОМУ И НАЛОГОВОМУ УЧЕТУ</b>\n\n"
                                                    f"Многие организации занимаются учетом силами самого руководителя "
                                                    f"или штатного бухгалтера  в зависимости от объема оборота "
                                                    f"предприятия. Но часто возникают вопросы, с которыми справиться "
                                                    f"самостоятельно очень сложно, для чего существуют "
                                                    f"консультационные услуги по бухгалтерскому и налоговому учету.\n"
                                                    f"Наши специалисты оказывают широкий перечень консультаций в сфере "
                                                    f"бухгалтерского учета и налогообложения. Профессиональные "
                                                    f"консультации от опытных сотрудников компании <b>«Центр "
                                                    f"экономической информации»</b> позволят вам избежать ошибок в "
                                                    f"учете и отчетности, которые могут привести к финансовым "
                                                    f"санкциям.\n\n<b>В каких случаях вам необходимо будет получить "
                                                    f"ответы на свои вопросы:</b>\n"
                                                    f"· Вы столкнулись с нетипичной ситуацией или сложным вопросом, "
                                                    f"требующие практические знания;\n· Вы хотите подготовиться к "
                                                    f"деловому разговору с контрагентом;\n· Вы хотите исключить ошибки "
                                                    f"в финансовой отчетности.\n\nКонсультационные услуги могут "
                                                    f"оказываться в форме разового или абонентского обслуживания. "
                                                    f"Ответы могут быть предоставлены как в устной, так и в "
                                                    f"письменной форме и предусматривают ссылки на нормативную базу "
                                                    f"и судебную практику.\n\n<b>У нас вы можете получить "
                                                    f"консультации:</b>\n<b>1.</b> По вопросам бухгалтерского учета и "
                                                    f"налогообложения, в том числе по вопросам постановки и ведения "
                                                    f"бухгалтерского, налогового учета;\n<b>2.</b> По оптимизации "
                                                    f"налогообложения;\nПрактические консультации по вопросам работы в "
                                                    f"программе «1С: Предприятие» в конфигурациях «Бухгалтерия "
                                                    "предприятия» и «Зарплата и Управление Персоналом»\n<b>4. </b>"
                                                    "По формированию учетной политики для целей бухгалтерского и "
                                                    "налогового учета;\n<b>5.</b> По составлению  и сдаче всех видов "
                                                    "отчетности.\nКонсультационные услуги по бухгалтерскому учету "
                                                    "оказывают действующие бухгалтеры, занимающиеся сопровождением "
                                                    "бухгалтерского и налогового учета. Наши сотрудники имеют "
                                                    "<b>аттестаты</b> сертифицированных профессиональных бухгалтеров "
                                                    "и налоговых консультантов. Получив колоссальный опыт на практике,"
                                                    " работая с различными направлениями бизнеса, мы сможем провести "
                                                    "консультацию, объяснить вам <b>сложнейшие</b> процессы <b>простым "
                                                    "и понятным</b> языком. "),
                           parse_mode='html')


@db.message_handler(text='Тарифы (консультация)')
async def rate_cons(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"Здесь будут ЦЕНЫ КОНСУЛЬТАЦИЙ"))


@db.message_handler(text='Оставить заявку на услугу')
async def application_cons(message: types.Message):
    await bot.send_message(message.chat.id, "Для перехода в чат нажмите на кнопку ниже:", reply_markup=url)


@db.callback_query_handler(text="Я хочу, чтобы со мной связались (консультация)", state=PhoneCons.contact_cons)
async def contact_cons(query: CallbackQuery):
    await bot.send_message(query.from_user.id, MESSAGES["send_contact_cons"], reply_markup=kb_consultation, parse_mode="MarkdownV2")


@db.message_handler(content_types=types.ContentTypes.ANY)
async def contact_handler_cons(message: types.Message, state: FSMContext):
    us_id = message.from_user.id
    user_name = message.from_user.first_name
    phone_number = message.contact.phone_number
    button = 'Консультационные услуги'
    await sqlite_db.db_table_val(us_id=us_id, user_name=user_name, phone_number=phone_number, button=button)
    await state.finish()


@db.message_handler(text='Назад')
async def back_cons(message: types.Message):
    await bot.send_message(message.chat.id, 'Главное меню', reply_markup=kb_first_menu)


def register_handlers_search(db: Dispatcher):
    db.register_message_handler(description_cons, commands=['Описание (консультация)'])
    db.register_message_handler(rate_cons, commands=['Тарифы (консультация)'])
    db.register_message_handler(application_cons, commands=['Оставить заявку на услугу'])
    db.register_message_handler(contact_cons, commands=['Я хочу, чтобы со мной связались (консультация)'])
    db.register_message_handler(back_cons, commands=['Назад'])
