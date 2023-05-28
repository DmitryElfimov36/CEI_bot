from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_description_fill = KeyboardButton(text='Описание (заполнение документов)')
button_rate_fill = KeyboardButton(text='Тарифы (заполнение документов)')
button_application_fill = KeyboardButton(text='Оставить заявку на услугу')
button_contact_fill = KeyboardButton(text='Я хочу, чтобы со мной связались', request_contact=True)
button_back_fill = KeyboardButton(text='Назад')

kb_fill = ReplyKeyboardMarkup(resize_keyboard=True)

kb_fill.insert(button_description_fill).insert(button_rate_fill).row(button_application_fill)\
    .insert(button_contact_fill).row(button_back_fill)