from aiogram.utils import executor

import logging
from aiogram import Bot, Dispatcher, types, executor

from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, callback_query

# Объекты для команд бота
from aiogram.types import BotCommand, BotCommandScopeChat

from aiogram.types import InputMediaPhoto

from aiogram.utils.markdown import link

from aiogram import types

from keyboards import *

TOKEN = "your token"
logging.basicConfig(level=logging.INFO)


# прокси
proxy_url = "your proxy_url"


bot = Bot(token=TOKEN, proxy=proxy_url)
dp = Dispatcher(bot)


# Функция (запуск бота)
async def on_startup(dp):
	await bot.send_message(your id, "Я запустился")

# Функция (выключение бота)
async def on_shutdown(dp):
	await bot.send_message(your id, "Я завершил работу")


# Картинки для менюшек
menu_one = ("https://downloader.disk.yandex.ru/preview/711bb1adff875b15eb27bc2e953f8d0b36a69eecb3a2ca4648143ee0aa223585"
			"/63c1af3e/_6tncDV3aVZTsQg0TZbCornwjRjeQl6Sbl7ryrTKPw9pPdoQLXcQ1r0Yu5Untrt8SGGTmFGHYgs8E_rm6dSkYA%3D%3D?uid=0&"
			"filename=menu_one.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")

ios = ("https://downloader.disk.yandex.ru/preview/5b42c746b53921a74847b49334ef13e01f2864a5e758af36484f783248b9f5f8"
		"/63c1af84/1iEydv63EpJWU_e7x7LDfqX3ATg9TGRKmTLY0YJUpIRbS974E5ceNrIrAqGV3o-TvDf9AYWnpGhBpJ15kq8vPw%3D%3D?uid=0&"
		"filename=ios.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")

android = ("https://downloader.disk.yandex.ru/preview/5f590d1bcdda15d56e668bba0c430c5714439e97a3e188401357306c4b101eb2"
		"/63c1afb3/lsX9zrLWoYPzhyZU41o5w6X3ATg9TGRKmTLY0YJUpITesx_k25DxwZNvFQTOTgbNV1IjEwIpXQ4ssHZ9Bk8ywg%3D%3D?uid=0&"
		"filename=android.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")

pc = ("https://downloader.disk.yandex.ru/preview/c2f1fbb4c7d3c2a355d7d61785ab22188ea5f22530e92a1f322a740a6501e478"
		"/63c1afe4/MNQlWgSL62OIKo3AGtl_v6X3ATg9TGRKmTLY0YJUpIQD6nmvIEl_RH7MzyL3Flp8Iowu8MDThx2y9aZ5ZE9loQ%3D%3D?uid=0&"
		"filename=pc.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")

google_play = ("https://downloader.disk.yandex.ru/preview/96cff67912e20350583aa5e39a9bc6a0994ec30ef871a46c4a8444dde4134963"
		"/63d53985/lw9UVvCoowbEvBhKKB6sLYaa__hDX-jp_fjofm25VinHzXea_bSmCdK1PkFvjK4JS2ihJDr4UrHs0TjYNz4i8w%3D%3D?uid=0&"
		"filename=google_play.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")

faq = ("https://downloader.disk.yandex.ru/preview/87f33def26b09db3e18c3dd2f3137cd3a43a08c83c2f6a02301fbd6035c6615a"
		"/63c1b002/cVQro105INirqiPWEro9H6X3ATg9TGRKmTLY0YJUpISHHAmrL6lUr33tyAmW2_qwI3ZwRG3eV-ovVOZmbOYMhg%3D%3D?uid=0&"
		"filename=FAQ.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")


# Картинки для менюшек English
en_menu = ("https://downloader.disk.yandex.ru/preview/a41d6e5b6e080dca6a0b27e0a2e10a3b93ebc5249c3a3e1a8b96f65ddee0c5f2"
			"/63d43877/8tUqByIlKdFjR7xnNbgYj0aXDJB59eX7utlYUyhGcf13gQHfmnklgyCQDu03CMNZ4VgzQDxwqs7YESJ7RPvBRA%3D%3D?uid=0&"
			"filename=mainmenu.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")

