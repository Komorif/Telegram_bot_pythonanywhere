from aiogram import Router, types, F

from ..images import *
from ..keyboards import *
from .keyboard_editing import edit_message

router = Router()

# Отдельный back с mainmenu на выбор языков rus
@router.callback_query(F.data.contains("rus_back_mainMenu"))
async def lang_rus_back(call: types.CallbackQuery):

	image = menu_one
	if call.data == "rus_back_mainMenu":
		await edit_message(call, photo=image, caption="🇺🇸 / 🇷🇺", kb=mainMenu_en_rus)

# Russian
@router.callback_query(F.data.contains("rus_back_"))
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
@router.callback_query(F.data.contains("rus_in_"))
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