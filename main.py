import logging
import asyncio
from aiogram import Bot, Dispatcher

from handlers import router  # общий роутер

TOKEN = "your_token"
logging.basicConfig(level=logging.INFO)

# создаём бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher()

# подключаем роутер
dp.include_router(router)

# Функция запуска
async def main():
    # сообщение при старте
    await bot.send_message(your_telegram_id, "Я запустился")

    try:
        await dp.start_polling(bot)
    finally:
        await bot.send_message(your_telegram_id, "Я завершил работу")
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())