from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_fill = KeyboardButton(text='Заполнение деклараций, заявлений, справок')
button_null = KeyboardButton(text='Нулевая отчетность')
button_back_time_serv = KeyboardButton(text='Главное меню')

kb_time_services = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_time_services.insert(button_fill).insert(button_null).row(button_back_time_serv)
