from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from config import BOT_TOKEN, ADMIN_CHAT_ID
from notifier import send_notification

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: Message):
    await message.reply("🔔 Эйнос на связи. Готов присылать уведомления!")
    await message.reply(f"👤 Ваш chat_id: `{message.chat.id}`", parse_mode="Markdown")
    await send_notification(bot, ADMIN_CHAT_ID, "✨ Бот активирован и работает!")

if __name__ == '__main__':
    executor.start_polling(dp)