en_social_network = ("https://downloader.disk.yandex.ru/preview/9e70fb7803245d98c211e0da3466d026bc57bd9a65ecd1a168ff36f3b8d0310c"
					"/63c1b070/nA_Tzw5hTAom4eLxCwtmX6X3ATg9TGRKmTLY0YJUpISRDKBSZerOmTeBwgs_AoTsQ8IeF_4aLiIgLFstdOiqBA%3D%3D?uid=0&"
					"filename=en_social_network.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")

en_donation = ("https://downloader.disk.yandex.ru/preview/47d815b9afdaeb8a78227244ae18100ec9ab26db7f47a2ea7ef7227f537f960a"
				"/63c1b091/iHeFI6ozuVm4jxnyqkivl6X3ATg9TGRKmTLY0YJUpIRp9GktWZbSD8CYW5bOoozojw2HsB_q8F2vChjF_ASPvA%3D%3D?uid=0&"
				"filename=en_donation.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")

en_mod_bl = ("https://downloader.disk.yandex.ru/preview/d77ef2bdff300f67bc3dfa76d428e50a2831c23fb027f785f3cc82c217bb504b"
			"/63c1b081/6CJXf9gXYkwgKeJuReORQbnwjRjeQl6Sbl7ryrTKPw94tzTUKvV07Tzv4_HOBQpduUo-Uz7qHopuycX_qB2HAA%3D%3D?uid=0&"
			"filename=en_mod_bl.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")

en_platform = ("https://downloader.disk.yandex.ru/preview/0856ad63f6b1604d107cf01f435a3acb2870138debf1a821202ec6296d1102d2"
				"/63c1b0b0/KniNQVNcyYLVfZFvpQk_VrnwjRjeQl6Sbl7ryrTKPw9aIHZN5gDMTD2IB6NuXpiPBDcKAuknVXsIhEAr2IoqVg%3D%3D?uid=0&"
				"filename=en_platform.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")

en_phone = ("https://downloader.disk.yandex.ru/preview/ab4d78a35c261ef702b4f7cc4b5831d77d86907a1d53d878232de22c9bcdf556"
			"/63d42a9a/sMY82TkfDdbpLU_KYp5ABHq9fksKA_u6Qdlxi1mzlvkYnKyNv5mu8n5nFdECD8WnvEzBXTA5xk_aVhWX8A57Vw%3D%3D?uid=0"
			"&filename=phone.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")

en_profile = ("https://downloader.disk.yandex.ru/preview/dce9ab49782fe5182a7772c6a3cc164b74c6b38cdfce13ae96691cb6c7fdc634"
				"/63c1b0a1/s0oqgq8sySb2pAGHKhdAv6X3ATg9TGRKmTLY0YJUpISzy3nZJGCDYSf3glLT8pfLn_NK5CQ3-BGJ0RYRMMG39Q%3D%3D?uid=0&"
				"filename=en_profile.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")

en_reviews = ("https://downloader.disk.yandex.ru/preview/2d19a70f37647c93e825757563cd3a70d1f2ef3e22c4391710ee7effd9fc20f4"
				"/64440b24/07vDvRdiGK_Umqb7K0OKYZasZUJ1CSLRvgRxCbeAmbQkcdGPgonO92JnLOw2u0F7vMvNy1yb2oGyucFpgZPOCw%3D%3D?uid=0&"
				"filename=en_reviews.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")


# Картинки для менюшек Russian
rus_menu = ("https://downloader.disk.yandex.ru/preview/170dd84ecdd0e02a097dcb64a021a97c445181048d4d1b22cccd10867a8e5041"
			"/63c1b46a/BEY3ThlvSC5pLmNSlclnc9-rcZs5RLWR3E1vERxC9CgFY7Czim8bvmNQ7ppNK1A8NTJ1cnQ4t8Wfgd1UHtE3Pw%3D%3D?uid=0&"
			"filename=rus_menu.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")

rus_social_network = ("https://downloader.disk.yandex.ru/preview/5e6eaa54cbd5d273ed746392430ee67368b115b52be709a92067dc7a6881bd80"
						"/63c1b04c/0MK89FED-4X2FcfnPeA9y6X3ATg9TGRKmTLY0YJUpITIE_sADpIQGmAA6lNp-D4kDRRADv9EHBTb8y2v7B6Tzw%3D%3D?uid=0&"
						"filename=rus_social_network.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")

