from aiogram import Router, types, F

from ..images import *
from ..keyboards import *
from .keyboard_editing import edit_message

router = Router()

# Отдельный back с mainmenu на выбор языков en
@router.callback_query(F.data.contains("en_back_mainMenu"))
async def lang_en_back(call: types.CallbackQuery):
	image = menu_one
	if call.data == "en_back_mainMenu":
		await edit_message(call, photo=image, caption="🇺🇸 / 🇷🇺", kb=mainMenu_en_rus)

# English
# Отдельный back с mainmenu на выбор языков rus
@router.callback_query(F.data.contains("en_back_"))
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
@router.callback_query(F.data.contains("en_in_"))
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