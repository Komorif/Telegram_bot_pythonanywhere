from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, callback_query


# Клавиатура номер 1 (выбором языка)
mainMenu_en_rus = InlineKeyboardMarkup(row_width=2)
lang_en = InlineKeyboardButton(text="English 🇺🇸", callback_data="lang_en")
lang_rus = InlineKeyboardButton(text="Russian 🇷🇺", callback_data="lang_rus")

mainMenu_en_rus.add(lang_en).add(lang_rus)


# Клавиатура номер 1.2 (выбором языка)
mainMenu_en_rus_two = InlineKeyboardMarkup(row_width=2)
lang_rus_two = InlineKeyboardButton(text="Russian 🇷🇺", callback_data="lang_rus_two")
lang_en_two = InlineKeyboardButton(text="English 🇺🇸", callback_data="lang_en_two")

mainMenu_en_rus_two.add(lang_en_two)
mainMenu_en_rus_two.add(lang_rus_two)




# English
# Клавиатура номер 1 (English_main_menu)
en_mainMenu = InlineKeyboardMarkup(row_width=2)
en_in_our_games = InlineKeyboardButton(text="Our games 🎮", callback_data="en_in_our_games")
en_in_social_network = InlineKeyboardButton(text="Social Media 🌍", callback_data="en_in_social_network")
en_in_Profile = InlineKeyboardButton(text="Profile 🧒", callback_data="en_in_Profile")
en_in_FAQ = InlineKeyboardButton(text="FAQ❓", callback_data="en_in_FAQ")
en_in_reviews = InlineKeyboardButton(text="Reviews ✏", callback_data="en_in_reviews")
en_in_donation = InlineKeyboardButton(text="Support 💰", callback_data="en_in_donation")
en_back_mainMenu = InlineKeyboardButton(text="Back", callback_data="en_back_mainMenu")

en_mainMenu.add(en_in_our_games, en_in_social_network).add(en_in_Profile, en_in_FAQ)
en_mainMenu.add(en_in_reviews, en_in_donation)
en_mainMenu.add(en_back_mainMenu)


# Клавиатура номер 2 (Наши игры)
en_in_our_games = InlineKeyboardMarkup(row_width=2)
en_in_ios = InlineKeyboardButton(text="IOS 🍏", callback_data="en_in_ios")
en_in_android = InlineKeyboardButton(text="ANDROID 🤖", callback_data="en_in_android")
en_in_pc = InlineKeyboardButton(text="PC 🖥️", callback_data="en_in_pc")
en_in_web_games = InlineKeyboardButton(text="WEB GAMES 🎮", callback_data="en_in_web_games")
en_back_games = InlineKeyboardButton(text="Back", callback_data="en_back_games")

en_in_our_games.add(en_in_ios, en_in_android)
en_in_our_games.add(en_in_pc, en_in_web_games)
en_in_our_games.add(en_back_games)


# Клавиатура номер 3 (ios)
en_in_ios = InlineKeyboardMarkup(row_width=2)
en_back_ios = InlineKeyboardButton(text="Back", callback_data="en_back_ios")

en_in_ios.add(en_back_ios)


# Клавиатура номер 4 (android)
en_in_android = InlineKeyboardMarkup(row_width=2)
en_in_google_play = InlineKeyboardButton(text="GOOGLE PLAY 👾", callback_data="en_in_google_play")
en_in_cars_two = InlineKeyboardButton(text="Cars 🚗", callback_data="en_in_cars_two")
en_in_mosaic = InlineKeyboardButton(text="Mosaic 🧠", callback_data="en_in_mosaic")
en_back_android = InlineKeyboardButton(text="Back", callback_data="en_back_android")

en_in_android.add(en_in_google_play, en_in_cars_two)
en_in_android.add(en_in_mosaic)
en_in_android.add(en_back_android)


# Клавиатура номер 5 (pc)
en_in_pc = InlineKeyboardMarkup(row_width=2)
en_in_pc_calculator = InlineKeyboardButton(text="Calculator C#", callback_data="en_in_pc_calculator")
en_in_mod_bl = InlineKeyboardButton(text="ES MOD 🧚‍♂️", callback_data="en_in_mod_bl")
en_back_pc = InlineKeyboardButton(text="Back", callback_data="en_back_pc")

en_in_pc.add(en_in_mod_bl, en_in_pc_calculator)
en_in_pc.add(en_back_pc)