rus_donation = ("https://downloader.disk.yandex.ru/preview/d27eae5cda0522b720a1374cb15fe70b00866d5002ee80c256100c31b6428754"
				"/63c1b024/lCvTYZkOtl_KiCVwROLU4aX3ATg9TGRKmTLY0YJUpIRAZFVTQVGzo0u5ul1B10bh_B9lSwVv1bqwwGwSeWABmw%3D%3D?uid=0&"
				"filename=rus_donation.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")

rus_mod_bl = ("https://downloader.disk.yandex.ru/preview/713634f417141a913e250c473364de52fefaf4c71ba50673bb99ea591e76b39b"
				"/63c1b013/ekNSf85xrnEWXBFg-lT1z7nwjRjeQl6Sbl7ryrTKPw_oUKVUk4sd2kC9uuhEYadBpyH1tpWLS4Q0Sv775Jf7Aw%3D%3D?uid=0&"
				"filename=rus_mod_bl.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")

rus_platform = ("https://downloader.disk.yandex.ru/preview/e0779c47f7523699a0550b0e831705cc9cd499b05323a175930a608a4b059d3c"
				"/64431dd2/Vrk10M4lxUmYpAxy9taM378RG94hQbd9Gv2UXx_WTEckVyY85790xKgkDYejJE6kHQEOr2LtAwefMMR0vek7JQ%3D%3D?uid=0&"
				"filename=rus_platform.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")

rus_phone = ("https://downloader.disk.yandex.ru/preview/51d2f367a1a41aa520cfc049eaec03d0d4c4212156a41f1daf28efa75fec1507"
			"/63d42ae4/IasrU8Hu2XzBVjdC6D6qZFBavCHoxKachbVWEqGMJmwxvAxbP3osMcrGPezZc3VuXhMOHAM2IACzYjAhChesVw%3D%3D?uid=0&"
			"filename=%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")

rus_profile = ("https://downloader.disk.yandex.ru/preview/6811da4964699788c99ae5bb69b41048387bc2d9c1f9e7cb8c5349d9404ec053"
				"/63c1b05b/YgAWFr1vJHk_O_uT15w--aX3ATg9TGRKmTLY0YJUpIRVDHxEdaip2EyFseskn7OsIQ737D4UmDZHbGTolY1g3A%3D%3D?uid=0&"
				"filename=rus_profile.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")

rus_reviews = ("https://downloader.disk.yandex.ru/preview/554650e7b6445d784db93fdfa0534767ba2c7e3f039a77be5b506478598012a6"
				"/64440788/BDCxFTBY55zKZIJUdHQScoi0ggHk1chw0tThiEIJG-y39tCiZLREiR88alTp-JTq-O_ysKUMBTx28G5bFAFCdw%3D%3D?uid=0&"
				"filename=reviews.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")

# Картинки для баннеров игры
calculator_card = ("https://downloader.disk.yandex.ru/preview/248584608d648df0d7d34d965eec779a8fbfd06e27ebe4fa3b183f750f77209d"
					"/644320b0/FSvNuN28p3ulGk-xcnTfKmRDTHquQMBdtdnjfjgvFfrt2JvOCZUwnKFsVhQNoXCzrf3KveM-3uN-InNkW5BuNw%3D%3D?uid=0&"
					"filename=calculator.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")

endless_summer_card = ("https://downloader.disk.yandex.ru/preview/c770decdf1a98e584fe94fbd40b597ef89990ebc6cd2fe1f802167eee08b37b6"
						"/64432857/CBxM-YisCnJlR74orLAowZfnTKFlkYr3bagiK8noXhjh8-PAXSjcLunb1haH48f9Vrqty3rRuC62549cqEXqXw%3D%3D?uid=0&"
						"filename=Everlasting_Summer_NdNfec8MxX.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048")

cars_card = ("https://downloader.disk.yandex.ru/preview/6606a14178f014918a4ea43977be328de17d9bf02d03790703dc185a1eb8307e"
				"/64432fd3/aG7xacNyFljOd_1gt2TP_H0z5pF4H_j88sf3649jAzy1QEw3BBqVF6UGMyh16yATbbsYpFaS8BZHafF9l2Ay5w%3D%3D?uid=0&"
				"filename=cars.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")

