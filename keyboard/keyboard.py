from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_accounting = KeyboardButton(text='Бухгалтерский учет')
button_tax_accountiong = KeyboardButton(text='Налоговый учет')
button_times_services = KeyboardButton(text='Разовые услуги')
button_help = KeyboardButton(text='Помощь')

kb_first_menu = ReplyKeyboardMarkup(resize_keyboard=True)

kb_first_menu.insert(button_accounting).insert(button_tax_accountiong).insert(button_times_services).row(button_help)
