from tmdb_fetcher import get_movie_by_genre
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
import asyncio

API_TOKEN = '8265378179:AAHz8INiM43hs3LCQptOHWQU1y6UAFjLsiA' 

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def send_welcome(message: Message):
    await message.answer("سلام! 🎬 من آناهیتافیلم هستم و توسط مائده 357 ساخته شدم. بگو چه ژانری دوست داری؟")

@dp.message()
async def reply_message(message: Message):
    genre = message.text.strip()
    result = get_movie_by_genre(genre)
    await message.answer(result)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
