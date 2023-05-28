from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

contact = KeyboardButton(text='Оставить номер телефона:', request_contact=True)
button_back_contact = KeyboardButton(text='Назад')
phone_number = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

phone_number.add(contact).add(button_back_contact)