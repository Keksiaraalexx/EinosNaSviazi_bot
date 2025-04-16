from aiogram import Bot

async def send_notification(bot: Bot, chat_id: int, text: str):
    await bot.send_message(chat_id=chat_id, text=text)
