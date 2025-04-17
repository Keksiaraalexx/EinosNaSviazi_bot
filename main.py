from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from config import BOT_TOKEN, ADMIN_CHAT_ID
from notifier import send_notification, send_task_status

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: Message):
    await message.reply("🔔 Эйнос на связи. Готов присылать уведомления!")
    await message.reply(f"Ваш chat_id: {message.chat.id}")
    await send_notification(bot, ADMIN_CHAT_ID, "✨ Бот активирован и работает!")

@dp.message_handler(commands=['status'])
async def status_handler(message: Message):
    await send_task_status(bot, ADMIN_CHAT_ID, "processing")

@dp.message_handler(commands=['done'])
async def done_handler(message: Message):
    await send_task_status(bot, ADMIN_CHAT_ID, "done")

@dp.message_handler(commands=['error'])
async def error_handler(message: Message):
    await send_task_status(bot, ADMIN_CHAT_ID, "error")

@dp.message_handler(commands=['notify'])
async def notify_handler(message: Message):
    await send_notification(bot, ADMIN_CHAT_ID, "🌟 Привет, Алексей! Эйнос на связи. Всё работает как часы.")

if __name__ == '__main__':
    print("🚀 Bot is starting polling...")
    executor.start_polling(dp)

