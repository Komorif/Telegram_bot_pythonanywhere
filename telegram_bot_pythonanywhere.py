from aiogram.utils import executor

import logging
from aiogram import Bot, Dispatcher, types, executor


from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, callback_query

# Объекты для команд бота
from aiogram.types import BotCommand, BotCommandScopeChat


TOKEN = "your token"
logging.basicConfig(level=logging.INFO)


# прокси
proxy_url = "http://proxy.server:3128"


bot = Bot(token=TOKEN, proxy=proxy_url)
dp = Dispatcher(bot)


# Функция (запуск бота)
async def on_startup(dp):
	await bot.send_message(your id, "Я запустился")

# Функция (выключение бота)
async def on_shutdown(dp):
	await bot.send_message(your id, "Я завершил работу")


# Клавиатура номер 1 (выбором языка)
mainMenu_en_rus = InlineKeyboardMarkup(row_width=2)
lang_rus = InlineKeyboardButton(text="Russian 🇷🇺", callback_data="lang_rus")
lang_en = InlineKeyboardButton(text="English 🇺🇸", callback_data="lang_en")

# Добавляем кнопки для клавиатуры c выбором языка
mainMenu_en_rus.add(lang_en).add(lang_rus)


# Клавиатура номер 1.2 (выбором языка)
mainMenu_en_rus_two = InlineKeyboardMarkup(row_width=2)
lang_rus_two = InlineKeyboardButton(text="Russian 🇷🇺", callback_data="lang_rus_two")
lang_en_two = InlineKeyboardButton(text="English 🇺🇸", callback_data="lang_en_two")

# Добавляем кнопки для клавиатуры c выбором языка
mainMenu_en_rus_two.add(lang_en_two)
mainMenu_en_rus_two.add(lang_rus_two)



# English
# Клавиатура номер 1 (English_main_menu)
en_mainMenu = InlineKeyboardMarkup(row_width=2)
en_in_our_games = InlineKeyboardButton(text="Our games 🎮", callback_data="en_in_our_games")
en_in_social_network = InlineKeyboardButton(text="Social Media 🌍", callback_data="en_in_social_network")
en_in_FAQ = InlineKeyboardButton(text="FAQ❓", callback_data="en_in_FAQ")
en_in_Profile = InlineKeyboardButton(text="Profile 🧒", callback_data="en_in_Profile")
en_in_donation = InlineKeyboardButton(text="Support 💰", callback_data="en_in_donation")
en_back_mainMenu = InlineKeyboardButton(text="Back", callback_data="en_back_mainMenu")

# Добавляем кнопки для клавиатуры номер 1 (English)
en_mainMenu.add(en_in_our_games, en_in_social_network).add(en_in_FAQ, en_in_Profile)
en_mainMenu.add(en_in_donation)
en_mainMenu.add(en_back_mainMenu)


# Клавиатура номер 2 (Наши игры)
en_in_our_games = InlineKeyboardMarkup(row_width=2)
en_in_ios = InlineKeyboardButton(text="IOS 🍏", callback_data="en_in_ios")
en_in_android = InlineKeyboardButton(text="ANDROID 🤖", callback_data="en_in_android")
en_in_pc = InlineKeyboardButton(text="PC 🖥️", callback_data="en_in_pc")
en_in_web_games = InlineKeyboardButton(text="WEB GAMES 🎮", callback_data="en_in_web_games")
en_back_games = InlineKeyboardButton(text="Back", callback_data="en_back_games")

# Добавляем кнопки для клавиатуры номер 2 (Наши игры)
en_in_our_games.add(en_in_ios, en_in_android)
en_in_our_games.add(en_in_pc, en_in_web_games)
en_in_our_games.add(en_back_games)


# Клавиатура номер 3 (ios)
en_in_ios = InlineKeyboardMarkup(row_width=2)
en_back_ios = InlineKeyboardButton(text="Back", callback_data="en_back_ios")

# Добавляем кнопки для клавиатуры 3 (ios)
en_in_ios.add(en_back_ios)


# Клавиатура номер 4 (android)
en_in_android = InlineKeyboardMarkup(row_width=2)
en_in_google_play = InlineKeyboardButton(text="GOOGLE PLAY 👾", callback_data="en_in_google_play")
en_in_cars_two = InlineKeyboardButton(text="Cars 🚗", url="https://disk.yandex.ru/d/VEy132RmANfIMA", callback_data="en_in_cars_two")
en_in_mosaic = InlineKeyboardButton(text="Mosaic 🧠",url="https://disk.yandex.ru/d/G2b7dN2O8vFd7g", callback_data="en_in_mosaic")
en_back_android = InlineKeyboardButton(text="Back", callback_data="en_back_android")

# Добавляем кнопки для клавиатуры номер 4 (android)
en_in_android.add(en_in_google_play, en_in_cars_two)
en_in_android.add(en_in_mosaic)
en_in_android.add(en_back_android)


# Клавиатура номер 5 (pc)
en_in_pc = InlineKeyboardMarkup(row_width=2)
en_in_mod_bl = InlineKeyboardButton(text="ES MOD 🧚‍♂️", callback_data="en_in_mod_bl")
en_in_horror = InlineKeyboardButton(text="Horror 🧟‍♂️", url="https://disk.yandex.ru/d/nzt0GC6gXpJ83w", callback_data="en_in_horror")
en_back_pc = InlineKeyboardButton(text="Back", callback_data="en_back_pc")

# Добавляем кнопки для клавиатуры номер 5 (pc)
en_in_pc.add(en_in_mod_bl, en_in_horror)
en_in_pc.add(en_back_pc)


