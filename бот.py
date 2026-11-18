import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.enums import ParseMode

# --- НАСТРОЙКИ ---
BOT_TOKEN = "ВАШ_ТОКЕН_ОТ_BOTFATHER"
STICKER_ID = "СЮДА_ВСТАВЬТЕ_FILE_ID_СТИКЕРА"  # Получите, отправив стикер боту
WEBAPP_URL = "https://ваш-сайт.com/miniapp"  # Ссылка на ваше мини-приложение
# -----------------

dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    # 1. Отправляем текст
    await message.answer("Забирай звезды")
    
    # 2. Отправляем стикер по file_id
    await message.answer_sticker(sticker=STICKER_ID)
    
    # 3. Отправляем кнопку-ссылку на мини-приложение
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Открыть приложение", web_app=WebAppInfo(url=WEBAPP_URL))]
        ]
    )
    await message.answer("Нажми на кнопку ниже:", reply_markup=keyboard)

# Вспомогательный хэндлер: пришлите боту стикер, чтобы узнать его file_id
@dp.message(F.sticker)
async def get_sticker_id(message: Message):
    await message.answer(f"`{message.sticker.file_id}`", parse_mode=ParseMode.MARKDOWN)

async def main():
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
