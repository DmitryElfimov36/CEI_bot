from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

url_button = InlineKeyboardButton(text="Перейти в чат", url="https://t.me/BuhCEIbot")

url = InlineKeyboardMarkup(resize_keyboard=True)
url.add(url_button)