# Клавиатура номер 6 (web_games)
en_in_web_games = InlineKeyboardMarkup(row_width=2)
en_in_pc_web_games = InlineKeyboardButton(text="PC 🖥️", callback_data="en_in_pc_web_games")
en_in_phone_web_games = InlineKeyboardButton(text="PHONE 📱", callback_data="en_in_phone_web_games")
en_back_in_web_games= InlineKeyboardButton(text="Back", callback_data="en_back_in_web_games")

# Добавляем кнопки для клавиатуры номер 6 (web_games)
en_in_web_games.add(en_in_pc_web_games, en_in_phone_web_games)
en_in_web_games.add(en_back_in_web_games)


# Клавиатура номер 7 (pc_web_games)
en_in_pc_web_games = InlineKeyboardMarkup(row_width=2)
en_back_in_pc_web_games = InlineKeyboardButton(text="Back", callback_data="en_back_in_pc_web_games")

# Добавляем кнопки для клавиатуры номер 7 (pc_web_games)
en_in_pc_web_games.add(en_back_in_pc_web_games)


# Клавиатура номер 8 (phone_web_games)
en_in_phone_web_games = InlineKeyboardMarkup(row_width=2)
en_back_in_phone_web_games = InlineKeyboardButton(text="Back", callback_data="en_back_in_phone_web_games")

# Добавляем кнопки для клавиатуры номер 8 (phone_web_games)
en_in_phone_web_games.add(en_back_in_phone_web_games)


# Клавиатура номер 9 (google_play)
en_in_google_play = InlineKeyboardMarkup(row_width=2)
en_back_in_google_play = InlineKeyboardButton(text="Back", callback_data="en_back_in_google_play")

# Добавляем кнопки для клавиатуры номер 9 (google_play)
en_in_google_play.add(en_back_in_google_play)


# Клавиатура номер 10 (Мод БЛ)
en_in_mod_bl = InlineKeyboardMarkup(row_width=2)
en_in_mod_bl_downl = InlineKeyboardButton(text="Download our mod for the game ES 🧚‍♂️", url="https://disk.yandex.ru/d/XmU8R4pGdsiuIA", callback_data="en_in_mod_bl_downl")
en_back_mod = InlineKeyboardButton(text="Back", callback_data="en_back_mod")

# Добавляем кнопки для клавиатуры номер 10 (Мод БЛ)
en_in_mod_bl.add(en_in_mod_bl_downl)
en_in_mod_bl.add(en_back_mod)


# Клавиатура номер 11 (социальные сети)
en_in_social_network = InlineKeyboardMarkup(row_width=2)
en_in_youtube_one = InlineKeyboardButton(text="YOUTUBE 1 📺", url="https://www.youtube.com/channel/UC9EJAIYe4sL0iGB_huHTqHw", callback_data="en_in_youtube_one")
en_in_youtube_two = InlineKeyboardButton(text="YOUTUBE 2 📺", url="https://www.youtube.com/channel/UCb2GlPOgqB_VpWTvQM_dzKg", callback_data="en_in_youtube_two")
en_in_twitch = InlineKeyboardButton(text="TWITCH 🔴", url="https://www.twitch.tv/komorifn", callback_data="en_in_twitch")
en_in_discord = InlineKeyboardButton(text="DISCORD 🗣️", url="https://discord.gg/2pbCpNcDZm", callback_data="en_in_discord")
en_in_github = InlineKeyboardButton(text="GITHUB 💣", url="https://github.com/Komorif", callback_data="en_in_github")
en_in_vk = InlineKeyboardButton(text="VK ✔️", url="https://vk.com/komorilfg", callback_data="en_in_vk")
en_back_social = InlineKeyboardButton(text="Back", callback_data="en_back_social")

# Добавляем кнопки для клавиатуры номер 11 (социальные сети)
en_in_social_network.add(en_in_youtube_one, en_in_youtube_two).add(en_in_twitch, en_in_discord)
en_in_social_network.add(en_in_github, en_in_vk)
en_in_social_network.add(en_back_social)


# Клавиатура номер 12 (FAQ)
en_in_FAQ = InlineKeyboardMarkup(row_width=2)
en_in_FAQ_ds = InlineKeyboardButton(text="Here ⬆", url = "https://1drv.ms/w/s!AtF4vCOqewgBoCr1uMzSn-xf_3fV?e=rmxrjf", callback_data="en_in_FAQ_ds")
en_back_faq = InlineKeyboardButton(text="Back", callback_data="en_back_faq")

# Добавляем кнопки для клавиатуры номер 12 (FAQ)
en_in_FAQ.add(en_in_FAQ_ds)
en_in_FAQ.add(en_back_faq)


# Клавиатура номер 13 (Профиль)
en_in_Profile = InlineKeyboardMarkup(row_width=2)
en_back_prof = InlineKeyboardButton(text="Back", callback_data="en_back_prof")

# Добавляем кнопки для клавиатуры номер 13 (Профиль)
en_in_Profile.add(en_back_prof)


# Клавиатура номер 14 (Пожертвования)
en_in_donation = InlineKeyboardMarkup(row_width=2)
en_in_donation_in = InlineKeyboardButton(text="Donation 💰", url="https://www.donationalerts.com/r/fetchy74", callback_data="en_in_donation_in")
en_back_donat = InlineKeyboardButton(text="Back", callback_data="en_back_donat")

# Добавляем кнопки для клавиатуры 14 (Пожертвования)
en_in_donation.add(en_in_donation_in)
en_in_donation.add(en_back_donat)



# Russian
# Клавиатура номер 1 (Russian_main_menu)
rus_mainMenu = InlineKeyboardMarkup(row_width=2)
rus_in_our_games = InlineKeyboardButton(text="Наши игры 🎮", callback_data="rus_in_our_games")
rus_in_social_network = InlineKeyboardButton(text="Социалки 🌍", callback_data="rus_in_social_network")
rus_in_FAQ = InlineKeyboardButton(text="FAQ❓", callback_data="rus_in_FAQ")
rus_in_Profile = InlineKeyboardButton(text="Профиль 🧒", callback_data="rus_in_Profile")
rus_in_donation = InlineKeyboardButton(text="Поддержка 💰", callback_data="rus_in_donation")
rus_back_mainMenu = InlineKeyboardButton(text="Назад",  callback_data="rus_back_mainMenu")

