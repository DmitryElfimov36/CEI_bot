from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_description_cons = KeyboardButton(text='Описание (консультация)')
button_rate_cons = KeyboardButton(text='Тарифы (консультация)')
button_application_cons = KeyboardButton(text='Оставить заявку на услугу')
button_contact_cons = KeyboardButton(text='Я хочу, чтобы со мной связались', request_contact=True)
button_back_cons = KeyboardButton(text='Назад')


kb_consultation = ReplyKeyboardMarkup(resize_keyboard=True)

kb_consultation.insert(button_description_cons).insert(button_rate_cons).row(button_application_cons)\
    .insert(button_contact_cons).row(button_back_cons)