mosaic_card = ("https://downloader.disk.yandex.ru/preview/c671dec34ff65ef0c253545b682b351c71c47fe57ddc41fce90de70d343f381a"
				"/644330ed/XxOy4RGwmFLuyf83Ej6A5cGD5lx9DMHYfDyJ0VrtMkTouTdTjApFxDF2y-dgQyLozwrIIsA6h-u1WxikiysUgg%3D%3D?uid=0&"
				"filename=mosaic.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048")


# Менюшка команд бота
async def set_starting_commands(bot: Bot, chat_id: int):
    STARTING_COMMANDS = {
		"ru": [
			BotCommand("start", "Команда start запускает бота, начать сначала"), # /start
			BotCommand("help", "Вывести информацию по боту"), # /help
			BotCommand("id", "Узнать свой id"), # /id
			BotCommand("echo", "Эхо"), # /echo
			BotCommand("games", "Узнать какие есть игры"), # /games
		],
		"en": [
			BotCommand("start", "Restart bot"), # /start
			BotCommand("help", "Info about bot"), # /help
			BotCommand("id", "Find your id"), # /id
			BotCommand("echo", "Echo"), # /echo
			BotCommand("games", "Find out what games are available"), # /games
		]
	}
    for language, commands in STARTING_COMMANDS.items():
	    await bot.set_my_commands(
		    commands=commands,
		    scope=BotCommandScopeChat(chat_id),
		    language_code=language
		)



# /start
# 1 меню выбор языка
@dp.message_handler(commands="start")
async def command_start(message: types.Message):
    await bot.send_photo(message.from_user.id, photo=menu_one, caption="🇺🇸 / 🇷🇺", reply_markup=mainMenu_en_rus)
    await set_starting_commands(bot, message.from_user.id)



# /help
@dp.message_handler(commands="help")
async def command_help(message: types.Message):
    if message.from_user.language_code == "ru":
	    await message.answer("Вы можете использовать меня для загрузки игр, посмотреть наш Youtube, Discord и т.д.😲")

    elif message.from_user.language_code == "en":
	    await message.answer("You can use me for download games, see our Youtube, Discord etc.😲")


# /id
@dp.message_handler(commands="id")
async def command_id(message: types.Message):
    if message.from_user.language_code == "ru":
        await message.answer(f"Ваш id: {message.from_user.id}")

    elif message.from_user.language_code == "en":
	    await message.answer(f"Your id: {message.from_user.id}")


# /echo
@dp.message_handler(commands="echo")
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
@dp.message_handler(commands="games")
async def command_games(message: types.Message):
    if message.from_user.language_code == "ru":
        await message.answer("ANDROID\n1. Cars\n2. Mosaic\n\nPC\n1. Calculator\n2. ES MOD\n\nWEB GAMES\nПока нет")

    elif message.from_user.language_code == "en":
        await message.answer("ANDROID\n1. Cars\n2. Mosaic\n\nPC\n1. Calculator\n2. ES MOD\n\nWEB GAMES\nNot yet")



# Функция для редактирования инлайн клавиатур
async def edit_message(call: types.CallbackQuery, photo,
                       kb: InlineKeyboardMarkup, caption: str):

	image = InputMediaPhoto(photo)

	await call.message.edit_media(media=image)

	await call.message.edit_caption(caption, parse_mode="HTML")
	await call.message.edit_reply_markup(reply_markup=kb)



# /start
# 1 меню выбор языка
@dp.callback_query_handler(text_contains="start")
async def mainMenu_en_rus_two(call: types.CallbackQuery):

	image = menu_one
	if call.data == "mainMenu_en_rus":
		await edit_message(call, photo=image, caption="🇺🇸 / 🇷🇺", kb=mainMenu_en_rus)


# Итерация с кнопок English и Russian на их менюшки
@dp.callback_query_handler(text_contains="lang_")
async def lang_all(call: types.CallbackQuery):

	if call.data == "lang_en":
		image = en_menu
		await edit_message(call, photo=image, caption="MAIN MENU 🇺🇸", kb=en_mainMenu)

	elif call.data == "lang_rus":
		image = rus_menu
		await edit_message(call, photo=image, caption="ГЛАВНОЕ МЕНЮ 🇷🇺", kb=rus_mainMenu)



