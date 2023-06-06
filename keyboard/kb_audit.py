from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_description_audit = KeyboardButton(text='Описание (внутренний аудит)')
button_rate_audit = KeyboardButton(text='Тарифы (внутренний аудит)')
button_application_audit = KeyboardButton(text='Оставить заявку на услугу')
button_contact_audit = KeyboardButton(text='Я хочу, чтобы со мной связались', request_contact=True)
button_back_audit = KeyboardButton(text='Главное меню')

kb_audit = ReplyKeyboardMarkup(resize_keyboard=True)

kb_audit.insert(button_description_audit).insert(button_rate_audit).row(button_application_audit). \
    insert(button_contact_audit).row(button_back_audit)
