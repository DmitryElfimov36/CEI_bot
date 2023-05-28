from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_conducting = KeyboardButton(text='Ведение бухгалтерского учета')
button_recovery = KeyboardButton(text='Восстановление бухгалтерского учета')
button_staging = KeyboardButton(text='Постановка бухгалтерского учета')
button_1c = KeyboardButton(text='Постановка учета 1С')
button_correction = KeyboardButton(text='Исправление ошибок')
button_consultation = KeyboardButton(text='Консультационные услуги')
button_back_acc = KeyboardButton(text='Назад')
kb_acc = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_acc.insert(button_conducting).insert(button_recovery).row(button_staging).insert(button_1c).row(button_correction).\
    insert(button_consultation).row(button_back_acc)
