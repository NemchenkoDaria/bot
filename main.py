import aiosqlite
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram import F
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config
from handlers import router

logging.basicConfig(level=logging.INFO)

API_TOKEN = '6525590699:AAEIv6ss0stOLCGqLlDlQdp-V66K9Zqk4Jk'

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

DB_NAME = 'db'

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())