# Отдельный back с mainmenu на выбор языков en
@dp.callback_query_handler(text_contains="en_back_mainMenu")
async def lang_en_back(call: types.CallbackQuery):

	image = menu_one
	if call.data == "en_back_mainMenu":
		await edit_message(call, photo=image, caption="🇺🇸 / 🇷🇺", kb=mainMenu_en_rus)


# Отдельный back с mainmenu на выбор языков rus
@dp.callback_query_handler(text_contains="rus_back_mainMenu")
async def lang_rus_back(call: types.CallbackQuery):

	image = menu_one
	if call.data == "rus_back_mainMenu":
		await edit_message(call, photo=image, caption="🇺🇸 / 🇷🇺", kb=mainMenu_en_rus)



# English
# Отдельный back с mainmenu на выбор языков rus
@dp.callback_query_handler(text_contains="en_back_")
async def back_buttons_en(call: types.CallbackQuery):

	# Условия для всех назад кнопок назад (English)
	if call.data == "en_back_games":
		image = en_menu
		await edit_message(call, photo=image, caption="MAIN MENU 🇺🇸", kb=en_mainMenu)

	elif call.data == "en_back_ios":
		image = en_platform
		await edit_message(call, photo=image, caption=r"SELECT A PLATFORM 🇺🇸", kb=en_in_our_games)

	elif call.data == "en_back_android":
		image = en_platform
		await edit_message(call, photo=image, caption=r"SELECT A PLATFORM 🇺🇸", kb=en_in_our_games)

	elif call.data == "en_back_pc":
		image = en_platform
		await edit_message(call, photo=image, caption=r"SELECT A PLATFORM 🇺🇸", kb=en_in_our_games)

	elif call.data == "en_back_in_web_games":
		image = en_platform
		await edit_message(call, photo=image, caption=r"SELECT A PLATFORM 🇺🇸", kb=en_in_our_games)

	elif call.data == "en_back_in_pc_web_games":
		image = en_platform
		await edit_message(call, photo=image, caption=r"SELECT A PLATFORM 🇺🇸", kb=en_in_web_games)

	elif call.data == "en_back_in_phone_web_games":
		image = en_platform
		await edit_message(call, photo=image, caption=r"SELECT A PLATFORM 🇺🇸", kb=en_in_web_games)

	elif call.data == "en_back_in_google_play":
		image = android
		await edit_message(call, photo=image, caption="Choose any game you want to download 🇺🇸", kb=en_in_android)

	elif call.data == "en_back_mod":
		image = en_platform
		await edit_message(call, photo=image, caption=r"SELECT A PLATFORM 🇺🇸", kb=en_in_pc)

	elif call.data == "en_back_social":
		image = en_menu
		await edit_message(call, photo=image, caption="MAIN MENU 🇺🇸", kb=en_mainMenu)

	elif call.data == "en_back_faq":
		image = en_menu
		await edit_message(call, photo=image, caption="MAIN MENU 🇺🇸", kb=en_mainMenu)

	elif call.data == "en_back_prof":
		image = en_menu
		await edit_message(call, photo=image, caption="MAIN MENU 🇺🇸", kb=en_mainMenu)

	elif call.data == "en_back_donat":
		image = en_menu
		await edit_message(call, photo=image, caption="MAIN MENU 🇺🇸", kb=en_mainMenu)

	elif call.data == "en_back_in_pc_calculator":
		image = pc
		await edit_message(call, photo=image, caption="Choose any game you want to download 🇺🇸", kb=en_in_pc)

	elif call.data == "en_back_in_cars_two":
		image = android
		await edit_message(call, photo=image, caption="Choose any game you want to download 🇺🇸", kb=en_in_android)

	elif call.data == "en_back_in_mosaic":
		image = android
		await edit_message(call, photo=image, caption="Choose any game you want to download 🇺🇸", kb=en_in_android)

	elif call.data == "en_back_in_reviews":
		image = en_menu
		await edit_message(call, photo=image, caption="MAIN MENU 🇺🇸", kb=en_mainMenu)


