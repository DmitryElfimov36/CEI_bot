from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


button_description_tab_ip = KeyboardButton(text='Описание (Налоговый учет для ИП)')
button_rate_tab_ip = KeyboardButton(text='Тарифы (Налоговый учет для ИП)')
button_application_tab_ip = KeyboardButton(text='Оставить заявку на услугу')
button_contact_tab_ip = KeyboardButton(text='Я хочу, чтобы со мной связались', request_contact=True)
button_back_tab_ip = KeyboardButton(text='Главное меню')


kb_tab_ip = ReplyKeyboardMarkup(resize_keyboard=True)

kb_tab_ip.insert(button_description_tab_ip).insert(button_rate_tab_ip).row(button_application_tab_ip)\
    .insert(button_contact_tab_ip).row(button_back_tab_ip)