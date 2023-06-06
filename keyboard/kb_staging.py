from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_description_stag = KeyboardButton(text='Описание (постановка бухучета)')
button_rate_stag = KeyboardButton(text='Тарифы (постановка бухучета)')
button_application_stag = KeyboardButton(text='Оставить заявку на услугу')
button_contact_stag = KeyboardButton(text='Я хочу, чтобы со мной связались', request_contact=True)
button_back_stag = KeyboardButton(text='Главное меню')

kb_staging = ReplyKeyboardMarkup(resize_keyboard=True)

kb_staging.insert(button_description_stag).insert(button_rate_stag).row(button_application_stag)\
    .insert(button_contact_stag).row(button_back_stag)