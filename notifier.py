from aiogram import Bot

async def send_notification(bot: Bot, chat_id: int, text: str):
    await bot.send_message(chat_id=chat_id, text=text)

async def send_task_status(bot: Bot, chat_id: int, status: str = "processing"):
    if status == "done":
        message = "✅ Задача завершена"
    elif status == "processing":
        message = "🕐 Задача в процессе"
    elif status == "error":
        message = "❌ Произошла ошибка"
    else:
        message = f"🔔 Статус: {status}"

    await bot.send_message(chat_id=chat_id, text=message)
