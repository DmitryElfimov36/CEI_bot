from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_description_null = KeyboardButton(text='Описание (Нулевая отчетность)')
button_rate_null = KeyboardButton(text='Тарифы (Нулевая отчетность)')
button_application_null = KeyboardButton(text='Оставить заявку на услугу')
button_contact_null = KeyboardButton(text='Я хочу, чтобы со мной связались', request_contact=True)
button_back_null = KeyboardButton(text='Главное меню')

kb_null = ReplyKeyboardMarkup(resize_keyboard=True)

kb_null.insert(button_description_null).insert(button_rate_null).row(button_application_null).\
    insert(button_contact_null).row(button_back_null)