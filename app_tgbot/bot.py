import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import CommandStart
from app_tgbot.config import TOKEN
from app_tgbot.fsm import Form
from app_tgbot.handlers import start_handler, name_handler, age_handler, grade_handler

# Logging
logging.basicConfig(level=logging.INFO)

# Bot and Dispatcher initialization
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Handler registration
dp.message.register(start_handler,CommandStart())
dp.message.register(name_handler, Form.name)
dp.message.register(age_handler, Form.age)
dp.message.register(grade_handler, Form.grade)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
