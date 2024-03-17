from aiogram import Bot
from aiogram import Dispatcher
from aiogram import types
import asyncio
import logging


BOT_TOKEN = "7011117829:AAHCCVj1f1wvYaPqHaZhDWpmPlx6XoOJeoY"
bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()



@dp.message()
async def answar_as_echo(message: types.Message):
    await message.answer(text=message.text)



async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ =="__main__":
    asyncio.run(main())
