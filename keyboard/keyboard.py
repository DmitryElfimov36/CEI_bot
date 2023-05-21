from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_accounting = KeyboardButton(text='Бухгалтерский учет')
button_tax_accountiong = KeyboardButton(text='Налоговый учет')
button_times_services = KeyboardButton(text='Разовые услуги')
button_help = KeyboardButton(text='Помощь')

kb_first_menu = ReplyKeyboardMarkup(resize_keyboard=True)

kb_first_menu.add(button_accounting).add(button_tax_accountiong).add(button_times_services).insert(button_help)
