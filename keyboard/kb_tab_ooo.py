from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_description_tab_ooo = KeyboardButton(text='Описание (Налоговый учет для ООО)')
button_rate_tab_ooo = KeyboardButton(text='Тарифы (Налоговый учет для ООО)')
button_application_tab_ooo = KeyboardButton(text='Оставить заявку на услугу')
button_contact_tab_ooo = KeyboardButton(text='Я хочу, чтобы со мной связались', request_contact=True)
button_back_tab_ooo = KeyboardButton(text='Назад')


kb_tab_ooo = ReplyKeyboardMarkup(resize_keyboard=True)

kb_tab_ooo.insert(button_description_tab_ooo).insert(button_rate_tab_ooo).row(button_application_tab_ooo).\
    insert(button_contact_tab_ooo).row(button_back_tab_ooo)