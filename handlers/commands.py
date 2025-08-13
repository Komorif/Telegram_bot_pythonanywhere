from aiogram.types import BotCommand, BotCommandScopeChat
from aiogram import Router, types, Bot
from aiogram.filters import Command

from .images import *
from .keyboards.en_rus_keyboards import mainMenu_en_rus

router = Router()


# Меню команд бота
async def set_starting_commands(bot: Bot, chat_id: int):
    STARTING_COMMANDS = {
        "ru": [
            BotCommand(command="start", description="Команда start запускает бота, начать сначала"),
            BotCommand(command="help", description="Вывести информацию по боту"),
            BotCommand(command="id", description="Узнать свой id"),
            BotCommand(command="echo", description="Эхо"),
            BotCommand(command="games", description="Узнать какие есть игры"),
        ],
        "en": [
            BotCommand(command="start", description="Restart bot"),
            BotCommand(command="help", description="Info about bot"),
            BotCommand(command="id", description="Find your id"),
            BotCommand(command="echo", description="Echo"),
            BotCommand(command="games", description="Find out what games are available"),
        ]
    }
    for lang, commands in STARTING_COMMANDS.items():
	    await bot.set_my_commands(
		    commands=commands,
		    scope=BotCommandScopeChat(chat_id=chat_id),
		    language_code=lang
		)


# /start
# 1 меню выбор языка
@router.message(Command("start"))
async def command_start(message: types.Message):
    await message.answer_photo(photo=menu_one, caption="🇺🇸 / 🇷🇺", reply_markup=mainMenu_en_rus)
    await set_starting_commands(message.bot, message.from_user.id)


# /help
@router.message(Command("help"))
async def command_help(message: types.Message):
    if message.from_user.language_code == "ru":
	    await message.answer("Вы можете использовать меня для загрузки игр, посмотреть наш Youtube, Discord и т.д.😲")
    elif message.from_user.language_code == "en":
	    await message.answer("You can use me for download games, see our Youtube, Discord etc.😲")


# /id
@router.message(Command("id"))
async def command_id(message: types.Message):
    if message.from_user.language_code == "ru":
        await message.answer(f"Ваш id: {message.from_user.id}")

    elif message.from_user.language_code == "en":
	    await message.answer(f"Your id: {message.from_user.id}")


# /echo
@router.message(Command("echo"))
async def command_echo(message: types.Message):
    if message.from_user.language_code == "ru":
        await message.answer("Если отправить что-то из этого списка"
        					"\n1. Смайлик\n2. Эмоджи\n3. Gif\n4. Видео"
        					"\n4. Фото\n5. Голосовое сообщение\n\nБот отправит вам его в ответ")

    elif message.from_user.language_code == "en":
        await message.answer("If you send something from this list"
        					"\n1. Smiley face\n2. Emoji\n3. Gif\n4. Video"
        					"\n4. Picture\n5. Voice message\n\nBot will send it back to you")


# /games
@router.message(Command("games"))
async def command_games(message: types.Message):
    if message.from_user.language_code == "ru":
        await message.answer("ANDROID\n1. Cars\n2. Mosaic\n\nPC\n1. Calculator\n2. ES MOD\n\nWEB GAMES\nПока нет")

    elif message.from_user.language_code == "en":
        await message.answer("ANDROID\n1. Cars\n2. Mosaic\n\nPC\n1. Calculator\n2. ES MOD\n\nWEB GAMES\nNot yet")