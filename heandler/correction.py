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


@db.message_handler(text='Описание (исправление ошибок)')
async def description_corr(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"<b>Исправление ошибок в бухгалтерском и налоговом учете</b>\n\n"
                                                    f"Существует много приемов и способов для контроля за первичной "
                                                    f"документацией и правильностью введения бухгалтерского учета, "
                                                    f"но время от времени случается так, что в учете данные "
                                                    f"отражаются неточно или ошибочно. Полностью уберечь компанию "
                                                    f"от ошибок в учете практически невозможно. А значит, нужно "
                                                    f"предпринимать меры к своевременному выявлению и устранению "
                                                    f"последствий ошибок в учете и отчетности.\n\n<b>Самые "
                                                    f"распространенные ошибки в бухгалтерском учете и отчетности "
                                                    f"могут возникнуть по причине:</b>\n· неправильного применения "
                                                    f"законодательства РФ о бухгалтерском учете и (или) нормативных "
                                                    f"правовых актов по бухгалтерскому учету;\n· неверного "
                                                    f"использования учетной политики организации;\n· неточности в "
                                                    f"вычислениях;\n· неправильной классификации или оценки фактов "
                                                    f"хозяйственной деятельности;\n· неправильного использования "
                                                    f"информации, имеющейся на дату подписания бухгалтерской "
                                                    f"отчетности;\n· недобросовестных действий должностных лиц "
                                                    f"организации."),
                           parse_mode='html')


@db.message_handler(text='Тарифы (исправление ошибок)')
async def rate_corr(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"Здесь будут ЦЕНЫ ИСП ОШИБОК"))


@db.message_handler(text='Оставить заявку на услугу')
async def application_corr(message: types.Message):
    await bot.send_message(message.chat.id, "Для перехода в чат нажмите на кнопку ниже:", reply_markup=url)


@db.message_handler(text='Я хочу, чтобы со мной связались')
async def contact_corr(message: types.Message):
    await bot.send_message(message.chat.id, 'Спасибо. С вами свяжутся')


@db.message_handler(text='Назад')
async def back_corr(message: types.Message):
    await bot.send_message(message.chat.id, 'Главное меню', reply_markup=kb_first_menu)


def register_handlers_search(db: Dispatcher):
    db.register_message_handler(description_corr, commands=['Описание (исправление ошибок)'])
    db.register_message_handler(rate_corr, commands=['Тарифы (исправление ошибок)'])
    db.register_message_handler(application_corr, commands=['Оставить заявку на услугу'])
    db.register_message_handler(contact_corr, commands=['Я хочу, чтобы со мной связались'])
    db.register_message_handler(back_corr, commands=['Назад'])