# Добавляем кнопки для клавиатуры номер 1 (Russian_main_menu)
rus_mainMenu.add(rus_in_our_games, rus_in_social_network).add(rus_in_FAQ, rus_in_Profile)
rus_mainMenu.add(rus_in_donation)
rus_mainMenu.add(rus_back_mainMenu)


# Клавиатура номер 2 (Наши игры)
rus_in_our_games = InlineKeyboardMarkup(row_width=2)
rus_in_ios = InlineKeyboardButton(text="IOS 🍏", callback_data="rus_in_ios")
rus_in_android = InlineKeyboardButton(text="ANDROID 🤖", callback_data="rus_in_android")
rus_in_pc = InlineKeyboardButton(text="PC 🖥️", callback_data="rus_in_pc")
rus_in_web_games = InlineKeyboardButton(text="WEB GAMES 🎮", callback_data="rus_in_web_games")
rus_back_games = InlineKeyboardButton(text="Назад", callback_data="rus_back_games")


# Добавляем кнопки для клавиатуры номер 2 (Наши игры)
rus_in_our_games.add(rus_in_ios, rus_in_android)
rus_in_our_games.add(rus_in_pc, rus_in_web_games)
rus_in_our_games.add(rus_back_games)


# Клавиатура номер 3 (ios)
rus_in_ios = InlineKeyboardMarkup(row_width=2)
rus_back_ios = InlineKeyboardButton(text="Назад", callback_data="rus_back_ios")

# Добавляем кнопки для клавиатуры 3 (ios)
rus_in_ios.add(rus_back_ios)


# Клавиатура номер 4 (android)
rus_in_android = InlineKeyboardMarkup(row_width=2)
rus_in_google_play = InlineKeyboardButton(text="GOOGLE PLAY 👾", callback_data="rus_in_google_play")
rus_in_cars_two = InlineKeyboardButton(text="Cars 🚗", url="https://disk.yandex.ru/d/VEy132RmANfIMA", callback_data="rus_in_cars_two")
rus_in_mosaic = InlineKeyboardButton(text="Mosaic 🧠",url="https://disk.yandex.ru/d/G2b7dN2O8vFd7g", callback_data="rus_in_mosaic")
rus_back_android = InlineKeyboardButton(text="Назад", callback_data="rus_back_android")

# Добавляем кнопки для клавиатуры номер 4 (android)
rus_in_android.add(rus_in_google_play, rus_in_cars_two)
rus_in_android.add(rus_in_mosaic)
rus_in_android.add(rus_back_android)


# Клавиатура номер 5 (pc)
rus_in_pc = InlineKeyboardMarkup(row_width=2)
rus_in_mod_bl = InlineKeyboardButton(text="МОД БЛ 🧚‍♂️", callback_data="rus_in_mod_bl")
rus_in_horror = InlineKeyboardButton(text="Horror 🧟‍♂️", url="https://disk.yandex.ru/d/nzt0GC6gXpJ83w", callback_data="rus_in_horror")
rus_back_pc = InlineKeyboardButton(text="Назад", callback_data="rus_back_pc")

# Добавляем кнопки для клавиатуры номер 5 (pc)
rus_in_pc.add(rus_in_mod_bl, rus_in_horror)
rus_in_pc.add(rus_back_pc)


# Клавиатура номер 6 (web_games)
rus_in_web_games = InlineKeyboardMarkup(row_width=2)
rus_in_pc_web_games = InlineKeyboardButton(text="ПК 🖥️", callback_data="rus_in_pc_web_games")
rus_in_phone_web_games = InlineKeyboardButton(text="ТЕЛЕФОН 📱", callback_data="rus_in_phone_web_games")
rus_back_in_web_games= InlineKeyboardButton(text="Назад", callback_data="rus_back_in_web_games")

# Добавляем кнопки для клавиатуры номер 6 (web_games)
rus_in_web_games.add(rus_in_pc_web_games, rus_in_phone_web_games)
rus_in_web_games.add(rus_back_in_web_games)


# Клавиатура номер 7 (pc_web_games)
rus_in_pc_web_games = InlineKeyboardMarkup(row_width=2)
rus_back_in_pc_web_games = InlineKeyboardButton(text="Назад", callback_data="rus_back_in_pc_web_games")

# Добавляем кнопки для клавиатуры номер 7 (pc_web_games)
rus_in_pc_web_games.add(rus_back_in_pc_web_games)


# Клавиатура номер 8 (phone_web_games)
rus_in_phone_web_games = InlineKeyboardMarkup(row_width=2)
rus_back_in_phone_web_games = InlineKeyboardButton(text="Назад", callback_data="rus_back_in_phone_web_games")

# Добавляем кнопки для клавиатуры номер 8 (phone_web_games)
rus_in_phone_web_games.add(rus_back_in_phone_web_games)


# Клавиатура номер 9 (google_play)
rus_in_google_play = InlineKeyboardMarkup(row_width=2)
rus_back_in_google_play = InlineKeyboardButton(text="Back", callback_data="rus_back_in_google_play")

# Добавляем кнопки для клавиатуры номер 9 (google_play)
rus_in_google_play.add(rus_back_in_google_play)


# Клавиатура номер 10 (Мод БЛ)
rus_in_mod_bl = InlineKeyboardMarkup(row_width=2)
rus_in_mod_bl_downl = InlineKeyboardButton(text="Скачать наш мод для игры БЛ 🧚‍♂️", url="https://disk.yandex.ru/d/XmU8R4pGdsiuIA", callback_data="rus_in_mod_bl_downl")
rus_back_mod = InlineKeyboardButton(text="Назад", callback_data="rus_back_mod")

