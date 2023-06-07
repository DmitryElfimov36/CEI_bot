from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_tab_ooo = KeyboardButton(text='Налоговый учет для ООО')
button_tab_ip = KeyboardButton(text='Налоговый учет для ИП')
button_audit = KeyboardButton(text='Внутренний аудит налогового учета')
button_back_tax = KeyboardButton(text='Главное меню')

kb_tax = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_tax.insert(button_tab_ooo).insert(button_tab_ip).row(button_audit).row(button_back_tax)