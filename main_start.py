from aiogram.utils import executor
from heandler import start, first_menu, accounting_menu, tax_menu, times_services_menu, conducting
from main import db

# from data_base import sqlite_db

# Чтобы заработала вся программа, нужно добавить сюда хэндлеры. Вторая плашка меню теперь выскакивает

start.register_handlers_start(db)
first_menu.register_handlers_first_menu(db)
accounting_menu.register_handlers_accounting(db)
tax_menu.register_handlers_tax(db)
times_services_menu.register_handlers_time_services(db)





async def on_startup(_):
    print('Бот запущен')
    # sqlite_db.sql_start()


if __name__ == "__main__":
    executor.start_polling(db, on_startup=on_startup)