# Клавиатура номер 6 (web_games)
en_in_web_games = InlineKeyboardMarkup(row_width=2)
en_in_pc_web_games = InlineKeyboardButton(text="PC 🖥️", callback_data="en_in_pc_web_games")
en_in_phone_web_games = InlineKeyboardButton(text="PHONE 📱", callback_data="en_in_phone_web_games")
en_back_in_web_games= InlineKeyboardButton(text="Back", callback_data="en_back_in_web_games")

en_in_web_games.add(en_in_pc_web_games, en_in_phone_web_games)
en_in_web_games.add(en_back_in_web_games)


# Клавиатура номер 7 (pc_web_games)
en_in_pc_web_games = InlineKeyboardMarkup(row_width=2)
en_back_in_pc_web_games = InlineKeyboardButton(text="Back", callback_data="en_back_in_pc_web_games")

en_in_pc_web_games.add(en_back_in_pc_web_games)


# Клавиатура номер 8 (phone_web_games)
en_in_phone_web_games = InlineKeyboardMarkup(row_width=2)
en_back_in_phone_web_games = InlineKeyboardButton(text="Back", callback_data="en_back_in_phone_web_games")

en_in_phone_web_games.add(en_back_in_phone_web_games)


# Клавиатура номер 9 (google_play)
en_in_google_play = InlineKeyboardMarkup(row_width=2)
en_back_in_google_play = InlineKeyboardButton(text="Back", callback_data="en_back_in_google_play")

en_in_google_play.add(en_back_in_google_play)


# Клавиатура номер 10 (социальные сети)
en_in_social_network = InlineKeyboardMarkup(row_width=2)
en_in_youtube_one = InlineKeyboardButton(text="YOUTUBE 1 📺", url="https://www.youtube.com/channel/UC9EJAIYe4sL0iGB_huHTqHw", callback_data="en_in_youtube_one")
en_in_youtube_two = InlineKeyboardButton(text="YOUTUBE 2 📺", url="https://www.youtube.com/channel/UCb2GlPOgqB_VpWTvQM_dzKg", callback_data="en_in_youtube_two")
en_in_twitch = InlineKeyboardButton(text="TWITCH 🔴", url="https://www.twitch.tv/komorifn", callback_data="en_in_twitch")
en_in_discord = InlineKeyboardButton(text="DISCORD 🗣️", url="https://discord.gg/2pbCpNcDZm", callback_data="en_in_discord")
en_in_github = InlineKeyboardButton(text="GITHUB 💣", url="https://github.com/Komorif", callback_data="en_in_github")
en_in_vk = InlineKeyboardButton(text="VK ✔️", url="https://vk.com/komorilfg", callback_data="en_in_vk")
en_back_social = InlineKeyboardButton(text="Back", callback_data="en_back_social")

en_in_social_network.add(en_in_youtube_one, en_in_youtube_two).add(en_in_twitch, en_in_discord)
en_in_social_network.add(en_in_github, en_in_vk)
en_in_social_network.add(en_back_social)


# Клавиатура номер 11 (FAQ)
en_in_FAQ = InlineKeyboardMarkup(row_width=2)
en_back_faq = InlineKeyboardButton(text="Back", callback_data="en_back_faq")

en_in_FAQ.add(en_back_faq)


# Клавиатура номер 12 (Профиль)
en_in_Profile = InlineKeyboardMarkup(row_width=2)
en_back_prof = InlineKeyboardButton(text="Back", callback_data="en_back_prof")

en_in_Profile.add(en_back_prof)


# Клавиатура номер 13 (Пожертвования)
en_in_donation = InlineKeyboardMarkup(row_width=2)
en_in_donation_in = InlineKeyboardButton(text="Donation 💰", url="https://www.donationalerts.com/r/fetchy74", callback_data="en_in_donation_in")
en_back_donat = InlineKeyboardButton(text="Back", callback_data="en_back_donat")

en_in_donation.add(en_in_donation_in)
en_in_donation.add(en_back_donat)


# Клавиатура номер 14 (Отзывы)
en_in_reviews = InlineKeyboardMarkup(row_width=2)
en_back_in_reviews = InlineKeyboardButton(text="Back", callback_data="en_back_in_reviews")

en_in_reviews.add(en_back_in_reviews)