# Все inline клавиатуры inline en_in_ перед каждой English
@dp.callback_query_handler(text_contains="en_in_")
async def it_buttons_en(call: types.CallbackQuery):

	# Условия для всех назад кнопок rus_in_ (English)
    if call.data == "en_in_our_games":
    	image = en_platform
    	await edit_message(call, photo=image, caption=r"SELECT A PLATFORM 🇺🇸", kb=en_in_our_games)

    elif call.data == "en_in_ios":
    	image = ios
    	await edit_message(call, photo=image, caption="Choose any game you want to download 🇺🇸", kb=en_in_ios)

    elif call.data == "en_in_android":
    	image = android
    	await edit_message(call, photo=image, caption="Choose any game you want to download 🇺🇸", kb=en_in_android)

    elif call.data == "en_in_pc":
    	image = pc
    	await edit_message(call, photo=image, caption="Choose any game you want to download 🇺🇸", kb=en_in_pc)

    elif call.data == "en_in_web_games":
    	image = en_platform
    	await edit_message(call, photo=image, caption=r"SELECT A PLATFORM 🇺🇸", kb=en_in_web_games)

    elif call.data == "en_in_pc_web_games":
    	image = pc
    	await edit_message(call, photo=image, caption="Pick any game you want 🇺🇸", kb=en_in_pc_web_games)

    elif call.data == "en_in_phone_web_games":
    	image = en_phone
    	await edit_message(call, photo=image, caption="Pick any game you want 🇺🇸", kb=en_in_phone_web_games)

    elif call.data == "en_in_mod_bl":
    	image = endless_summer_card
    	await edit_message(call, photo=image, caption="MOD FOR ENDLESS SUMMER 🇺🇸", kb=en_in_mod_bl)

    elif call.data == "en_in_google_play":
    	image = google_play
    	await edit_message(call, photo=image, caption="GOOGLE PLAY 🇺🇸", kb=en_in_google_play)

    elif call.data == "en_in_social_network":
    	image = en_social_network
    	await edit_message(call, photo=image, caption="SOCIAL MEDIA 🇺🇸", kb=en_in_social_network)

    elif call.data == "en_in_FAQ":
    	image = faq
    	await edit_message(call, photo=image, caption="We have answered frequently asked questions for your convenience"
														'<a href="your telegraph"> here</a> 🇺🇸',
														kb=en_in_FAQ)

    elif call.data == "en_in_Profile":
    	image = en_profile
    	await edit_message(call, photo=image, caption="You are a human being. \nGood luck using the bot 🇺🇸", kb=en_in_Profile)

    elif call.data == "en_in_donation":
    	image = en_donation
    	await edit_message(call, photo=image, caption="You can help us be better 🇺🇸", kb=en_in_donation)

    elif call.data == "en_in_pc_calculator":
    	image = calculator_card
    	await edit_message(call, photo=image, caption="This application was created ONLY for Windows."
    													"\nWith this calculator you can perform simple operations such as addition,"
    													"division, subtraction, etc. 🇺🇸",
    													kb=en_in_pc_calculator)

    elif call.data == "en_in_cars_two":
    	image = cars_card
    	await edit_message(call, photo=image, caption="Download the game cars two 🇺🇸", kb=en_in_cars_two)

    elif call.data == "en_in_mosaic":
    	image = mosaic_card
    	await edit_message(call, photo=image, caption="Download the game Mosaic 🇺🇸", kb=en_in_mosaic)

    elif call.data == "en_in_reviews":
    	image = en_reviews
    	await edit_message(call, photo=image, caption='We have a separate <a href="https://t.me/+oemeUSzhSv44YmIy">chat room</a>'
														" with the reviews of our games, where everyone can leave their feedback"
														'\nTo see the reviews, click on – <a href="https://t.me/+oemeUSzhSv44YmIy"> here</a> 🇺🇸',
														kb=en_in_reviews)



