from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_start = KeyboardButton(text='Составление декларации')
button_search = KeyboardButton(text='Поиск')
button_help = KeyboardButton(text='Помощь')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(button_start).add(button_search).insert(button_help)
