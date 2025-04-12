import asyncio
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = "7866381644:AAHnCWsOji0bRD3IR4FYv6SRpC2I2z5CRuc"

dp = Dispatcher()


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.bot.send_photo(message.chat.id, "https://s3.akarmain.ru/qr/5013a7308.png")


# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
          