# PC
# Клавиатура номер 1.1 (Мод БЛ)
en_in_mod_bl = InlineKeyboardMarkup(row_width=2)
en_in_mod_bl_button_download = InlineKeyboardButton(text="Download mod for the game ES 🧚‍♂️", url="https://disk.yandex.ru/d/XmU8R4pGdsiuIA", callback_data="en_in_mod_bl_downl")
en_back_mod = InlineKeyboardButton(text="Back", callback_data="en_back_mod")

en_in_mod_bl.add(en_in_mod_bl_button_download)
en_in_mod_bl.add(en_back_mod)


# Клавиатура 1.2 (Карточка Калькулятор)
en_in_pc_calculator = InlineKeyboardMarkup(row_width=2)
en_in_pc_calculator_button_download = InlineKeyboardButton(text="Download", url="https://disk.yandex.ru/d/rDZ7E98l2uj8YA", callback_data="en_in_pc_calculator_button_download")
en_back_in_pc_calculator = InlineKeyboardButton(text="Back", callback_data="en_back_in_pc_calculator")

en_in_pc_calculator.add(en_in_pc_calculator_button_download)
en_in_pc_calculator.add(en_back_in_pc_calculator)



# Android
# Клавиатура номер 1.1 (Машины)
en_in_cars_two = InlineKeyboardMarkup(row_width=2)
en_in_android_cars_two_button_download = InlineKeyboardButton(text="Download", url="https://disk.yandex.ru/d/rDZ7E98l2uj8YA", callback_data="en_in_android_cars_two_button_download")
en_back_in_cars_two = InlineKeyboardButton(text="Back", callback_data="en_back_in_cars_two")

en_in_cars_two.add(en_in_android_cars_two_button_download)
en_in_cars_two.add(en_back_in_cars_two)



# Клавиатура номер 1.2 (Мозаика)
en_in_mosaic = InlineKeyboardMarkup(row_width=2)
en_in_android_mosaic_button_download = InlineKeyboardButton(text="Download", url="https://disk.yandex.ru/d/G2b7dN2O8vFd7g", callback_data="en_in_android_mosaic_button_download")
en_back_in_mosaic = InlineKeyboardButton(text="Back", callback_data="en_back_in_mosaic")

en_in_mosaic.add(en_in_android_mosaic_button_download)
en_in_mosaic.add(en_back_in_mosaic)




# Russian
# Клавиатура номер 1 (Russian_main_menu)
rus_mainMenu = InlineKeyboardMarkup(row_width=2)
rus_in_our_games = InlineKeyboardButton(text="Наши игры 🎮", callback_data="rus_in_our_games")
rus_in_social_network = InlineKeyboardButton(text="Социалки 🌍", callback_data="rus_in_social_network")
rus_in_Profile = InlineKeyboardButton(text="Профиль 🧒", callback_data="rus_in_Profile")
rus_in_FAQ = InlineKeyboardButton(text="FAQ❓", callback_data="rus_in_FAQ")
rus_in_reviews = InlineKeyboardButton(text="Отзывы ✏", callback_data="rus_in_reviews")
rus_in_donation = InlineKeyboardButton(text="Поддержка 💰", callback_data="rus_in_donation")
rus_back_mainMenu = InlineKeyboardButton(text="Назад",  callback_data="rus_back_mainMenu")

rus_mainMenu.add(rus_in_our_games, rus_in_social_network).add(rus_in_Profile, rus_in_FAQ)
rus_mainMenu.add(rus_in_reviews, rus_in_donation)
rus_mainMenu.add(rus_back_mainMenu)


# Клавиатура номер 2 (Наши игры)
rus_in_our_games = InlineKeyboardMarkup(row_width=2)
rus_in_ios = InlineKeyboardButton(text="IOS 🍏", callback_data="rus_in_ios")
rus_in_android = InlineKeyboardButton(text="ANDROID 🤖", callback_data="rus_in_android")
rus_in_pc = InlineKeyboardButton(text="PC 🖥️", callback_data="rus_in_pc")
rus_in_web_games = InlineKeyboardButton(text="WEB GAMES 🎮", callback_data="rus_in_web_games")
rus_back_games = InlineKeyboardButton(text="Назад", callback_data="rus_back_games")

rus_in_our_games.add(rus_in_ios, rus_in_android)
rus_in_our_games.add(rus_in_pc, rus_in_web_games)
rus_in_our_games.add(rus_back_games)