# Добавляем кнопки для клавиатуры номер 10 (Мод БЛ)
rus_in_mod_bl.add(rus_in_mod_bl_downl)
rus_in_mod_bl.add(rus_back_mod)


# Клавиатура номер 11 (социальные сети)
rus_in_social_network = InlineKeyboardMarkup(row_width=2)
rus_in_youtube_one = InlineKeyboardButton(text="YOUTUBE 1 📺", url="https://www.youtube.com/channel/UC9EJAIYe4sL0iGB_huHTqHw", callback_data="rus_in_youtube_one")
rus_in_youtube_two = InlineKeyboardButton(text="YOUTUBE 2 📺", url="https://www.youtube.com/channel/UCb2GlPOgqB_VpWTvQM_dzKg", callback_data="rus_in_youtube_two")
rus_in_twitch = InlineKeyboardButton(text="TWITCH 🔴", url="https://www.twitch.tv/komorifn", callback_data="rus_in_twitch")
rus_in_discord = InlineKeyboardButton(text="DISCORD 🗣️", url="https://discord.gg/2pbCpNcDZm", callback_data="rus_in_discord")
rus_in_github = InlineKeyboardButton(text="GITHUB 💣", url="https://github.com/Komorif", callback_data="rus_in_github")
rus_in_vk = InlineKeyboardButton(text="VK ✔️", url="https://vk.com/komorilfg", callback_data="rus_in_vk")
rus_back_social = InlineKeyboardButton(text="Назад", callback_data="rus_back_social")

# Добавляем кнопки для клавиатуры номер 11 (социальные сети)
rus_in_social_network.add(rus_in_youtube_one, rus_in_youtube_two).add(rus_in_twitch, rus_in_discord)
rus_in_social_network.add(rus_in_github, rus_in_vk)
rus_in_social_network.add(rus_back_social)


# Клавиатура номер 12 (FAQ)
rus_in_FAQ = InlineKeyboardMarkup(row_width=2)
rus_in_FAQ_ds = InlineKeyboardButton(text="Тут ⬆", url = "https://1drv.ms/w/s!AtF4vCOqewgBoB1t_x6DdrpMX1QH?e=wrR0sq", callback_data="rus_in_FAQ_ds")
rus_back_faq = InlineKeyboardButton(text="Назад", callback_data="rus_back_faq")

# Добавляем кнопки для клавиатуры номер 12 (FAQ)
rus_in_FAQ.add(rus_in_FAQ_ds)
rus_in_FAQ.add(rus_back_faq)


# Клавиатура номер 13 (Профиль)
rus_in_Profile = InlineKeyboardMarkup(row_width=2)
rus_back_prof = InlineKeyboardButton(text="Назад", callback_data="rus_back_prof")

# Добавляем кнопки для клавиатуры номер 13 (Профиль)
rus_in_Profile.add(rus_back_prof)


# Клавиатура номер 14 (Пожертвования)
rus_in_donation = InlineKeyboardMarkup(row_width=2)
rus_in_donation_in = InlineKeyboardButton(text="Пожертвование 💰", url="https://www.donationalerts.com/r/fetchy74", callback_data="rus_in_donation_in")
rus_back_donat = InlineKeyboardButton(text="Назад", callback_data="rus_back_donat")

# Добавляем кнопки для клавиатуры 14 (Пожертвования)
rus_in_donation.add(rus_in_donation_in)
rus_in_donation.add(rus_back_donat)



# Картинки для менюшек
menu_one="https://downloader.disk.yandex.ru/preview/711bb1adff875b15eb27bc2e953f8d0b36a69eecb3a2ca4648143ee0aa223585/63c1af3e/_6tncDV3aVZTsQg0TZbCornwjRjeQl6Sbl7ryrTKPw9pPdoQLXcQ1r0Yu5Untrt8SGGTmFGHYgs8E_rm6dSkYA%3D%3D?uid=0&filename=menu_one.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
ios="https://downloader.disk.yandex.ru/preview/5b42c746b53921a74847b49334ef13e01f2864a5e758af36484f783248b9f5f8/63c1af84/1iEydv63EpJWU_e7x7LDfqX3ATg9TGRKmTLY0YJUpIRbS974E5ceNrIrAqGV3o-TvDf9AYWnpGhBpJ15kq8vPw%3D%3D?uid=0&filename=ios.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
andoid="https://downloader.disk.yandex.ru/preview/5f590d1bcdda15d56e668bba0c430c5714439e97a3e188401357306c4b101eb2/63c1afb3/lsX9zrLWoYPzhyZU41o5w6X3ATg9TGRKmTLY0YJUpITesx_k25DxwZNvFQTOTgbNV1IjEwIpXQ4ssHZ9Bk8ywg%3D%3D?uid=0&filename=android.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
pc="https://downloader.disk.yandex.ru/preview/c2f1fbb4c7d3c2a355d7d61785ab22188ea5f22530e92a1f322a740a6501e478/63c1afe4/MNQlWgSL62OIKo3AGtl_v6X3ATg9TGRKmTLY0YJUpIQD6nmvIEl_RH7MzyL3Flp8Iowu8MDThx2y9aZ5ZE9loQ%3D%3D?uid=0&filename=pc.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
google_play="https://downloader.disk.yandex.ru/preview/96cff67912e20350583aa5e39a9bc6a0994ec30ef871a46c4a8444dde4134963/63d53985/lw9UVvCoowbEvBhKKB6sLYaa__hDX-jp_fjofm25VinHzXea_bSmCdK1PkFvjK4JS2ihJDr4UrHs0TjYNz4i8w%3D%3D?uid=0&filename=google_play.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
faq="https://downloader.disk.yandex.ru/preview/87f33def26b09db3e18c3dd2f3137cd3a43a08c83c2f6a02301fbd6035c6615a/63c1b002/cVQro105INirqiPWEro9H6X3ATg9TGRKmTLY0YJUpISHHAmrL6lUr33tyAmW2_qwI3ZwRG3eV-ovVOZmbOYMhg%3D%3D?uid=0&filename=FAQ.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"

