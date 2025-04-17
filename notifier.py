from aiogram import Bot
from aiogram.utils.exceptions import BotBlocked, ChatNotFound, TelegramAPIError

async def send_notification(bot: Bot, chat_id: int, text: str):
    try:
        await bot.send_message(chat_id=chat_id, text=text)
    except ChatNotFound:
        print(f"❌ Чат с ID {chat_id} не найден.")
    except BotBlocked:
        print(f"🚫 Бот заблокирован пользователем {chat_id}.")
    except TelegramAPIError as e:
        print(f"⚠️ Другая ошибка Telegram API: {e}")

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
        print(f"⚠️ Ошибка при отправке статуса: {e}")
