import requests
import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

from database import sqlite_db
from keyboard.kb_staging import button_contact_stag
from main import db, bot
from keyboard.contact import phone_number
from keyboard.keyboard import kb_first_menu
from keyboard.kb_bot_link import url


class PhoneStag(StatesGroup):
    application_cond_state = State()
    contact_staging = State()


@db.message_handler(text='Описание (постановка бухучета)')
async def description_staging(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"<b>ПОСТАНОВКА БУХГАЛТЕРСКОГО УЧЕТА</b>\n\nЧто сложного в "
                                                    f"постановке бухгалтерского учета? Купил программу и дело сделано, "
                                                    f"она сама за вас все посчитает. Но, все не так просто. Для "
                                                    f"ведения правильного учета необходимо построить четкую систему "
                                                    f"сбора, обработки и регистрации информации.\n\n"
                                                    f"<b>Постановка бухгалтерского учета включает несколько этапов:</b>"
                                                    f"\n· анализ правовой структуры компании и направлений ее "
                                                    f"деятельности;\n· организация системы документооборота и "
                                                    f"построение системы внутреннего контроля;\n "
                                                    f"· построение эффективной организационной структуры бухгалтерии с "
                                                    f"учётом распределения обязанностей в целях предотвращения риска "
                                                    f"обмана и хищений;\n· разработка собственной системы регистров "
                                                    f"бухгалтерского и налогового учёта;\n"
                                                    f"· составление схемы документооборота и графика его осуществления."
                                                    f"\n\nПри регистрации нового бизнеса собственники часто не спешат "
                                                    f"прибегать к услугам профессионалов, ошибочно полагая, что "
                                                    f"«нулевая» организация не требует никаких затрат пока не начала "
                                                    f"работать. Но это не так. Как только юридическое лицо поставлено "
                                                    f"на учет в налоговом органе, на руководителя накладывается "
                                                    f"обязанность ведения бухгалтерского и налогового учета, и "
                                                    f"формирование и предоставление отчетности. Учет начинается с "
                                                    f"первого дня новой организации, его нельзя начать через неделю "
                                                    f"или месяц. Когда бы вы не пришли  к бухгалтеру, учет он начнет "
                                                    f"с того самого первого дня. Зачастую выбор сторонней организации, "
                                                    f"оказывающей профильные услуги, оказывается самым выгодным "
                                                    f"вариантом.\n\n"
                                                    f"<b>В каких случаях придется произвести восстановление "
                                                    f"бухучета:</b>\n<b>1.</b> Открытие новой организации;"
                                                    f"\n<b>2.</b> Изменение вида деятельности;"
                                                    f"\n<b>3.</b> Переход на иной режим налогообложения;\n"
                                                    f"<b>4.</b> Реорганизация предприятия;\n<b>5.</b> Реорганизация "
                                                    f"предприятия;\n<b>6.</b> Запущенность учета в прошлые периоды.\n\n"
                                                    f"Наша компания осуществит постановку учета в соответствии с "
                                                    f"требованиями законодательства. Мы организуем работу бухгалтерии, "
                                                    f"систему взаимодействия с руководителем. Правильная постановка "
                                                    f"бухгалтерского учёта поможет вашему бизнесу в любую минуту "
                                                    f"получить достоверную информацию о финансовом состоянии "
                                                    f"предприятия для принятия эффективных управленческих решений."),
                           parse_mode='html')


@db.message_handler(text='Тарифы (постановка бухучета)')
async def rate_staging(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"Здесь будут ЦЕНЫ ПОСТАНОВКА БУХ УЧЕТА"))


@db.message_handler(text='Оставить заявку на услугу')
async def application_staging(message: types.Message):
    await bot.send_message(message.chat.id, "Для перехода в чат нажмите на кнопку ниже:", reply_markup=url)


@db.message_handler(commands=["Я хочу, чтобы со мной связались (постановка бухучета)"])
async def contact_staging(message: types.Message):
    await bot.send_message(message.chat.id, 'Номер телефона', reply_markup=button_contact_stag)
    await PhoneStag.contact_staging.set()


@db.message_handler(content_types=['contact'])
async def contact_handler_stag(message: types.Message, state: FSMContext):
    if message.contact is not None:
        us_id_stag = message.from_user.id
        user_name_stag = message.from_user.first_name
        phone_number_stag = message.contact.phone_number
        button_stag = 'Постановка бух учета'
        await sqlite_db.db_table_val(us_id=us_id_stag, user_name=user_name_stag, phone_number=phone_number_stag)
        await state.finish()


@db.message_handler(text='Главное меню')
async def back_staging(message: types.Message):
    await bot.send_message(message.chat.id, 'Главное меню', reply_markup=kb_first_menu)


def register_handlers_search(db: Dispatcher):
    db.register_message_handler(description_staging, commands=['Описание (постановка бухучета)'])
    db.register_message_handler(rate_staging, commands=['Тарифы (постановка бухучета)'])
    db.register_message_handler(application_staging, commands=['Оставить заявку на услугу (постановка бухучета)'])
    db.register_message_handler(contact_staging, commands=['Я хочу, чтобы со мной связались (постановка бухучета)'])
    db.register_message_handler(back_staging, commands=['Главное меню'])