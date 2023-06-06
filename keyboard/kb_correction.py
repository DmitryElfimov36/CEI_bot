from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_description_corr = KeyboardButton(text='Описание (исправление ошибок)')
button_rate_corr = KeyboardButton(text='Тарифы (исправление ошибок)')
button_application_corr = KeyboardButton(text='Оставить заявку на услугу')
button_contact_corr = KeyboardButton(text='Я хочу, чтобы со мной связались', request_contact=True)
button_back_corr = KeyboardButton(text='Главное меню')


kb_correction = ReplyKeyboardMarkup(resize_keyboard=True)

kb_correction.insert(button_description_corr).insert(button_rate_corr).row(button_application_corr)\
    .insert(button_contact_corr).row(button_back_corr)