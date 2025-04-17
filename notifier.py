from aiogram import Bot
from aiogram.exceptions import TelegramAPIError, ChatNotFound

async def send_notification(bot: Bot, chat_id: int, text: str):
    try:
        await bot.send_message(chat_id=chat_id, text=text)
    except ChatNotFound:
        print(f"❌ Ошибка: Чат с ID {chat_id} не найден. Возможно, пользователь не написал первым.")
    except TelegramAPIError as e:
        print(f"❌ Telegram API error: {e}")

async def send_task_status(bot: Bot, chat_id: int, status: str = "processing"):
    if status == "done":
        message = "✅ Задача завершена"
    elif status == "processing":
        message = "🔄 Задача в процессе"
    elif status == "error":
        message = "❌ Произошла ошибка"
    else:
        message = f"⚠️ Статус: {status}"

    try:
        await bot.send_message(chat_id=chat_id, text=message)
    except TelegramAPIError as e:
        print(f"❌ Telegram API error while sending status: {e}")
