from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_description_cond = KeyboardButton(text='Описание (ведение бухучета)')
button_rate_cond = KeyboardButton(text='Тарифы (ведение бухучета)')
button_application_cond = KeyboardButton(text='Оставить заявку на услугу')
button_contact_cond = KeyboardButton(text='Я хочу, чтобы со мной связались (бухучет)', request_contact=True)
button_back_conducting = KeyboardButton(text='Главное меню')

kb_conducting = ReplyKeyboardMarkup(resize_keyboard=True)

kb_conducting.insert(button_description_cond).insert(button_rate_cond).row(button_application_cond)\
    .insert(button_contact_cond).row(button_back_conducting)
