from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

contact = KeyboardButton(text = 'Отправить свой контакт ☎️', request_contact=True)
markup_request = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

markup_request.add(contact)