# Картинки для менюшек English
en_menu="https://downloader.disk.yandex.ru/preview/a41d6e5b6e080dca6a0b27e0a2e10a3b93ebc5249c3a3e1a8b96f65ddee0c5f2/63d43877/8tUqByIlKdFjR7xnNbgYj0aXDJB59eX7utlYUyhGcf13gQHfmnklgyCQDu03CMNZ4VgzQDxwqs7YESJ7RPvBRA%3D%3D?uid=0&filename=mainmenu.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
en_social_network="https://downloader.disk.yandex.ru/preview/9e70fb7803245d98c211e0da3466d026bc57bd9a65ecd1a168ff36f3b8d0310c/63c1b070/nA_Tzw5hTAom4eLxCwtmX6X3ATg9TGRKmTLY0YJUpISRDKBSZerOmTeBwgs_AoTsQ8IeF_4aLiIgLFstdOiqBA%3D%3D?uid=0&filename=en_social_network.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
en_donation="https://downloader.disk.yandex.ru/preview/47d815b9afdaeb8a78227244ae18100ec9ab26db7f47a2ea7ef7227f537f960a/63c1b091/iHeFI6ozuVm4jxnyqkivl6X3ATg9TGRKmTLY0YJUpIRp9GktWZbSD8CYW5bOoozojw2HsB_q8F2vChjF_ASPvA%3D%3D?uid=0&filename=en_donation.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
en_mod_bl="https://downloader.disk.yandex.ru/preview/d77ef2bdff300f67bc3dfa76d428e50a2831c23fb027f785f3cc82c217bb504b/63c1b081/6CJXf9gXYkwgKeJuReORQbnwjRjeQl6Sbl7ryrTKPw94tzTUKvV07Tzv4_HOBQpduUo-Uz7qHopuycX_qB2HAA%3D%3D?uid=0&filename=en_mod_bl.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
en_platform="https://downloader.disk.yandex.ru/preview/0856ad63f6b1604d107cf01f435a3acb2870138debf1a821202ec6296d1102d2/63c1b0b0/KniNQVNcyYLVfZFvpQk_VrnwjRjeQl6Sbl7ryrTKPw9aIHZN5gDMTD2IB6NuXpiPBDcKAuknVXsIhEAr2IoqVg%3D%3D?uid=0&filename=en_platform.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
en_phone="https://downloader.disk.yandex.ru/preview/ab4d78a35c261ef702b4f7cc4b5831d77d86907a1d53d878232de22c9bcdf556/63d42a9a/sMY82TkfDdbpLU_KYp5ABHq9fksKA_u6Qdlxi1mzlvkYnKyNv5mu8n5nFdECD8WnvEzBXTA5xk_aVhWX8A57Vw%3D%3D?uid=0&filename=phone.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
en_profile="https://downloader.disk.yandex.ru/preview/dce9ab49782fe5182a7772c6a3cc164b74c6b38cdfce13ae96691cb6c7fdc634/63c1b0a1/s0oqgq8sySb2pAGHKhdAv6X3ATg9TGRKmTLY0YJUpISzy3nZJGCDYSf3glLT8pfLn_NK5CQ3-BGJ0RYRMMG39Q%3D%3D?uid=0&filename=en_profile.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"

# Картинки для менюшек Russian
rus_menu="https://downloader.disk.yandex.ru/preview/170dd84ecdd0e02a097dcb64a021a97c445181048d4d1b22cccd10867a8e5041/63c1b46a/BEY3ThlvSC5pLmNSlclnc9-rcZs5RLWR3E1vERxC9CgFY7Czim8bvmNQ7ppNK1A8NTJ1cnQ4t8Wfgd1UHtE3Pw%3D%3D?uid=0&filename=rus_menu.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
rus_social_network="https://downloader.disk.yandex.ru/preview/5e6eaa54cbd5d273ed746392430ee67368b115b52be709a92067dc7a6881bd80/63c1b04c/0MK89FED-4X2FcfnPeA9y6X3ATg9TGRKmTLY0YJUpITIE_sADpIQGmAA6lNp-D4kDRRADv9EHBTb8y2v7B6Tzw%3D%3D?uid=0&filename=rus_social_network.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
rus_donation="https://downloader.disk.yandex.ru/preview/d27eae5cda0522b720a1374cb15fe70b00866d5002ee80c256100c31b6428754/63c1b024/lCvTYZkOtl_KiCVwROLU4aX3ATg9TGRKmTLY0YJUpIRAZFVTQVGzo0u5ul1B10bh_B9lSwVv1bqwwGwSeWABmw%3D%3D?uid=0&filename=rus_donation.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
rus_mod_bl="https://downloader.disk.yandex.ru/preview/713634f417141a913e250c473364de52fefaf4c71ba50673bb99ea591e76b39b/63c1b013/ekNSf85xrnEWXBFg-lT1z7nwjRjeQl6Sbl7ryrTKPw_oUKVUk4sd2kC9uuhEYadBpyH1tpWLS4Q0Sv775Jf7Aw%3D%3D?uid=0&filename=rus_mod_bl.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
rus_platform="https://downloader.disk.yandex.ru/preview/06105be0af89d22c9670a08316b4b46e0f481bfe92d4a832d74fc8b9ad89c1a8/63c1b03b/jkk3Y7EBMq8COZs_yYwMI7nwjRjeQl6Sbl7ryrTKPw8rEB7s5cCmyZFg6ntzpGbUWhwhDkefJe83IztboXiOVA%3D%3D?uid=0&filename=rus_platform.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
rus_phone="https://downloader.disk.yandex.ru/preview/51d2f367a1a41aa520cfc049eaec03d0d4c4212156a41f1daf28efa75fec1507/63d42ae4/IasrU8Hu2XzBVjdC6D6qZFBavCHoxKachbVWEqGMJmwxvAxbP3osMcrGPezZc3VuXhMOHAM2IACzYjAhChesVw%3D%3D?uid=0&filename=%D1%82%D0%B5%D0%BB%D0%B5%D1%84%D0%BE%D0%BD.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"
rus_profile="https://downloader.disk.yandex.ru/preview/6811da4964699788c99ae5bb69b41048387bc2d9c1f9e7cb8c5349d9404ec053/63c1b05b/YgAWFr1vJHk_O_uT15w--aX3ATg9TGRKmTLY0YJUpIRVDHxEdaip2EyFseskn7OsIQ737D4UmDZHbGTolY1g3A%3D%3D?uid=0&filename=rus_profile.jpg&disposition=inline&hash=&limit=0&content_type=image%2Fjpeg&owner_uid=0&tknv=v2&size=2048x2048"


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
        await message.answer("Если отправить что-то из этого списка\n1. Смайлик\n2. Эмоджи\n3. Gif\n4. Видео\n4. Фото\n5. Голосовое сообщение\n\nБот отправит вам его в ответ")

    elif message.from_user.language_code == "en":
        await message.answer("If you send something from this list\n1. Smiley face\n2. Emoji\n3. Gif\n4. Video\n4. Picture\n5. Voice message\n\nBot will send it back to you")



