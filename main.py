import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart, Command
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"Hi, {message.from_user.first_name}, I'm bot!")


@dp.message(Command('help'))
async def command_help(message: Message):
    await message.answer("This bot can execute the commands:\n /start\n /help")


if __name__ == "__main__":
    asyncio.run(main())
