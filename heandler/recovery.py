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


@db.message_handler(text='Описание (восстановление бухучета)')
async def description_rec(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"<b>ВОССТАНОВЛЕНИЕ БУХГАЛТЕРСКОГО УЧЕТА</b>\n\n"
                                                    f"<b>Бухгалтерский и налоговый учет</b> должны вестись непрерывно "
                                                    f"со дня регистрации. Российское законодательство определяет четкую "
                                                    f"структуру ведения документооборота компании. Несданные вовремя "
                                                    f"отчеты и налоговые декларации, даже «нулевые», приведут к аресту "
                                                    f"расчетного счета. Следствием ошибок в учете и неправильно "
                                                    f"исчисленных налогов будет доначисление штрафов и пеней и, "
                                                    f"как следствие, остановка деятельности всего предприятия. "
                                                    f"В этом случае организации требуются услуги по восстановлению "
                                                    f"бухгалтерского учета.\n\n<b>В каких случаях придется произвести "
                                                    f"восстановление бухучета:</b>\n· недостоверная информация в "
                                                    f"отчетах или отсутствие их;\n· ошибки в базе данных "
                                                    f"документооборота;\n· увольнение или смена штатного бухгалтера;\n"
                                                    f"· смена руководителя или учредителей;\n· предстоящая проверка "
                                                    f"контролирующих органов.\n\nВосстановление бухгалтерского учета "
                                                    f"включает в себя:\n<b>1.</b> Анализ бухгалтерского и налогового "
                                                    f"учета на выявление нарушений\n<b>2.</b> Обработка первичной документации"
                                                    f"\n<b>3.</b> Восстановление недостающих документов\n"
                                                    f"<b>4.</b> Формирование регистров бухгалтерского учета\n<b>5. </b>Расчет, "
                                                    f"формирование отчетности в налоговом учете\n<b>6.</b> Отправка "
                                                    f"отчетности в фискальные органы и заказчику"),
                           parse_mode='html')


@db.message_handler(text='Тарифы (восстановление бухучета)')
async def rate_rec(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"Здесь будут ЦЕНЫ ВОССТАНОВЛЕНИЕ"))


@db.message_handler(text='Оставить заявку на услугу')
async def application_rec(message: types.Message):
    await bot.send_message(message.chat.id, "Для перехода в чат нажмите на кнопку ниже:", reply_markup=url)


@db.message_handler(text='Я хочу, чтобы со мной связались')
async def contact_rec(message: types.Message):
    await bot.send_message(message.chat.id, 'Спасибо. С вами свяжутся')


@db.message_handler(text='Назад')
async def back_rec(message: types.Message):
    await bot.send_message(message.chat.id, 'Главное меню', reply_markup=kb_first_menu)


def register_handlers_search(db: Dispatcher):
    db.register_message_handler(description_rec, commands=['Описание (восстановление бухучета)'])
    db.register_message_handler(rate_rec, commands=['Тарифы (восстановление бухучета)'])
    db.register_message_handler(application_rec, commands=['Оставить заявку на услугу'])
    db.register_message_handler(contact_rec, commands=['Я хочу, чтобы со мной связались'])
    db.register_message_handler(back_rec, commands=['Назад'])