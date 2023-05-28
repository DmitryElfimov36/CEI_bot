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


@db.message_handler(text='Описание (постановка учета 1С)')
async def description_staging_1c(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"<b>Постановка учета и работа в 1С</b>\n\nНаша компания "
                                                    f"осуществляет бухгалтерское обслуживание в системе «1С» в "
                                                    f"облачном сервисе 1C:Fresh, который позволяет работать с "
                                                    f"программой «1С:Предприятие» через интернет. Базы данных "
                                                    f"хранятся не на компьютере пользователя, а на серверах фирмы "
                                                    f"«1С». \n\nВ сервисе предусмотрено несколько уровней "
                                                    f"обеспечения безопасности и сохранности данных. Базы системы "
                                                    f"«1С:Предприятие», хранятся и обрабатываются в надежном и "
                                                    f"охраняемом дата-центре, регулярно осуществляется полное "
                                                    f"резервное копирование всех данных пользователей\n\n"
                                                    f"<b>Приложения в системе «1С», в которых мы работаем:</b>\n"
                                                    f"1С:Бухгалтерия предприятия;\n1С:Зарплата и управление персоналом;"
                                                    f"\n1С:Зарплата и кадры;\n1С:Предприниматель;\n1С:Управление "
                                                    f"нашей фирмой.\n\nДля наших клиентов мы открываем один доступ "
                                                    f"бесплатно. Руководитель или уполномоченный представитель может "
                                                    f"в любое время зайти в программу своей компании и получить всю "
                                                    f"информацию, сформировать финансовый анализ, сделать счет для "
                                                    f"покупателя и т.д.\n\nБухгалтерское обслуживание ООО обязательно "
                                                    f"на всех налоговых режимах и даже при отсутствии реальной "
                                                    f"деятельности компании. Мы предлагаем профессиональные услуги "
                                                    f"по бухгалтерскому сопровождению как отдельных участков "
                                                    f"бухгалтерии, так и комплексно.\nВсе специалисты Центра "
                                                    f"экономической информации имеют сертификаты пользователя "
                                                    f"ПП «1С:Предприятие» и всегда готовы помочь руководителю или "
                                                    f"его представителю разобраться в программном продукте, в "
                                                    f"открытом для клиента доступе.\n\n<b>Мы всегда рады помочь нашим "
                                                    f"клиентам в работе с «1С» как разово, так и на постоянной "
                                                    f"основе</b>\n\n<b>1.</b> Постановка бухгалтерского учета на "
                                                    f"платформе «1С»;\n<b>2.</b>Ведение отдельных участков учета в "
                                                    f"«1С»;\n<b>3.</b>Формирование регистров бухгалтерского учета и "
                                                    f"отчетности;\n<b>4.</b>Восстановление базы клиента, приведение "
                                                    f"регистров учета в соответствии с законодательством;\n<b>5.</b>"
                                                    f"Отладка учетных регистров и конфигурации программы, подходящей "
                                                    f"для специфики вашей компании;\n<b>6.</b>Подготовка документов на "
                                                    f"основании аналитики по конкретным операциям или направлениям "
                                                    f"деятельности компании."),
                           parse_mode='html')


@db.message_handler(text='Тарифы (постановка учета 1С)')
async def rate_staging_1c(message: types.Message):
    await bot.send_message(message.chat.id, md.text(f"Здесь будут ЦЕНЫ ПОСТАНОВКА БУХ УЧЕТА 1C"))


@db.message_handler(text='Оставить заявку на услугу')
async def application_staging_1c(message: types.Message):
    await bot.send_message(message.chat.id, "Для перехода в чат нажмите на кнопку ниже:", reply_markup=url)


@db.message_handler(text='Я хочу, чтобы со мной связались')
async def contact_staging_1c(message: types.Message):
    await bot.send_message(message.chat.id, 'Спасибо. С вами свяжутся')


@db.message_handler(text='Назад')
async def back_staging_1c(message: types.Message):
    await bot.send_message(message.chat.id, 'Главное меню', reply_markup=kb_first_menu)


def register_handlers_search(db: Dispatcher):
    db.register_message_handler(description_staging_1c, commands=['Описание (постановка учета 1С)'])
    db.register_message_handler(rate_staging_1c, commands=['Тарифы (постановка учета 1С)'])
    db.register_message_handler(application_staging_1c, commands=['Оставить заявку на услугу'])
    db.register_message_handler(contact_staging_1c, commands=['Я хочу, чтобы со мной связались'])
    db.register_message_handler(back_staging_1c, commands=['Назад'])