# Russian
@dp.callback_query_handler(text_contains="rus_back_")
async def back_buttons_rus(call: types.CallbackQuery):

	# Условия для всех назад кнопок назад (Russian)
    if call.data == "rus_back_games":
    	image = rus_menu
    	await edit_message(call, photo=image, caption="ГЛАВНОЕ МЕНЮ 🇷🇺", kb=rus_mainMenu)

    elif call.data == "rus_back_ios":
    	image = rus_platform
    	await edit_message(call, photo=image, caption="ВЫВЕРИТЕ ПЛАТФОРМУ 🇷🇺", kb=rus_in_our_games)

    elif call.data == "rus_back_android":
    	image = rus_platform
    	await edit_message(call, photo=image, caption="ВЫВЕРИТЕ ПЛАТФОРМУ 🇷🇺", kb=rus_in_our_games)

    elif call.data == "rus_back_pc":
    	image = rus_platform
    	await edit_message(call, photo=image, caption="ВЫВЕРИТЕ ПЛАТФОРМУ 🇷🇺", kb=rus_in_our_games)

    elif call.data == "rus_back_in_web_games":
    	image = rus_platform
    	await edit_message(call, photo=image, caption="ВЫВЕРИТЕ ПЛАТФОРМУ 🇷🇺", kb=rus_in_our_games)

    elif call.data == "rus_back_in_pc_web_games":
    	image = rus_platform
    	await edit_message(call, photo=image, caption="ВЫВЕРИТЕ ПЛАТФОРМУ 🇷🇺", kb=rus_in_web_games)

    elif call.data == "rus_back_in_phone_web_games":
    	image = rus_platform
    	await edit_message(call, photo=image, caption="ВЫВЕРИТЕ ПЛАТФОРМУ 🇷🇺", kb=rus_in_web_games)

    elif call.data == "rus_back_in_google_play":
    	image = android
    	await edit_message(call, photo=image, caption="Выбирай любую игру какую хочешь скачать 🇷🇺", kb=rus_in_android)

    elif call.data == "rus_back_mod":
    	image = rus_platform
    	await edit_message(call, photo=image, caption="ВЫВЕРИТЕ ПЛАТФОРМУ 🇷🇺", kb=rus_in_pc)

    elif call.data == "rus_back_social":
    	image = rus_menu
    	await edit_message(call, photo=image, caption="ГЛАВНОЕ МЕНЮ 🇷🇺", kb=rus_mainMenu)

    elif call.data == "rus_back_faq":
    	image = rus_menu
    	await edit_message(call, photo=image, caption="ГЛАВНОЕ МЕНЮ 🇷🇺", kb=rus_mainMenu)

    elif call.data == "rus_back_prof":
    	image = rus_menu
    	await edit_message(call, photo=image, caption="ГЛАВНОЕ МЕНЮ 🇷🇺", kb=rus_mainMenu)

    elif call.data == "rus_back_donat":
    	image = rus_menu
    	await edit_message(call, photo=image, caption="ГЛАВНОЕ МЕНЮ 🇷🇺", kb=rus_mainMenu)

    elif call.data == "rus_back_in_pc_calculator":
    	image = pc
    	await edit_message(call, photo=image, caption="Выбирай любую игру какую хочешь скачать 🇷🇺", kb=rus_in_pc)

    elif call.data == "rus_back_in_cars_two":
    	image = android
    	await edit_message(call, photo=image, caption="Выбирай любую игру какую хочешь скачать 🇷🇺", kb=rus_in_android)

    elif call.data == "rus_back_in_mosaic":
    	image = android
    	await edit_message(call, photo=image, caption="Выбирай любую игру какую хочешь скачать 🇷🇺", kb=rus_in_android)

    elif call.data == "rus_back_in_reviews":
    	image = rus_menu
    	await edit_message(call, photo=image, caption="ГЛАВНОЕ МЕНЮ 🇷🇺", kb=rus_mainMenu)


