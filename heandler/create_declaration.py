import requests
import aiogram.utils.markdown as md
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from main import db, bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboard.kb_declaration import kb_next


class FSM(StatesGroup):
    price = State()
    doc = State()


@db.message_handler(text='Составление декларации')
async def start_command(message: types.Message):
    await bot.send_message(message.chat.id, 'Что вас интересует?', reply_markup=kb_next)



@db.message_handler(text='Стоимость')
async def price(message: types.Message):
    await bot.send_message(message.chat.id, 'Составление декларации 3-НДФЛ - 720 руб.')


@db.message_handler(text='Какие документы нужны')
async def documents(message: types.Message):
    await bot.send_message(message.chat.id,
                           'Список документов для вычета: \n'
                           '1. Справка 2-НДФЛ с работы\n2. Ксерокопия паспорта 2, 3 страницы и прописка\n3. ИНН\n\n'
                           '4.1 Вычет по приобретению квартиры (дома) копии документов:\nДоговор купли-продажи\n'
                           'Акт приема-передачи\nВыписка из ЕГРН\nПлатежный документ (чек, платежное '
                           'поручение)\n\n4.2 Если квартира приобретена в ипотеку:\nИпотечный договор\n'
                           'Справка из банка об уплаченных процентах\n\n5. Вычет по медицинским услугам, '
                           'копии документов:\nДоговор об оказании медицинских услуг\nЛицензия медицинской организации\n'
                           'Справка об оплате медицинских услуг\n\n6. Вычет по оплате образовательных услуг, '
                           'копии документов:\nДоговор об оказании образовательных услуг\n'
                           'Лицензия организации, оказывающей образовательные услуги\nЧек об оплате образовательных'
                           'услуг\n\n7. Вычет по договору добровольного страхования, копии документов: \n'
                           'Договор добровольного страхования\nЧек об оплате\n\n8. Вычет по физкультуре и оздоровительным '
                           'услугам, копии документов: \nДоговор об оказании услуг\nЛицензия\nЧек об оплате\n\n'
                           'Если вычеты по лечению, обучению родственников, необходимы документы, подтверждающие'
                           'родство (свидетельство о рождении, свидетельство о браке, справка из ЗАГС')


def register_handlers_search(db: Dispatcher):
    db.register_message_handler(start_command, commands=['Составление декларации'])
    db.register_message_handler(price, commands=['Стоимость'])
    db.register_message_handler(documents, commands=['Какие документы нужны'])