# /games
@dp.message_handler(commands="games")
async def command_games(message: types.Message):
    if message.from_user.language_code == "ru":
        await message.answer("ANDROID\n1. Cars\n2. Mosaic\n\nPC\n1. Horror\n2. ES MOD\n\nWEB GAMES\nПока нет")

    elif message.from_user.language_code == "en":
        await message.answer("ANDROID\n1. Cars\n2. Mosaic\n\nPC\n1. Horror\n2. ES MOD\n\nWEB GAMES\nNot yet")



# 1.2 меню выбор языка
@dp.callback_query_handler(text_contains="start")
async def mainMenu_en_rus_two(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)

    if call.data == "mainMenu_en_rus_two":
        await bot.send_message(call.from_user.id, caption="🇺🇸 / 🇷🇺", reply_markup=mainMenu_en_rus)


# Итерация с кнопок English и Russian на их менюшки
@dp.callback_query_handler(text_contains="lang_")
async def lang_all(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)

    if call.data == "lang_en":
        await bot.send_photo(call.from_user.id, photo=en_menu, caption="MAIN MENU 🇺🇸", reply_markup=en_mainMenu)

    elif call.data == "lang_rus":
        await bot.send_photo(call.from_user.id, photo=rus_menu, caption="ГЛАВНОЕ МЕНЮ 🇷🇺", reply_markup=rus_mainMenu)


# Отдельный back с mainmenu на выбор языков en
@dp.callback_query_handler(text_contains="en_back_mainMenu")
async def lang_en_back(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)

    if call.data == "en_back_mainMenu":
        await bot.send_photo(call.from_user.id, photo=menu_one, caption="🇺🇸 / 🇷🇺", reply_markup=mainMenu_en_rus)


# Отдельный back с mainmenu на выбор языков rus
@dp.callback_query_handler(text_contains="rus_back_mainMenu")
async def lang_rus_back(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)

    if call.data == "rus_back_mainMenu":
        await bot.send_photo(call.from_user.id, photo=menu_one, caption="🇺🇸 / 🇷🇺", reply_markup=mainMenu_en_rus)


# Продвинутое эхо
@dp.message_handler(content_types=[
	types.ContentType.DOCUMENT, types.ContentType.PHOTO,
	types.ContentType.STICKER, types.ContentType.VIDEO,
	types.ContentType.TEXT,  types.ContentType.ANIMATION,
	types.ContentType.VOICE
])
async def download_doc(message: types.Message):
    # Если (документ) работает также с gif
	if 'document' in message:
		await message.answer_document(message.document.file_id)

		# Необязательная загрузка
		#await message.document.download()

	# Если (фото)
	elif 'photo' in message:
		await message.answer_photo(message.photo[-1].file_id)

		# Необязательная загрузка
		#await message.photo[-1].download()

	# Если (стикер)
	elif "sticker" in message:
		await message.answer_sticker(message.sticker.file_id)

		# Необязательная загрузка
		#await message.sticker.download()

	# Если (видео)
	elif "video" in message:
		await message.answer_video(message.video.file_id)

		# Необязательная загрузка
		#await message.video.download()

	# Если (какой - либо текст) работает также со смайликами
	elif "text" in message:
	    await message.answer(message.text)

	# Если (голосовое сообщение)
	elif "voice" in message:
	    await message.answer_voice(message.voice.file_id)

	    # Необязательная загрузка
	    #await message.voice.download()



# English
@dp.callback_query_handler(text_contains="en_back_")
async def back_buttons_en(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)

