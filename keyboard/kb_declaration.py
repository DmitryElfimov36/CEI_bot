from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_price = KeyboardButton(text='Стоимость')
button_doc = KeyboardButton(text='Какие документы нужны')
kb_next = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_next.add(button_price).add(button_doc)
