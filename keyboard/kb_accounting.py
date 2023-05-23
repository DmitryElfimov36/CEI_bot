from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_conducting = KeyboardButton(text='Ведение бухгалтерского учета')
button_recovery = KeyboardButton(text='Восстановление бухгалтерского учета')
button_staging = KeyboardButton(text='Постановка бухгалтерского учета')
button_1c = KeyboardButton(text='Постановка учета 1С')
button_correction = KeyboardButton(text='Исправление ошибок')
button_consultation = KeyboardButton(text='Консультационные услуги')
kb_acc = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_acc.add(button_conducting).add(button_recovery).add(button_staging).add(button_1c).add(button_correction).\
    add(button_consultation)