# Условия для всех назад кнопок English
    if call.data == "en_back_games":
        await bot.send_photo(call.from_user.id, photo=en_menu, caption="MAIN MENU 🇺🇸", reply_markup=en_mainMenu)
    elif call.data == "en_back_ios":
        await bot.send_photo(call.from_user.id, photo=en_platform, caption=r"SELECT A PLATFORM 🇺🇸", reply_markup=en_in_our_games)
    elif call.data == "en_back_android":
        await bot.send_photo(call.from_user.id, photo=en_platform, caption=r"SELECT A PLATFORM 🇺🇸", reply_markup=en_in_our_games)
    elif call.data == "en_back_pc":
        await bot.send_photo(call.from_user.id, photo=en_platform, caption=r"SELECT A PLATFORM 🇺🇸", reply_markup=en_in_our_games)
    elif call.data == "en_back_in_web_games":
        await bot.send_photo(call.from_user.id, photo=en_platform, caption=r"SELECT A PLATFORM 🇺🇸", reply_markup=en_in_our_games)
    elif call.data == "en_back_in_pc_web_games":
        await bot.send_photo(call.from_user.id, photo=en_platform, caption=r"SELECT A PLATFORM 🇺🇸", reply_markup=en_in_web_games)
    elif call.data == "en_back_in_phone_web_games":
        await bot.send_photo(call.from_user.id, photo=en_platform, caption=r"SELECT A PLATFORM 🇺🇸", reply_markup=en_in_web_games)
    elif call.data == "en_back_in_google_play":
        await bot.send_photo(call.from_user.id, photo=andoid, caption="Choose any game you want to download 🇺🇸", reply_markup=en_in_android)
    elif call.data == "en_back_mod":
        await bot.send_photo(call.from_user.id, photo=en_platform, caption=r"SELECT A PLATFORM 🇺🇸", reply_markup=en_in_pc)
    elif call.data == "en_back_social":
        await bot.send_photo(call.from_user.id, photo=en_menu, caption="MAIN MENU 🇺🇸", reply_markup=en_mainMenu)
    elif call.data == "en_back_faq":
        await bot.send_photo(call.from_user.id, photo=en_menu, caption="MAIN MENU 🇺🇸", reply_markup=en_mainMenu)
    elif call.data == "en_back_prof":
        await bot.send_photo(call.from_user.id, photo=en_menu, caption="MAIN MENU 🇺🇸", reply_markup=en_mainMenu)
    elif call.data == "en_back_donat":
        await bot.send_photo(call.from_user.id, photo=en_menu, caption="MAIN MENU 🇺🇸", reply_markup=en_mainMenu)


# Все inline клавиатуры inline en_in_ перед каждой English
@dp.callback_query_handler(text_contains="en_in_")
async def it_buttons_en(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)

# Условия для всех inline клавиатур English
    if call.data == "en_in_our_games":
        await bot.send_photo(call.from_user.id, photo=en_platform, caption=r"SELECT A PLATFORM 🇺🇸", reply_markup=en_in_our_games)
    elif call.data == "en_in_ios":
        await bot.send_photo(call.from_user.id, photo=ios, caption="Choose any game you want to download 🇺🇸", reply_markup=en_in_ios)
    elif call.data == "en_in_android":
        await bot.send_photo(call.from_user.id, photo=andoid, caption="Choose any game you want to download 🇺🇸", reply_markup=en_in_android)
    elif call.data == "en_in_pc":
        await bot.send_photo(call.from_user.id, photo=pc, caption="Choose any game you want to download 🇺🇸", reply_markup=en_in_pc)
    elif call.data == "en_in_web_games":
        await bot.send_photo(call.from_user.id, photo=en_platform, caption=r"SELECT A PLATFORM 🇺🇸", reply_markup=en_in_web_games)
    elif call.data == "en_in_pc_web_games":
        await bot.send_photo(call.from_user.id, photo=pc, caption=r"Pick any game you want 🇺🇸", reply_markup=en_in_pc_web_games)
    elif call.data == "en_in_phone_web_games":
        await bot.send_photo(call.from_user.id, photo=en_phone, caption=r"Pick any game you want 🇺🇸", reply_markup=en_in_phone_web_games)
    elif call.data == "en_in_mod_bl":
        await bot.send_photo(call.from_user.id, photo=en_mod_bl, caption="MOD FOR ENDLESS SUMMER 🇺🇸", reply_markup=en_in_mod_bl)
    elif call.data == "en_in_google_play":
        await bot.send_photo(call.from_user.id, photo=google_play, caption="GOOGLE PLAY 🇺🇸", reply_markup=en_in_google_play)
    elif call.data == "en_in_social_network":
        await bot.send_photo(call.from_user.id, photo=en_social_network, caption="SOCIAL MEDIA 🇺🇸", reply_markup=en_in_social_network)
    elif call.data == "en_in_FAQ":
        await bot.send_photo(call.from_user.id, photo=faq, caption="We have answered frequently asked questions for your convenience 🇺🇸", reply_markup=en_in_FAQ)
    elif call.data == "en_in_Profile":
        await bot.send_photo(call.from_user.id, photo=en_profile, caption=f"Your profile ID: {call.from_user.id} \nYou are a human being. \nGood luck using the bot 🇺🇸", reply_markup=en_in_Profile)
    elif call.data == "en_in_donation":
        await bot.send_photo(call.from_user.id, photo=en_donation, caption="You can help us be better 🇺🇸", reply_markup=en_in_donation)



# Russian
@dp.callback_query_handler(text_contains="rus_back_")
async def back_buttons_rus(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)

