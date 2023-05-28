from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_description_cor = KeyboardButton(text='Описание (исправление ошибок)')
button_rate_cor = KeyboardButton(text='Тарифы (исправление ошибок)')
button_application_cor = KeyboardButton(text='Оставить заявку на услугу')
button_contact_cor = KeyboardButton(text='Я хочу, чтобы со мной связались', request_contact=True)
button_back_cor = KeyboardButton(text='Назад')


kb_correction = ReplyKeyboardMarkup(resize_keyboard=True)

kb_correction.insert(button_description_cor).insert(button_rate_cor).row(button_application_cor)\
    .insert(button_contact_cor).row(button_back_cor)