# Все inline клавиатуры inline en_in_ перед каждой English
@dp.callback_query_handler(text_contains="rus_in_")
async def it_buttons_rus(call: types.CallbackQuery):

	# Условия для всех назад кнопок rus_in_ (Russian)
    if call.data == "rus_in_our_games":
    	image = rus_platform
    	await edit_message(call, photo=image, caption="ВЫБЕРИТЕ ПЛАТФОРМУ 🇷🇺", kb=rus_in_our_games)

    elif call.data == "rus_in_ios":
    	image = ios
    	await edit_message(call, photo=image, caption="Выбирай любую игру какую хочешь скачать 🇷🇺", kb=rus_in_ios)

    elif call.data == "rus_in_android":
    	image = android
    	await edit_message(call, photo=image, caption="Выбирай любую игру какую хочешь скачать 🇷🇺", kb=rus_in_android)

    elif call.data == "rus_in_pc":
    	image = pc
    	await edit_message(call, photo=image, caption="Выбирай любую игру какую хочешь скачать 🇷🇺", kb=rus_in_pc)

    elif call.data == "rus_in_web_games":
    	image = rus_platform
    	await edit_message(call, photo=image, caption="ВЫБЕРИТЕ ПЛАТФОРМУ 🇷🇺", kb=rus_in_web_games)

    elif call.data == "rus_in_pc_web_games":
    	image = pc
    	await edit_message(call, photo=image, caption="Выбирай любую игру какую хочешь 🇷🇺", kb=rus_in_pc_web_games)

    elif call.data == "rus_in_phone_web_games":
    	image = rus_phone
    	await edit_message(call, photo=image, caption="Выбирай любую игру какую хочешь 🇷🇺", kb=rus_in_phone_web_games)

    elif call.data == "rus_in_mod_bl":
    	image = endless_summer_card
    	await edit_message(call, photo=image, caption="МОД НА БЕСКНОНЕЧНОГО ЛЕТО 🇷🇺", kb=rus_in_mod_bl)

    elif call.data == "rus_in_google_play":
    	image = google_play
    	await edit_message(call, photo=image, caption="GOOGLE PLAY 🇷🇺", kb=rus_in_google_play)

    elif call.data == "rus_in_social_network":
    	image = rus_social_network
    	await edit_message(call, photo=image, caption="СОЦИАЛЬНЫЕ СЕТИ 🇷🇺", kb=rus_in_social_network)

    elif call.data == "rus_in_FAQ":
    	image = faq
    	await edit_message(call, photo=image, caption="Мы ответили на часто задаваемые вопросы для вашего удобства"
														'<a href="your telegraph"> тут</a> 🇷🇺',
														kb=rus_in_FAQ)

    elif call.data == "rus_in_Profile":
    	image = rus_profile
    	await edit_message(call, photo=image, caption="Вы человек \nЖелаем удачи в пользовании ботом 🇷🇺", kb=rus_in_Profile)

    elif call.data == "rus_in_donation":
    	image = rus_donation
    	await edit_message(call, photo=image, caption="Вы можете помочь нам стать лучше 🇷🇺", kb=rus_in_donation)

    elif call.data == "rus_in_pc_calculator":
    	image = calculator_card
    	await edit_message(call, photo=image, caption="Это приложение было создано ТОЛЬКО для Windows."
    													"\nС помощью этого калькулятора вы можете выполнять простые операции,"
    													"такие как сложение, деление, вычитание и т.д. 🇷🇺",
    													kb=rus_in_pc_calculator)

    elif call.data == "rus_in_cars_two":
    	image = cars_card
    	await edit_message(call, photo=image, caption="Скачать игру Cars two 🇷🇺", kb=rus_in_cars_two)

    elif call.data == "rus_in_mosaic":
    	image = mosaic_card
    	await edit_message(call, photo=image, caption="Скачать игру Mosaic 🇷🇺", kb=rus_in_mosaic)

    elif call.data == "rus_in_reviews":
    	image = rus_reviews
    	await edit_message(call, photo=image, caption='У нас есть <a href="https://t.me/+gaRe71AYudBmMTRi">чат </a>'
    													"с отзывами наших игр, где каждый может оставить свой отзыв"
    													'\nЧтобы посмотреть отзывы нажми – <a href="https://t.me/+gaRe71AYudBmMTRi"> здесь</a> 🇷🇺',
														kb=rus_in_reviews)



# Продвинутое эхо
@dp.message_handler(content_types=[
	types.ContentType.DOCUMENT, types.ContentType.PHOTO,
	types.ContentType.STICKER, types.ContentType.VIDEO,
	types.ContentType.TEXT,  types.ContentType.ANIMATION,
	types.ContentType.VOICE
])
async def download_doc(message: types.Message):
	if "document" in message:
		await message.answer_document(message.document.file_id)

	elif "photo" in message:
		await message.answer_photo(message.photo[-1].file_id)

	elif "sticker" in message:
		await message.answer_sticker(message.sticker.file_id)

	elif "video" in message:
		await message.answer_video(message.video.file_id)

	elif "text" in message:
	    await message.answer(message.text)

	# Голосовое сообщение
	elif "voice" in message:
	    await message.answer_voice(message.voice.file_id)



# Register dispather
def register_handlers_client(dp : Dispatcher):
  dp.register_message_handler(command_start, commands=["start"])

if __name__ == "__main__":
	executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)