# Условия для всех назад кнопок English
    if call.data == "rus_back_games":
        await bot.send_photo(call.from_user.id, photo=rus_menu, caption="ГЛАВНОЕ МЕНЮ 🇷🇺", reply_markup=rus_mainMenu)
    elif call.data == "rus_back_ios":
        await bot.send_photo(call.from_user.id, photo=rus_platform, caption="ВЫВЕРИТЕ ПЛАТФОРМУ 🇷🇺", reply_markup=rus_in_our_games)
    elif call.data == "rus_back_android":
        await bot.send_photo(call.from_user.id, photo=rus_platform, caption="ВЫВЕРИТЕ ПЛАТФОРМУ 🇷🇺", reply_markup=rus_in_our_games)
    elif call.data == "rus_back_pc":
        await bot.send_photo(call.from_user.id, photo=rus_platform, caption="ВЫВЕРИТЕ ПЛАТФОРМУ 🇷🇺", reply_markup=rus_in_our_games)
    elif call.data == "rus_back_in_web_games":
        await bot.send_photo(call.from_user.id, photo=rus_platform, caption="ВЫВЕРИТЕ ПЛАТФОРМУ 🇷🇺", reply_markup=rus_in_our_games)
    elif call.data == "rus_back_in_pc_web_games":
        await bot.send_photo(call.from_user.id, photo=rus_platform, caption="ВЫВЕРИТЕ ПЛАТФОРМУ 🇷🇺", reply_markup=rus_in_web_games)
    elif call.data == "rus_back_in_phone_web_games":
        await bot.send_photo(call.from_user.id, photo=rus_platform, caption="ВЫВЕРИТЕ ПЛАТФОРМУ 🇷🇺", reply_markup=rus_in_web_games)
    elif call.data == "rus_back_in_google_play":
        await bot.send_photo(call.from_user.id, photo=andoid, caption="Выбирай любую игру какую хочешь скачать 🇷🇺", reply_markup=rus_in_android)
    elif call.data == "rus_back_mod":
        await bot.send_photo(call.from_user.id, photo=rus_platform, caption="ВЫВЕРИТЕ ПЛАТФОРМУ 🇷🇺", reply_markup=rus_in_pc)
    elif call.data == "rus_back_social":
        await bot.send_photo(call.from_user.id, photo=rus_menu, caption="ГЛАВНОЕ МЕНЮ 🇷🇺", reply_markup=rus_mainMenu)
    elif call.data == "rus_back_faq":
        await bot.send_photo(call.from_user.id, photo=rus_menu, caption="ГЛАВНОЕ МЕНЮ 🇷🇺", reply_markup=rus_mainMenu)
    elif call.data == "rus_back_prof":
        await bot.send_photo(call.from_user.id, photo=rus_menu, caption="ГЛАВНОЕ МЕНЮ 🇷🇺", reply_markup=rus_mainMenu)
    elif call.data == "rus_back_donat":
        await bot.send_photo(call.from_user.id, photo=rus_menu, caption="ГЛАВНОЕ МЕНЮ 🇷🇺", reply_markup=rus_mainMenu)


# Все inline клавиатуры inline en_in_ перед каждой English
@dp.callback_query_handler(text_contains="rus_in_")
async def it_buttons_rus(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)

# Условия для всех inline клавиатур English
    if call.data == "rus_in_our_games":
        await bot.send_photo(call.from_user.id, photo=rus_platform, caption="ВЫБЕРИТЕ ПЛАТФОРМУ 🇷🇺", reply_markup=rus_in_our_games)
    elif call.data == "rus_in_ios":
        await bot.send_photo(call.from_user.id, photo=ios, caption="Выбирай любую игру какую хочешь скачать 🇷🇺", reply_markup=rus_in_ios)
    elif call.data == "rus_in_android":
        await bot.send_photo(call.from_user.id, photo=andoid, caption="Выбирай любую игру какую хочешь скачать 🇷🇺", reply_markup=rus_in_android)
    elif call.data == "rus_in_pc":
        await bot.send_photo(call.from_user.id, photo=pc, caption="Выбирай любую игру какую хочешь скачать 🇷🇺", reply_markup=rus_in_pc)
    elif call.data == "rus_in_web_games":
        await bot.send_photo(call.from_user.id, photo=rus_platform, caption="ВЫБЕРИТЕ ПЛАТФОРМУ 🇷🇺", reply_markup=rus_in_web_games)
    elif call.data == "rus_in_pc_web_games":
        await bot.send_photo(call.from_user.id, photo=pc, caption="Выбирай любую игру какую хочешь 🇷🇺", reply_markup=rus_in_pc_web_games)
    elif call.data == "rus_in_phone_web_games":
        await bot.send_photo(call.from_user.id, photo=rus_phone, caption="Выбирай любую игру какую хочешь 🇷🇺", reply_markup=rus_in_phone_web_games)
    elif call.data == "rus_in_mod_bl":
        await bot.send_photo(call.from_user.id, photo=rus_mod_bl, caption="МОД НА БЕСКНОНЕЧНОГО ЛЕТО 🇷🇺", reply_markup=rus_in_mod_bl)
    elif call.data == "rus_in_google_play":
        await bot.send_photo(call.from_user.id, photo=google_play, caption="GOOGLE PLAY 🇷🇺", reply_markup=rus_in_google_play)
    elif call.data == "rus_in_social_network":
        await bot.send_photo(call.from_user.id, photo=rus_social_network, caption="СОЦИАЛЬНЫЕ СЕТИ 🇷🇺", reply_markup=rus_in_social_network)
    elif call.data == "rus_in_FAQ":
        await bot.send_photo(call.from_user.id, photo=faq, caption="Мы ответили на часто задаваемые вопросы для вашего удобства 🇷🇺", reply_markup=rus_in_FAQ)
    elif call.data == "rus_in_Profile":
        await bot.send_photo(call.from_user.id, photo=rus_profile, caption=f"ID вашего профиля: {call.from_user.id} \nВы человек \nЖелаем удачи в пользовании ботом 🇷🇺", reply_markup=rus_in_Profile)
    elif call.data == "rus_in_donation":
        await bot.send_photo(call.from_user.id, photo=rus_donation, caption="Вы можете помочь нам стать лучше 🇷🇺", reply_markup=rus_in_donation)



# Register dispather
def register_handlers_client(dp : Dispatcher):
  dp.register_message_handler(command_start, commands=["start"])

if __name__ == "__main__":
	executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)