# Клавиатура номер 3 (ios)
rus_in_ios = InlineKeyboardMarkup(row_width=2)
rus_back_ios = InlineKeyboardButton(text="Назад", callback_data="rus_back_ios")

rus_in_ios.add(rus_back_ios)


# Клавиатура номер 4 (android)
rus_in_android = InlineKeyboardMarkup(row_width=2)
rus_in_google_play = InlineKeyboardButton(text="GOOGLE PLAY 👾", callback_data="rus_in_google_play")
rus_in_cars_two = InlineKeyboardButton(text="Cars 🚗", callback_data="rus_in_cars_two")
rus_in_mosaic = InlineKeyboardButton(text="Mosaic 🧠", callback_data="rus_in_mosaic")
rus_back_android = InlineKeyboardButton(text="Назад", callback_data="rus_back_android")

rus_in_android.add(rus_in_google_play, rus_in_cars_two)
rus_in_android.add(rus_in_mosaic)
rus_in_android.add(rus_back_android)


# Клавиатура номер 5 (pc)
rus_in_pc = InlineKeyboardMarkup(row_width=2)
rus_in_pc_calculator = InlineKeyboardButton(text="Калькулятор C#", callback_data="rus_in_pc_calculator")
rus_in_mod_bl = InlineKeyboardButton(text="МОД БЛ 🧚‍♂️", callback_data="rus_in_mod_bl")
rus_back_pc = InlineKeyboardButton(text="Назад", callback_data="rus_back_pc")

rus_in_pc.add(rus_in_mod_bl, rus_in_pc_calculator)
rus_in_pc.add(rus_back_pc)


# Клавиатура номер 6 (web_games)
rus_in_web_games = InlineKeyboardMarkup(row_width=2)
rus_in_pc_web_games = InlineKeyboardButton(text="ПК 🖥️", callback_data="rus_in_pc_web_games")
rus_in_phone_web_games = InlineKeyboardButton(text="ТЕЛЕФОН 📱", callback_data="rus_in_phone_web_games")
rus_back_in_web_games= InlineKeyboardButton(text="Назад", callback_data="rus_back_in_web_games")

rus_in_web_games.add(rus_in_pc_web_games, rus_in_phone_web_games)
rus_in_web_games.add(rus_back_in_web_games)


# Клавиатура номер 7 (pc_web_games)
rus_in_pc_web_games = InlineKeyboardMarkup(row_width=2)
rus_back_in_pc_web_games = InlineKeyboardButton(text="Назад", callback_data="rus_back_in_pc_web_games")

rus_in_pc_web_games.add(rus_back_in_pc_web_games)


# Клавиатура номер 8 (phone_web_games)
rus_in_phone_web_games = InlineKeyboardMarkup(row_width=2)
rus_back_in_phone_web_games = InlineKeyboardButton(text="Назад", callback_data="rus_back_in_phone_web_games")

rus_in_phone_web_games.add(rus_back_in_phone_web_games)


# Клавиатура номер 9 (google_play)
rus_in_google_play = InlineKeyboardMarkup(row_width=2)
rus_back_in_google_play = InlineKeyboardButton(text="Back", callback_data="rus_back_in_google_play")

rus_in_google_play.add(rus_back_in_google_play)


# Клавиатура номер 10 (социальные сети)
rus_in_social_network = InlineKeyboardMarkup(row_width=2)
rus_in_youtube_one = InlineKeyboardButton(text="YOUTUBE 1 📺", url="https://www.youtube.com/channel/UC9EJAIYe4sL0iGB_huHTqHw", callback_data="rus_in_youtube_one")
rus_in_youtube_two = InlineKeyboardButton(text="YOUTUBE 2 📺", url="https://www.youtube.com/channel/UCb2GlPOgqB_VpWTvQM_dzKg", callback_data="rus_in_youtube_two")
rus_in_twitch = InlineKeyboardButton(text="TWITCH 🔴", url="https://www.twitch.tv/komorifn", callback_data="rus_in_twitch")
rus_in_discord = InlineKeyboardButton(text="DISCORD 🗣️", url="https://discord.gg/2pbCpNcDZm", callback_data="rus_in_discord")
rus_in_github = InlineKeyboardButton(text="GITHUB 💣", url="https://github.com/Komorif", callback_data="rus_in_github")
rus_in_vk = InlineKeyboardButton(text="VK ✔️", url="https://vk.com/komorilfg", callback_data="rus_in_vk")
rus_back_social = InlineKeyboardButton(text="Назад", callback_data="rus_back_social")

