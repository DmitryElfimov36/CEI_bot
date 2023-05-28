from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_description_1c = KeyboardButton(text='Описание (постановка учета 1С)')
button_rate_1c = KeyboardButton(text='Тарифы (постановка учета 1С)')
button_application_1c = KeyboardButton(text='Оставить заявку на услугу')
button_contact_1c = KeyboardButton(text='Я хочу, чтобы со мной связались', request_contact=True)
button_back_1c = KeyboardButton(text='Назад')


kb_staging_1c = ReplyKeyboardMarkup(resize_keyboard=True)

kb_staging_1c.insert(button_description_1c).insert(button_rate_1c).row(button_application_1c)\
    .insert(button_contact_1c).row(button_back_1c)