from aiogram.utils import executor
from heandler import start, create_declaration
from main import db
#from data_base import sqlite_db


start.register_handlers_start(db)
create_declaration.register_handlers_search(db)



async def on_startup(_):
    print('Бот запущен')
    # sqlite_db.sql_start()


if __name__ == "__main__":
    executor.start_polling(db, on_startup=on_startup)