rus_in_social_network.add(rus_in_youtube_one, rus_in_youtube_two).add(rus_in_twitch, rus_in_discord)
rus_in_social_network.add(rus_in_github, rus_in_vk)
rus_in_social_network.add(rus_back_social)


# Клавиатура номер 11 (FAQ)
rus_in_FAQ = InlineKeyboardMarkup(row_width=2)
rus_back_faq = InlineKeyboardButton(text="Назад", callback_data="rus_back_faq")

rus_in_FAQ.add(rus_back_faq)


# Клавиатура номер 12 (Профиль)
rus_in_Profile = InlineKeyboardMarkup(row_width=2)
rus_back_prof = InlineKeyboardButton(text="Назад", callback_data="rus_back_prof")

rus_in_Profile.add(rus_back_prof)


# Клавиатура номер 13 (Пожертвования)
rus_in_donation = InlineKeyboardMarkup(row_width=2)
rus_in_donation_in = InlineKeyboardButton(text="Пожертвование 💰", url="https://www.donationalerts.com/r/fetchy74", callback_data="rus_in_donation_in")
rus_back_donat = InlineKeyboardButton(text="Назад", callback_data="rus_back_donat")

rus_in_donation.add(rus_in_donation_in)
rus_in_donation.add(rus_back_donat)


# Клавиатура номер 14 (Отзывы)
rus_in_reviews = InlineKeyboardMarkup(row_width=2)
rus_back_in_reviews = InlineKeyboardButton(text="Назад", callback_data="rus_back_in_reviews")

rus_in_reviews.add(rus_back_in_reviews)



# PC
# Клавиатура номер 1.1 (Мод БЛ)
rus_in_mod_bl = InlineKeyboardMarkup(row_width=2)
rus_in_mod_bl_button_download = InlineKeyboardButton(text="Скачать мод для игры БЛ 🧚‍♂️", url="https://disk.yandex.ru/d/XmU8R4pGdsiuIA", callback_data="rus_in_mod_bl_button_download")
rus_back_mod = InlineKeyboardButton(text="Назад", callback_data="rus_back_mod")

rus_in_mod_bl.add(rus_in_mod_bl_button_download)
rus_in_mod_bl.add(rus_back_mod)


# Клавиатура 1.2 (Карточка Калькулятор)
rus_in_pc_calculator = InlineKeyboardMarkup(row_width=2)
rus_in_pc_calculator_button_download = InlineKeyboardButton(text="Скачать", url="https://disk.yandex.ru/d/rDZ7E98l2uj8YA", callback_data="rus_in_pc_calculator_button_download")
rus_back_in_pc_calculator = InlineKeyboardButton(text="Назад", callback_data="rus_back_in_pc_calculator")

rus_in_pc_calculator.add(rus_in_pc_calculator_button_download)
rus_in_pc_calculator.add(rus_back_in_pc_calculator)



# Android
# Клавиатура номер 1.1 (Машины)
rus_in_cars_two = InlineKeyboardMarkup(row_width=2)
rus_in_android_cars_two_button_download = InlineKeyboardButton(text="Скачать", url="https://disk.yandex.ru/d/rDZ7E98l2uj8YA", callback_data="rus_in_android_cars_two_button_download")
rus_back_in_cars_two = InlineKeyboardButton(text="Назад", callback_data="rus_back_in_cars_two")

rus_in_cars_two.add(rus_in_android_cars_two_button_download)
rus_in_cars_two.add(rus_back_in_cars_two)


# Клавиатура номер 1.2 (Мозаика)
rus_in_mosaic = InlineKeyboardMarkup(row_width=2)
rus_in_android_mosaic_button_download = InlineKeyboardButton(text="Скачать", url="https://disk.yandex.ru/d/G2b7dN2O8vFd7g", callback_data="rus_in_android_mosaic_button_download")
rus_back_in_mosaic = InlineKeyboardButton(text="Назад", callback_data="rus_back_in_mosaic")

rus_in_mosaic.add(rus_in_android_mosaic_button_download)
rus_in_mosaic.add(rus_back_in_mosaic)