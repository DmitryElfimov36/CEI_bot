from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_description_audit = KeyboardButton(text='Описание (внутренний аудит)')
button_rate_audit = KeyboardButton(text='Тарифы (внутренний аудит)')
button_application_audit = KeyboardButton(text='Оставить заявку на услугу (внутренний аудит)')
button_contact_audit = KeyboardButton(text='Я хочу, чтобы со мной связались (внутренний аудит)', request_contact=True)
button_back_audit = KeyboardButton(text='Назад аудит')

kb_audit = ReplyKeyboardMarkup(resize_keyboard=True)

kb_audit.insert(button_description_audit).insert(button_rate_audit).insert(button_application_audit). \
    insert(button_contact_audit).add(button_back_audit)
