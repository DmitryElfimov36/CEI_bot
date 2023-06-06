import aiosqlite as sq
from aiogram.types import Contact

conn = sq.connect('database_cei', check_same_thread=False)
cursor = conn.cursor()


async def sql_start():
    global base, cur
    base = await sq.connect('database_cei.db')
    cur = await base.cursor()
    if base:
        print('База данных подключена')
    await base.execute('CREATE TABLE IF NOT EXISTS history(us_id INT, user_name INT, phone_number INT)')
    await base.commit()


async def db_table_val(us_id: int, user_name: int, phone_number: int):
    await cur.execute('INSERT INTO history (us_id, user_name, phone_number) VALUES (?, ?, ?)',
                      (us_id, user_name, phone_number))
    await base.commit()
