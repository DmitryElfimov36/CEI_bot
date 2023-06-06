from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_description_rec = KeyboardButton(text='Описание (восстановление бухучета)')
button_rate_rec = KeyboardButton(text='Тарифы (восстановление бухучета)')
button_application_rec = KeyboardButton(text='Оставить заявку на услугу')
button_contact_rec = KeyboardButton(text='Я хочу, чтобы со мной связались', request_contact=True)
button_back_rec = KeyboardButton(text='Главное меню')


kb_recovery = ReplyKeyboardMarkup(resize_keyboard=True)

kb_recovery.insert(button_description_rec).insert(button_rate_rec).row(button_application_rec)\
    .insert(button_contact_rec).row(button_back_rec)