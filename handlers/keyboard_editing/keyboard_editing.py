from aiogram import Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto

from ..images import *
from ..keyboards import *

router = Router()

# Функция для редактирования инлайн клавиатур
async def edit_message(call: CallbackQuery, photo,
                       kb: InlineKeyboardMarkup, caption: str):
	media = InputMediaPhoto(media=photo, caption=caption, parse_mode="HTML")
	await call.message.edit_media(media=media, reply_markup=kb)


# Меню выбор языка
@router.callback_query(F.data.contains("start"))
async def mainMenu_en_rus_two(call: CallbackQuery):
    image = menu_one
    if call.data == "mainMenu_en_rus":
        await edit_message(call, photo=image, caption="🇺🇸 / 🇷🇺", kb=mainMenu_en_rus)


# Итерация с кнопок English и Russian на их менюшки
@router.callback_query(F.data.contains("lang_"))
async def lang_all(call: CallbackQuery):
	if call.data == "lang_en":
		image = en_menu
		await edit_message(call, photo=image, caption="MAIN MENU 🇺🇸", kb=en_mainMenu)
	elif call.data == "lang_rus":
		image = rus_menu
		await edit_message(call, photo=image, caption="ГЛАВНОЕ МЕНЮ 🇷🇺", kb=rus_mainMenu)